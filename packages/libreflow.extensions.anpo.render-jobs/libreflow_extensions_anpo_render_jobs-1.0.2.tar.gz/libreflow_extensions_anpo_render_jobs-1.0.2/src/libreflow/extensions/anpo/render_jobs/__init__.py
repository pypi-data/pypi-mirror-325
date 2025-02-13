import os
import re
import pathlib
import time
from bson.objectid import ObjectId
from datetime import datetime
from pprint import pprint
from kabaret import flow
from kabaret.app import resources
from kabaret.flow_contextual_dict import get_contextual_dict
from kabaret.app.ui.gui.widgets.widget_view import QtWidgets
from kabaret.flow.object import _Manager
from libreflow.baseflow.file import LinkedJob, TrackedFile, RenderBlenderPlayblast
from libreflow.flows.default.flow.film import Film
from libreflow.utils.kabaret.jobs.jobs_flow import Job, Jobs
from libreflow.utils.b3d import wrap_python_expr

from . import _version
__version__ = _version.get_versions()['version']


def get_time():
    return str(datetime.now().strftime(" %H:%M:%S (%d/%m)"))


class RenderBlenderProresPlayblast(RenderBlenderPlayblast):

    prores_clean = flow.BoolParam(True)

    def playblast_infos_from_revision(self, revision_name):
        filepath = self._file.path.get()
        filename = "_".join(self._file.name().split("_")[:-1])

        playblast_filename = filename + "_prores_movie"
        playblast_revision_filename = self._file.complete_name.get() + "_prores_movie.mov"
        
        playblast_filepath = os.path.join(
            self.root().project().get_root(),
            os.path.dirname(filepath),
            playblast_filename + "_mov",
            revision_name,
            playblast_revision_filename
        )

        return playblast_filepath, playblast_filename, self._file.path_format.get()

    def extra_argv(self):
        file_settings = get_contextual_dict(
            self._file, "settings", ["sequence", "shot"]
        )
        project_name = self.root().project().name()
        revision = self._file.get_revision(self.revision_name.get())
        do_render = self.quality.get() == 'Final'
        python_expr = """import bpy
bpy.ops.lfs.playblast(do_render=%s, filepath='%s', studio='%s', project='%s', sequence='%s', scene='%s', quality='%s', version='%s', template_path='%s', do_autoplay=%s, frame_count=%s, prores_clean=%s)""" % (
            str(do_render),
            self.output_path,
            self.root().project().get_current_site().name(),
            project_name,
            file_settings.get("sequence", "undefined"),
            file_settings.get("shot", "undefined"),
            'PREVIEW' if self.quality.get() == 'Preview' else 'FINAL',
            self.revision_name.get(),
            resources.get('mark_sequence.fields', 'default.json').replace('\\', '/'),
            self.auto_play_playblast.get(), 
            self.get_shot_frame_count(),
            self.prores_clean.get()
        )
        if not do_render:
            python_expr += "\nbpy.ops.wm.quit_blender()"
        
        args = [
            revision.get_path(),
            "--addons",
            "mark_sequence",
            "--python-expr",
            wrap_python_expr(python_expr),
        ]

        if do_render:
            args.insert(0, '-b')
        
        return args


class RenderJob(LinkedJob):

    def get_log_filename(self):
        filename = f"anpo_{self.seq_name.get()}_{self.shot_name.get()}_{self.task_name.get()}_{self.file_name.get()}_{self.job_id.get()}.job_log"
        log_path = pathlib.Path.home()/f".libreflow/log/jobs/{self.root().project().name()}/{filename}"
        return log_path

    def is_running(self, runner_id):
        info = self.root().session().cmds.SubprocessManager.get_runner_info(
            runner_id)
        return info['is_running']

    def show_runner_info(self, runner_info, description=None):
        if description is not None:
            description = "- "+description
        else:
            description = ""
        self.show_message(f"[INFO] Runner {runner_info['id']} started...")
        self.show_message(f"[INFO] Description: {runner_info['label']} {description}")
        self.show_message(f"[INFO] Command: {runner_info['command']}")
        self.show_message(f"[INFO] Log path: {runner_info['log_path']}")

    # Use old runner handlers prototype in Scene Builder extension
    # TODO: Migrate to the version in kabaret.subprocess_manager
    # def check_process_errors(self, log_path, runner_name, label):
    #     """
    #     Check for errors in the given log file path matched by
    #     error handlers associated to the given runner name.
    #     """
    #     self.show_message("Checking for errors...")
    #     handlers = self.root().project().admin.project_settings.runner_error_handlers
    #     msg = None
    #     error = None
    #     for handler in handlers.get_handlers(runner_name):
    #         error = handler.match(log_path)
    #         if error is not None:
    #             msg = handler.description.get()
    #             break

    #     if msg is not None:
    #         print(f"[ERROR] {msg}\n\n{error}\n")
    #         raise Exception(f"{msg}\n############# {label} - Failure #############" + get_time())

    def get_label(self):
        raise NotImplementedError()

    def wait_runner(self, runner_id):
        if runner_id is None:
            raise Exception("Runner undefined")

        info = self.root().session().cmds.SubprocessManager.get_runner_info(runner_id)
        self.show_runner_info(info)
        while self.is_running(runner_id):
            time.sleep(1)
        self.show_message(f"[RUNNER] Runner {runner_id} finished")
        # self.check_process_errors(info['log_path'], info['name'], self.get_label())


