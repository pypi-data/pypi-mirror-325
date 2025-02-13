import re
from kabaret.app.ui.gui.widgets.flow.flow_view import QtCore, QtGui, QtWidgets, CustomPageWidget
from kabaret.app import resources
from libreflow.resources.icons import gui as _
from libreflow.baseflow.ui.mytasks.components import LabelIcon

STYLESHEET = '''
    QPushButton:disabled {
        background-color: rgba(255, 255, 255, 0);
        color: rgba(255, 255, 255, 50);
    }'''


class ShotListSearch(QtWidgets.QLineEdit):

    def __init__(self, page_widget):
        super(ShotListSearch, self).__init__()
        self.page_widget = page_widget

        self.setStyleSheet('''
        QLineEdit {
            background-color: #232d33;
            border: 2px solid #4c4c4c;
            border-radius: 7px;
            padding-left: 30px;
        }''')

        self.setMaximumWidth(225)
        self.setMaximumHeight(32)

        self.build()

    def build(self):
        self.search_icon = LabelIcon(('icons.search', 'magn-glass'), 18)

        lo = QtWidgets.QHBoxLayout(self)
        lo.setContentsMargins(9,0,0,0)
        lo.addWidget(self.search_icon, 0, QtCore.Qt.AlignLeft)

        self.setClearButtonEnabled(True)

    def keyPressEvent(self, event):
        if (event.key() == QtCore.Qt.Key_Escape) or (event.key() == QtCore.Qt.Key_Return):
            self.clearFocus()
        else:
            super(ShotListSearch, self).keyPressEvent(event)


class ShotListItem(QtWidgets.QTreeWidgetItem):

    ICON_BY_STATUS = {
        'Download': ('icons.libreflow', 'download'),
        'None':   ('icons.libreflow', 'cross-mark-on-a-black-circle-background-colored'),
        'Re-render':   ('icons.libreflow', 'cross-mark-on-a-black-circle-background-colored')
    }

    def __init__(self, tree, item):
        super(ShotListItem, self).__init__(tree)
        self.shot = item
        self.tree = tree

        self.refresh()

    def refresh(self):
        self.setText(0, self.shot.seq_name.get())
        self.setIcon(0, self.get_icon(self.ICON_BY_STATUS[self.shot.status.get()]))
        
        self.setText(1, self.shot.shot_name.get())
        self.setText(2, self.shot.rev_name.get())
        if self.shot.source_site.get():
            self.setText(4, self.shot.source_site.get())
        elif self.tree.itemWidget(self, 5) is not None:
            self.setText(4, "")
            download_btn = self.tree.itemWidget(self, 7)
            download_btn.hide()
        
        if self.shot.status.get() in ['None', 'Re-render']:
            self.setCheckState(0, QtCore.Qt.Checked)
            self.refresh_sync_status()
        elif self.shot.status.get() == 'Download':
            self.setCheckState(0, QtCore.Qt.Unchecked)
        
        self.setCheckState(6, QtCore.Qt.Unchecked)
    
    def refresh_sync_status(self, status=""):
        if status == "Download":
            index = self.tree.indexOfTopLevelItem(self)
            self.tree.takeTopLevelItem(index)
            del self
        elif status == "Request":
            self.setText(5, "Requested")
        elif self.shot.status.get() == "Re-render" and self.shot.source_site.get():
            self.setText(5, "Not available")
            
            download_btn = self.tree.itemWidget(self, 7)
            if download_btn is not None:
                download_btn.hide()
    
    @staticmethod
    def get_icon(icon_ref):
        return QtGui.QIcon(resources.get_icon(icon_ref))


