# py-workshop-05-23
Code examples for the python workshop to be held on 4th May 2023

# Poetry Getting started
## Installing poetry
> python -m pip install pipx-in-pipx --user</br>
> pipx install poetry

## To create a poetry project
> poetry new project_name --src

## Poetry configuration to create virtual env within the project folder
> poetry config virtualenvs.in-project true

## Activate the virtual env
> poetry shell

## Adding external package dependencies to the project, Example below
> poetry add fastapi uvicorn[standard] </br>

## Adding external package dependencies required for development but not for deployment, Example below
> poetry add -G dev pytest

## To upgrade the packages and update the lock file
> poetry update

## Installing the dependencies from toml file
> poetry install

## Installing all the dependencies including dev dependencies from toml file
> poetry install --with dev

## Installing dependencies from lock file
> poetry install --sync

## To build package
> poetry build