class RenderAnimsplineJob(RenderJob):

    blend_oid   = flow.Param("")
    seq_name    = flow.Param("")
    shot_name   = flow.Param("")
    task_name   = flow.Param("animspline")
    file_name   = flow.Param("anim_spline_blend")
    rev_name    = flow.Param("")
    shot_status = flow.Param("")
    prores      = flow.Param(False)

    def get_label(self):
        return 'RENDER ANIMSPLINE'

    def _do_job(self):
        _file = self.root().get_object(self.blend_oid.get())
        if _file is None:
            raise Exception(f"Rendering scene not found")

        # Start render playblast action
        print(f"############# {self.get_label()} - Start #############" + get_time())
        self.root().project().ensure_runners_loaded()
        if self.prores.get():
            render_playblast = _file.render_blender_prores_playblast
        else:
            render_playblast = _file.render_blender_playblast
        render_playblast.revision_name.set(self.rev_name.get())
        render_playblast.auto_play_playblast.set(False)
        render_playblast.quality.set('Final')
        result = render_playblast.run('Render')
        self.wait_runner(result['runner_id'])
        
        # Create Upload Job if re-render
        if self.shot_status.get() == "Re-render":
            current_site = self.root().project().get_current_site()
            sync_job_queue = current_site.get_queue()

            sync_job_queue.submit_job(
                emitter_oid=f"{self.blend_oid.get()}/history/revisions/{self.rev_name.get()}",
                user=self.root().project().get_user_name(),
                studio=current_site.name(),
                job_type='Upload',
                init_status='WAITING'
            )

        print(f"############# {self.get_label()} - End #############" + get_time())


class RenderJobs(Jobs):

    @classmethod
    def job_type(cls):
        return RenderJob

    def create_job(self, shot, job_type=None):
        name = '{}{:>05}'.format(self._get_job_prefix(), self._get_next_job_id())
        job = self.add(name, object_type=job_type)
        job.blend_oid.set(shot.blend_oid.get())
        job.seq_name.set(shot.seq_name.get())
        job.shot_name.set(shot.shot_name.get())
        job.rev_name.set(shot.rev_name.get())
        job.shot_status.set(shot.status.get())
        job.prores.set(shot.prores.get())
        return job

    def columns(self):
        return ['Status', 'Sequence', 'Shot', 'Task', 'File', 'Pool', 'Creator', 'Created On']

    def _fill_row_cells(self, row, item):
        on = item.created_on.get()
        try:
            on = float(on)
        except:
            pass
        else:
            on = time.ctime(on)

        row.update(dict(
            Status=item.status.get(),
            Sequence=item.seq_name.get(),
            Shot=item.shot_name.get(),
            Task=item.task_name.get(),
            File=item.file_name.get(),
            Pool=item.get_job().get('pool', '???'),
            Creator=item.owner.get()
        ))
        row['Created On'] = on


class BlenderShot(flow.Object):

    blend_oid     = flow.SessionParam()
    mov_oid       = flow.SessionParam()
    seq_name      = flow.SessionParam()
    shot_name     = flow.SessionParam()
    rev_name      = flow.SessionParam()
    source_site   = flow.SessionParam()
    status        = flow.SessionParam()
    pool_name     = flow.SessionParam()
    sync_job_id   = flow.SessionParam()
    prores        = flow.SessionParam(False)

    def find_existing_job(self, job_queue, job_type, job_status):
        coll = job_queue.get_entity_store().get_collection(
            job_queue.collection_name())
        result = coll.find({'emitter_oid': self.mov_oid.get(),
                            'type': job_type,
                            'status': job_status})

        return list(result) if result is not None else None

    def download(self):
        mov_rev = self.root().get_object(self.mov_oid.get())

        # Download revision if available in exchange server
        if mov_rev.get_sync_status(exchange=True) == 'Available':
            mov_rev.download.run('Confirm')
            return "Download"
        else:
            sites = self.root().project().get_working_sites()
            source_site = sites[self.source_site.get()]

            # Mark as "ready for render", if upload job from source site has an error
            job_exists = self.find_existing_job(source_site.get_queue(), 'Upload', 'ERROR')
            if job_exists:
                self.sync_job_id.set(job_exists[0]['_id'])
                self.status.set('Re-render')
                return "Re-render"
            # Create a request
            else:
                mov_rev.request.get_buttons()
                mov_rev.request.run('Request')

            return "Request"