class ShotList(QtWidgets.QTreeWidget):
    
    def __init__(self, custom_widget, session):
        super(ShotList, self).__init__()
        self.custom_widget = custom_widget
        self.session = session

        self.download_check = False
        self.search_keys = ['source_display', 'job_type', 'status', 'user', 'site']

        self.setHeaderLabels(self.get_header_labels())

        self.refresh()

        self.header().resizeSections(QtWidgets.QHeaderView.ResizeToContents)
        self.setColumnWidth(2, self.columnWidth(2) + 30)
        self.setColumnWidth(3, self.columnWidth(3) + 50)

        self.itemChanged.connect(self._on_item_changed)
    
    def get_header_labels(self):
        return ['Sequence', 'Shot', 'Revision', 'Pool', 'Source Site', 'Sync Status', 'Prores', '']
    
    def refresh(self, force_update=False):
        self.clear()
        shots = self.session.cmds.Flow.call(
            self.custom_widget.oid, 'get_shots', {force_update}, {}
        )

        for item in shots:
            entry = ShotListItem(self, item)
            
            # Pool selection
            pool_cmb = QtWidgets.QComboBox()
            for pool in self.custom_widget.pools:
                pool_cmb.addItem(pool)
                pool_cmb.setCurrentText(item.pool_name.get())
            pool_cmb.currentTextChanged.connect(lambda text, i=item: self._on_pool_changed(i, text))

            self.setItemWidget(entry, 3, pool_cmb)

            # Download/Request button
            if item.status.get() == "Download":
                self.download_check = True

                download_widget = QtWidgets.QWidget()
                download_layout = QtWidgets.QHBoxLayout(download_widget)
                download_layout.setContentsMargins(0,0,0,0)

                download_btn = QtWidgets.QPushButton()
                download_btn.setIcon(QtGui.QIcon(resources.get_icon(('icons.libreflow', 'download'))))
                download_btn.setFixedSize(24,24)
                download_btn.clicked.connect(lambda checked=False, e=entry: self._on_download_clicked(e))

                download_layout.addWidget(download_btn, alignment=QtCore.Qt.AlignRight)

                self.setItemWidget(entry, 7, download_widget)

    def refresh_search(self, query_filter):
        count = 0
        keywords = query_filter.split()
        query_filter = '.*'+'.*'.join(keywords)

        for i in range(self.topLevelItemCount()):
            item = self.topLevelItem(i)
            if item is not None:
                matches = [
                    i for c in range(item.columnCount())
                    if re.match(query_filter, item.text(c))
                ]
                self.topLevelItem(i).setHidden(False if matches else True)
        
        self.custom_widget.shots_count.setText(self.get_shots_count())
    
    def get_shots_count(self):
        count = 0
        for i in range(self.topLevelItemCount()):
            item = self.topLevelItem(i)
            if item.isHidden() is False:
                count += 1

        if count > 1:
            return str(count) + " shots"
        if count == 1:
            return str(count) + " shot"
        return str(0) + " shots"
    
    def _on_pool_changed(self, item, text):
        item.pool_name.set(text)
    
    def _on_download_clicked(self, item):
        session = self.custom_widget.session
        format_log = f"[Batch Render Animspline] {item.shot.seq_name.get()} {item.shot.shot_name.get()} {item.shot.rev_name.get()}"

        status = item.shot.download()
        if status == "Request":
            session.log_info(f'{format_log} - Requested')
            item.refresh_sync_status("Request")
        elif status == "Download":
            session.log_info(f'{format_log} - Downloaded')
            item.refresh_sync_status("Download")
        else:
            session.log_info(f'{format_log} - Not Available. Can be re-rendered.')
            item.refresh()

    def _on_item_changed(self, item, column):
        if item.checkState(6) == QtCore.Qt.Checked:
            item.shot.prores.set(True)
        elif item.checkState(6) == QtCore.Qt.Unchecked:
            item.shot.prores.set(False)


