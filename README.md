# Static Type Checking in Python - Examples using MyPy

This purpose of this project is to demonstrate Python type annotations and static type checking, using [Mypy](http://mypy-lang.org), for commonly used sitautions - e.g. defing and using functions and classes. It consists of a Python 3 package with 3 modules, each of which demonstrates type annotation for a specific situation:

- function definition and usage;
- class definition and usage; and,
- named tuple definition and usage.

Extensive commentary has been included in the docstrings for each function as the aim is to read the code of a Python module that passes a static type check.

## Running MyPy

Analagous to a linter or a unit testing framwork, MyPy can be run from the command line as follows,

```bash
pipenv run python -m mypy examples/*.py
```

## MyPy Configuration

MyPy options for this project are kept in the `mypy.ini` file that MyPy will look for by default. For more information on the fulls set of options, see the [mypy documentation](https://mypy.readthedocs.io/en/stable/config_file.html).

## Project Dependencies

This project uses [pipenv](https://docs.pipenv.org) for managing dependencies (i.e. installing mypy) and Python environments (i.e. virtual environments).

### Installing Pipenv

To get started with Pipenv, first of all download it - assuming that there is a global version of Python available on your system and on the PATH, then this can be achieved by running the following command,

```bash
pip3 install pipenv
```

For more information, including advanced configuration options, see the [official pipenv documentation](https://docs.pipenv.org).

### Installing this Projects' Dependencies

Make sure that you're in the project's root directory (the same one in which `Pipfile` resides), and then run,

```bash
pipenv install --dev
```

This will install all of the direct project dependencies as well as the development dependencies (the latter a consequence of the `--dev` flag).