class BlenderShots(flow.DynamicMap):

    _settings = flow.Parent()

    def __init__(self, parent, name):
        super(BlenderShots, self).__init__(parent, name)
        self._document_cache = None
        self._document_cache_key = None

    @classmethod
    def mapped_type(cls):
        return BlenderShot

    def columns(self):
        return ['Sequence', 'Shot', 'Revision', 'Status']

    def mapped_names(self, page_num=0, page_size=None):
        cache_key = (page_num, page_size)
        
        # Update if no cache or time elapsed
        if (
            self._document_cache is None
            or self._document_cache_key != cache_key
        ):
            self._mng.children.clear()
            self._document_cache = {}

            self.root().session().log_info('[Batch Render Animspline] Fetching Shots (it may take a while)')
            self.get_shots_to_render()

            self._document_cache_key = cache_key
            self.root().session().log_info('[Batch Render Animspline] Data updated')

        return self._document_cache.keys()

    def get_shots_to_render(self):
        session = self.root().session()

        # Get root path
        root_path = self.root().project().get_root()

        # Get current site name
        current_site = self.root().project().get_current_site_name()

        # Fetch most recent published revisions
        rev_col = self.root().project().admin.entity_manager.get_revision_collection()

        blend_datas = (
            rev_col.get_entity_store()
            .get_collection(rev_col.collection_name())
            .find({"name": {"$regex": "anim_spline_blend"}, "working_copy": False})
        )
        blend_datas = list(blend_datas)

        mov_datas = (
            rev_col.get_entity_store()
            .get_collection(rev_col.collection_name())
            .find({"name": {"$regex": "anim_spline_movie_mov"}, "working_copy": False})
        )
        mov_datas = list(mov_datas)
        
        seq_name = None
        shot_name = None
        index_start = 0
        # for i, data in enumerate(blend_datas[0:300]): # For testing purposes
        for i, data in enumerate(blend_datas):
            seq_match = re.search('sq\d{3}[a-z]*', data['name'])
            shot_match = re.search('sh\d{5}', data['name'])

            # Ignore non shots
            if seq_match is None or shot_match is None:
                seq_match = ""
                shot_match = ""
            # Convert match object to str
            else:
                seq_match = seq_match.group(0)
                shot_match = shot_match.group(0)

            # For init
            if seq_name is None or shot_name is None:
                seq_name = seq_match
                shot_name = shot_match
            # Get latest animspline revision for shot
            elif (seq_name != seq_match) or (shot_name != shot_match):
                blend_revisions = [rev for rev in blend_datas[index_start:i]]
                blend_revision = max(blend_revisions, key = lambda r: r['name'])
                blend_oid = re.search('.*(?=\/history)', blend_revision['name']).group(0)

                seq_blend_name = re.search('sq\d{3}[a-z]*', blend_revision['name']).group(0)
                shot_blend_name = re.search('sh\d{5}', blend_revision['name']).group(0)
                rev_blend_name = re.search('v\d{3}', blend_revision['name']).group(0)

                # Check if movie exists
                blend_path = os.path.normpath(os.path.join(root_path, blend_revision['path']))
                if os.path.exists(blend_path) is False:
                    session.log_info(f"[Batch Render Animspline] {seq_blend_name} {shot_blend_name} {rev_blend_name} - blend file don't exist")
                    seq_name = seq_match
                    shot_name = shot_match
                    continue

                mov_query = (
                    rev_col.get_entity_store()
                    .get_collection(rev_col.collection_name())
                    .find_one({"name": {"$regex": f"({seq_blend_name}).*({shot_blend_name}).*(anim_spline_movie_mov).*({rev_blend_name})"}, "working_copy": False})
                )

                i = len(self._document_cache) + 1
                # No entry = Movie don't exist
                if mov_query is None:
                    session.log_info(f"[Batch Render Animspline] {seq_blend_name} {shot_blend_name} {rev_blend_name} - movie not created")
                    self._document_cache['shot'+str(i)] = dict(
                        blend_oid=blend_oid,
                        mov_oid=None,
                        seq_name=seq_blend_name,
                        shot_name=shot_blend_name,
                        rev_name=rev_blend_name,
                        source_site=None,
                        status="None"
                    )
                else:
                    mov_path = os.path.normpath(os.path.join(root_path, mov_query['path']))
                    # Path don't exist
                    if os.path.exists(mov_path) is False:
                        session.log_info(f"[Batch Render Animspline] {seq_blend_name} {shot_blend_name} {rev_blend_name} - movie not available on site")
                        # Entry created from which site ?
                        if current_site != mov_query['site']:
                            self._document_cache['shot'+str(i)] = dict(
                                blend_oid=blend_oid,
                                mov_oid=mov_query['name'],
                                seq_name=seq_blend_name,
                                shot_name=shot_blend_name,
                                rev_name=rev_blend_name,
                                source_site=mov_query['site'],
                                status="Download"
                            )
                        else:
                            session.log_info(f"[Batch Render Animspline] {seq_blend_name} {shot_blend_name} {rev_blend_name} - movie don't exist")
                            self._document_cache['shot'+str(i)] = dict(
                                blend_oid=blend_oid,
                                mov_oid=mov_query['name'],
                                seq_name=seq_blend_name,
                                shot_name=shot_blend_name,
                                rev_name=rev_blend_name,
                                source_site=mov_query['site'],
                                status="None"
                            )

                # Update variables for compare
                index_start = i
            
            seq_name = seq_match
            shot_name = shot_match

    def get_cache_key(self):
        return self._document_cache_key

    def touch(self):
        self._document_cache = None
        super(BlenderShots, self).touch()

    def _configure_child(self, child):
        child.blend_oid.set(self._document_cache[child.name()]['blend_oid'])
        child.mov_oid.set(self._document_cache[child.name()]['mov_oid'])
        child.seq_name.set(self._document_cache[child.name()]['seq_name'])
        child.shot_name.set(self._document_cache[child.name()]['shot_name'])
        child.rev_name.set(self._document_cache[child.name()]['rev_name'])
        child.source_site.set(self._document_cache[child.name()]['source_site'])
        child.status.set(self._document_cache[child.name()]['status'])
        child.pool_name.set(self._settings.default_pool.get())

    def _fill_row_cells(self, row, item):
        row["Sequence"] = item.seq_name.get()
        row["Shot"] = item.shot_name.get()
        row["Revision"] = item.rev_name.get()
        row["Status"] = item.status.get()