class BatchRenderWidget(CustomPageWidget):

    def build(self):
        self.setStyleSheet(STYLESHEET)
        self.pools = self.session.cmds.Flow.call(
            self.oid, 'get_pools', {}, {}
        )
        self.temp_text_timer = QtCore.QTimer(self)

        self.shot_list = ShotList(self, self.session)
        self.shots_count = QtWidgets.QLabel(self.shot_list.get_shots_count())

        self.search = ShotListSearch(self)
        self.search.textChanged.connect(self.shot_list.refresh_search)
        
        self.button_refresh = QtWidgets.QPushButton(QtGui.QIcon(resources.get_icon(('icons.gui', 'refresh'))), '')
        self.button_refresh.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.button_refresh.setToolTip('Refresh shot list and reset selection')
        
        self.button_settings = QtWidgets.QPushButton(QtGui.QIcon(resources.get_icon(('icons.flow', 'action'))), '')
        self.button_settings.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)

        self.list_filter = QtWidgets.QComboBox()
        self.list_filter.addItems(['No filter', 'Not existing', 'Not downloaded', 'Not checked', 'Checked'])
        self.list_filter.setCurrentIndex(0)
        self.list_filter.currentTextChanged.connect(self._on_list_filter_changed)

        self.pool_cmb = QtWidgets.QComboBox()
        for pool in self.pools:
            self.pool_cmb.addItem(pool)
        self.pool_cmb.currentTextChanged.connect(self._on_pool_changed)

        self.button_copy_last_batch = QtWidgets.QPushButton('Copy last batch')
        self.button_render = QtWidgets.QPushButton('Render')
        
        self.checkbox_selectall = QtWidgets.QCheckBox('Select all')
        self.checkbox_selectall.setCheckState(QtCore.Qt.Checked)

        self.button_download_all = QtWidgets.QPushButton('Download All')

        for i in range(self.shot_list.topLevelItemCount()):
            shot = self.shot_list.topLevelItem(i)
            if shot.checkState(0) == QtCore.Qt.Checked:
                self.button_render.setEnabled(True)
                break
            else:
                self.button_render.setEnabled(False)

        glo = QtWidgets.QGridLayout()
        glo.addWidget(self.shots_count, 0, 0, 1, 6)
        glo.addWidget(self.search, 1, 0, 1, 6)
        glo.addWidget(self.shot_list, 2, 0, 1, 7)
        glo.addWidget(self.button_refresh, 3, 0)
        glo.addWidget(self.button_settings, 3, 1)
        glo.addWidget(self.list_filter, 3, 2)
        glo.addWidget(self.pool_cmb, 3, 3)
        glo.addWidget(self.button_copy_last_batch, 3, 5)
        glo.addWidget(self.button_render, 3, 6)
        glo.addWidget(self.checkbox_selectall, 4, 2)
        if self.shot_list.download_check:
            glo.addWidget(self.button_download_all, 4, 6)

        self.setLayout(glo)
    
        # Install callbacks
        self.button_refresh.clicked.connect(self._on_button_refresh_clicked)
        self.button_settings.clicked.connect(self._on_button_settings_clicked)
        self.checkbox_selectall.stateChanged.connect(self._on_checkbox_selectall_state_changed)
        self.button_copy_last_batch.clicked.connect(self._on_button_copy_last_batch_clicked)
        self.button_render.clicked.connect(self._on_button_render_clicked)
        self.button_download_all.clicked.connect(self._on_button_download_clicked)

    def _on_button_refresh_clicked(self):
        self.checkbox_selectall.setCheckState(QtCore.Qt.Checked)

        self.status_feedback.setText('Loading...')
        QtWidgets.QApplication.processEvents()
        QtWidgets.QApplication.processEvents()
        self.shot_list.refresh(force_update=True)

        self.shots_count.setText(self.shot_list.get_shots_count())
        self.status_feedback.setText('')
    
    def _on_button_settings_clicked(self):
        self.page.goto(self.oid + '/settings')

    def _on_list_filter_changed(self, text):
        # Reset
        for i in range(self.shot_list.topLevelItemCount()):
            item = self.shot_list.topLevelItem(i)
            if item:
                item.setHidden(False)
        
        if self.search.text() != "":
            self.search.setText("")

        # Hide
        for i in range(self.shot_list.topLevelItemCount()):
            item = self.shot_list.topLevelItem(i)
            if item:
                if (
                    (text == "Not existing" and item.shot.status.get() != "None")
                    or (text == "Not downloaded" and item.shot.status.get() != "Download")
                    or (text == "Not checked" and item.checkState(0) == QtCore.Qt.Checked)
                    or (text == "Checked" and item.checkState(0) != QtCore.Qt.Checked)
                ):
                    item.setHidden(True)
        
        self.shots_count.setText(self.shot_list.get_shots_count())

    def _on_pool_changed(self, text):
        for i in range(self.shot_list.topLevelItemCount()):
            item = self.shot_list.topLevelItem(i)
            if item:
                item.shot.pool_name.set(text)
                pool_cmb = self.shot_list.itemWidget(item, 3)
                pool_cmb.setCurrentText(text)

    def _on_button_copy_last_batch_clicked(self):
        self.temp_text_timer.stop()

        copy_last_render = self.session.cmds.Flow.call(
            self.oid, 'copy_last_render', {}, {}
        )

        if copy_last_render == 'Not configured':
            self.button_copy_last_batch.setText('Logs disabled!')
        if copy_last_render == 'Not found':
            self.button_copy_last_batch.setText('No log found!')
        if copy_last_render == 'Copied':
            self.button_copy_last_batch.setText('Copied!')

        self.temp_text_timer.setInterval(5000)
        self.temp_text_timer.timeout.connect(self._reset_last_batch_feedback)
        self.temp_text_timer.start()
    
    def _reset_last_batch_feedback(self):
        self.button_copy_last_batch.setText('Copy last batch')

    def _on_button_render_clicked(self):
        selected_shots = []

        for i in range(self.shot_list.topLevelItemCount()):
            item = self.shot_list.topLevelItem(i)
            if item.checkState(0) == QtCore.Qt.Checked:
                selected_shots.append(item.shot)
        
        # self.status_feedback.setText('Submit jobs...')
        # QtWidgets.QApplication.processEvents()
        # QtWidgets.QApplication.processEvents()
        
        self.session.cmds.Flow.call(
            self.oid, 'render', [selected_shots], {}
        )

        self.shot_list.refresh(force_update=True)
        self.shots_count.setText(self.shot_list.get_shots_count())
        # self.status_feedback.setText('Completed')
    
    def _on_checkbox_selectall_state_changed(self, state):
        state = QtCore.Qt.CheckState(state)
        for i in range(self.shot_list.topLevelItemCount()):
            item = self.shot_list.topLevelItem(i)
            if item:
                if self.list_filter.currentText() == "No filter" and item.shot.status.get() == "Download":
                    continue
                self.shot_list.topLevelItem(i).setCheckState(0, state)

    def _on_button_download_clicked(self):
        for i in range(self.shot_list.topLevelItemCount()):
            item = self.shot_list.topLevelItem(i)
            if item.shot.status.get() == "Download":
                self.shot_list._on_download_clicked(item)

