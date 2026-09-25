# Functional geometry environment plan

## Dependencies

- Retain the existing system installation of LibreOffice and Poppler for DOCX-to-PDF conversion and PDF inspection.
- Create `functional_geometry/.venv` with Python 3.
- Install the exact versions in `functional_geometry/requirements.txt`.

## Reproduction commands

- Analysis: `cd functional_geometry && make analysis`
- Manuscript package: `cd functional_geometry && make manuscript`
- Tests: `cd functional_geometry && make test`
- Full build and QC: `cd functional_geometry && make all`

## Blueprint change

Add one incremental maintenance command that creates the project virtual environment if absent and installs pinned requirements. Add a short knowledge entry documenting the verified one-command build. No task-specific build will run during snapshot creation.

## Pre-commit

The repository has no `.pre-commit-config.yaml`, so no hook installation is proposed.
