[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# Base Hascode

## Setup ⚙️

### Prerequisites

[pyenv](https://github.com/pyenv/pyenv) and [Poetry](https://python-poetry.org/docs/) are already installed and configured.

### Install

- clone the repo and cd into it
- activate a compatible python version: `pyenv local 3.8.5`
- install the repo with all its dependencies: `make install`
    > NOTE: this also installs pre-commit hooks, and after the first commit it will take some time to setup the environments

### Run
- run the main function: `make run`
---