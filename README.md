## blueprint-batch-prefect

[![ci](https://github.com/FabienArcellier/blueprint-batch-prefect/actions/workflows/main.yml/badge.svg)](https://github.com/FabienArcellier/blueprint-batch-prefect/actions/workflows/main.yml)

This blueprint is a starting point for implementing a batch system that leverages prefect.

[Prefect](https://www.prefect.io) provides a development and runtime framework for scaling a batch system. 
Prefect also provides a supervision interface to monitor the status of different batches.

This blueprint can serve as a basis for

* an ETL system for transforming data into a datalake
* a regular batch system that calls on external systems

## Usage

Le déploiement de ce blueprint se fait avec ``docker-compose`` sur une seule machine. 

```bash
docker-compose up
```

Prefect supporte un déploiement en cluster. Ce blueprint ne l'implémente pas, vous pouvez le forker
et le faire évoluer pour le supporter.

### Interactive shell

Le shell interactif permet d'exécuter un flow et de le debugger pas à pas
sans écrire de test. Prefect ou pycharm ne fournit pas de manière simple pour invoquer un flow. 

Le shell interactif dans `tests/shell.py` s'exécute en debug depuis pycharm.

Si vous placez un point d'arret dans votre flow et appelez le flow dans le shell interactif, vous pourriez
le debugger pas à pas.

```python
fn(main.my_favorite_function)(12)
```

## Getting started

1. clone this repository

2. remove .git directory

## Latest version

You can find the latest version to ...

```bash
git clone https://github.com/FabienArcellier/blueprint-batch-prefect.git
```

## Developper guideline

### Build system

```text

```

### Add a dependency

``bash
poetry add requests
``
### Install development environment

Use make to instanciate a python virtual environment in ./venv and install the
python dependencies.

```bash
poetry install
```

### Update release dependencies

Use make to instanciate a python virtual environment in ./venv and freeze
dependencies version

```bash
poetry update update
```

### Activate the python environment

When you setup the requirements, a `venv` directory on python 3 is created.
To activate the venv, you have to execute :

```bash
poetry shell
```

### Run the continuous integration process

Before commit or send a pull request, you have to execute `pylint` to check the syntax
of your code and run the unit tests to validate the behavior.

```bash
$ poetry run alfred ci
```

## Contributors

* Fabien Arcellier

## License

MIT License

Copyright (c) 2018-2022 Fabien Arcellier

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
