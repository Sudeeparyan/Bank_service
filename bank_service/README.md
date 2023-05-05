## Installing poetry
> python -m pip install --user pipx </br>
> pipx install poetry

## To create poetry project
> poetry new bank_service --src

## Creating virtual env for the project
> poetry config virtualenvs.in-project true

## Activate the virtual env
> poetry shell

## Installing external packages required for the first time to add the dependencies
> poetry add fastapi uvicorn[standard] </br>
> poetry add -G dev pytest

## Installing packages from toml file and lock file
to install the pytest which is required only for the developers, use
> poetry install --with dev

else, to install packages other then the dev packages, use
> poetry install

If you would like to update the lock file, use
> poetry update

If you would like to install packages from lock file, use
> poetry install --sync

## Build package
To  build the wheel file, run the following command
> poetry build



