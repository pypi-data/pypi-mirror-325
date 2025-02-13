# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html)[^1].

<!---
Types of changes

- Added for new features.
- Changed for changes in existing functionality.
- Deprecated for soon-to-be removed features.
- Removed for now removed features.
- Fixed for any bug fixes.
- Security in case of vulnerabilities.

-->

## [Unreleased]

## [1.0.2] - 2025-02-06

### Added

* Allow to render in Prores 422 HQ and without marking data.

## [1.0.1] - 2025-02-05

### Fixed

* Forgot to remove a testing mode (not fetching all the data)

## [1.0.0] - 2025-02-05

### Added

* An action for batch rendering Blender animspline files.
    * It fetches the latest available revision of each animspline task in the project.
    * If a movie has been created by another site, you can try to download it.
        * When the file is not available on the exchange server, the shot will be marked as "ready to re-render" on the current site.
    * Depending on how many shots are left to render, the first loading of the action may take a while.
        * For example, 400 shots can take up to a minute.