class DefaultPoolName(flow.values.SessionValue):
    
    DEFAULT_EDITOR = 'choice'
    STRICT_CHOICES = False
    
    def choices(self):
        current_site = self.root().project().get_current_site()
        return current_site.pool_names.get()

    def revert_to_default(self):
        names = self.choices()
        if names:
            self.set(names[0])


class BatchRenderSettings(flow.Object):

    shots = flow.Child(BlenderShots)

    default_pool = flow.SessionParam(None, DefaultPoolName)
    render_log_folder = flow.Param(None)

    # TODO: Update Kitsu status
    #     kitsu_task = flow.SessionParam('Shots_Rendering')
    #     kitsu_status_start = flow.SessionParam('Work In Progress')
    #     kitsu_status_end = flow.SessionParam('Sup Approval')


class BatchRenderAnimsplineAction(flow.Action):

    ICON = ('icons.libreflow', 'blender')

    settings = flow.Child(BatchRenderSettings)

    _film = flow.Parent()

    def __init__(self, parent, name):
        super(BatchRenderAnimsplineAction, self).__init__(parent, name)
        self.today = datetime.now()
        self.timestamp = self.today.strftime("%y%m%d")

    def allow_context(self, context):
        return context

    def needs_dialog(self):
        self.settings.default_pool.revert_to_default()
        return True

    def get_buttons(self):
        return ['Build', 'Cancel']

    def get_shots(self, force_update=False):
        if force_update:
            self.settings.shots.touch()
        return self.settings.shots.mapped_items()

    def copy_last_render(self):
        if self.settings.render_log_folder.get() is None:
            return 'Not configured'

        render_log_folder = os.path.join(self.root().project().get_root(), self.settings.render_log_folder.get())

        log_files = [
            os.path.join(render_log_folder, x)
            for x in os.listdir(render_log_folder)
            if x.endswith(".txt")
        ]
        if log_files != []:
            latestFile = max(log_files, key = os.path.getctime)
            file_content = open(latestFile, 'r').read()
            app = QtWidgets.QApplication.instance()
            clip = app.clipboard()
            clip.setText(file_content)
            return 'Copied'
        else:
            return 'Not found'

    def get_pools(self):
        return self.settings.default_pool.choices()

    def submit_job(self, job, pool_name, label, user_name, paused):
        job.submit(pool_name, 100, label, \
            user_name, user_name, paused, False)

    def render(self, shots):
        # Fetch current user name
        user_name = self.root().project().get_user_name()

        # Prepare log file
        if self.settings.render_log_folder is not None:
            render_log_folder = os.path.join(self.root().project().get_root(), self.settings.render_log_folder.get())

            log_file = os.path.join(render_log_folder, self.timestamp + "_{}.txt")
            counter = 1

            while os.path.exists(log_file.format(counter)):
                counter += 1
            log_file = log_file.format(counter)

        # Render shots
        for shot in shots:
            shot_data = f"{shot.seq_name.get()} {shot.shot_name.get()} {shot.rev_name.get()}"
            
            # Add shot entry to log file
            if self.settings.render_log_folder is not None:
                with open(log_file, 'a') as f:
                    f.write(f"{shot_data} - {shot.pool_name.get()}\n")

            # Create render job
            job_render = self._film.render_jobs.create_job(shot, RenderAnimsplineJob)

            self.submit_job(job_render, shot.pool_name.get(),
                f"RENDER ANIMSPLINE {shot_data}",
                user_name, False
            )

            self.root().session().log_info(f'[Batch Render Animspline] {shot_data} - Job submitted!')

            # Delete download job if needed
            if shot.sync_job_id.get():
                # Delete entry from mongo sync collection of current working site
                current_site = self.root().project().get_current_site()
                sync_job_queue = current_site.get_queue()

                collection = sync_job_queue.get_entity_store().get_collection(sync_job_queue.collection_name())

                collection.delete_one({"_id": ObjectId(shot.sync_job_id.get())})

        # Show how many shots will be rendered
        shots_count = len(shots)
        self.root().session().log_info(f'[Batch Render Animspline] {str(shots_count)} render jobs submits!')

        if self.settings.render_log_folder is not None:
            with open(log_file, 'a') as f:
                shots_count = str(shots_count) + " render jobs submits!"
                f.write(shots_count)

    # TODO: Snippet for update Kitsu Status
    # def run(self, button):
        # if button == 'Cancel':
            # return

        # pool_name = self.pool.get()
        # d = get_contextual_dict(self, 'settings')
        # kitsu_api = self.root().project().kitsu_api()
        # kitsu_api.set_shot_task_status(d['sequence'],
        #                                d['shot'],
        #                                self.kitsu_task.get(),
        #                                self.kitsu_status_start.get(),
        #                                comment=f'en cours de rendu sur {pool_name}',
        #                                episode_name=None)
        # user_name = self.root().project().get_user_name()
        # site = self.root().project().get_current_site()
        # pool_name = self.pool.get()

        # job_render_comp_movie = self._task.jobs.create_job(MarkImageSequenceJob)
        # job_render_comp_movie.kitsu_task.set(self.kitsu_task.get())
        # job_render_comp_movie.kitsu_status_end.set(self.kitsu_status_end.get())
    
    def _fill_ui(self, ui):
        ui['custom_page'] = 'libreflow.extensions.anpo.render_jobs.ui.BatchRenderWidget'


def render_jobs(parent):
    if type(parent) is Film:
        batch_render_animspline = flow.Child(BatchRenderAnimsplineAction)
        batch_render_animspline.name = 'batch_render_animspline'
        batch_render_animspline.index = None
        batch_render_animspline.ui(label='Batch Render Animspline', dialog_size=(850, 600))

        render_jobs = flow.Child(RenderJobs)
        render_jobs.name = 'render_jobs'
        render_jobs.index = None
        render_jobs.ui(expanded=False, show_filter=True)

        return [
            batch_render_animspline,
            render_jobs,
        ]

    if isinstance(parent, TrackedFile):
        prores_playblast = flow.Child(RenderBlenderProresPlayblast)
        prores_playblast.name = 'render_blender_prores_playblast'
        prores_playblast.index = None
        prores_playblast.ui(hidden=True)
        
        return prores_playblast


def install_extensions(session):
    return {
        "render_jobs": [
            render_jobs,
        ]
    }
