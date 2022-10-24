# Quake Game Log  Parser Code Challenge

### Table of Contents

1. [Introduction](#introduction)
2. [How to run the application](#how-to-run-the-application)
3. [Run the tests and coverage](#run-the-tests-and-coverage)

## Introduction

The main problem is to find more information about the main kills in the game, however, there's a few circuntances that makes reading the log complex.

1. There's one or more Quake game
2. The user might change username before the game starts
3. The game might not have properly shutdown properly

## How to run the application

### Install the application

*Version:* The application was created in Python 3.10, so we recommend to use the most recent version of Python.

*Packages: * Before running, you should also install the package `coverage`.

```
pip install coverage
```

### Run the application

Before running we recommend using the `/input` folder and `/output` folder. The input already has sample files to try it out.

After the application is done, the name of the output path, should save in `json` format, to make easier to organize data later on.

```
python main.py -i input/qgames.log -o output/qgame
```

## Run the tests and coverage

TO run the tests, run the following commands.

```
python -m coverage run -m unittest
python -m coverage report
```

To check the visual report run

```python -m coverage html```

And open `htmlcov\index.html`.