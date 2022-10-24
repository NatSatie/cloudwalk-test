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

*Packages:* Before running, you should also install the package `coverage`.

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

To run the tests, run the following commands.

```
python -m coverage run -m unittest
python -m coverage report
```

To check the visual report run

```python -m coverage html```

And open `htmlcov\index.html`.

## Expected outcomes

While we run `python main.py -i input/game2.log -o output/game2`, we should expect to read the `game2.log` file and find a `game2.json` file in `output` folder. It should have information of two games, `game_0` and `game_1`.

If you run `python -m coverage report` intead, you should expect the printed result in your terminal:

```
Name                    Stmts   Miss  Cover
-------------------------------------------
MeansOfDeathEnum.py        31      0   100%
QuakeLog.py                38      2    95%
ReadFile.py                52     29    44%
tests\QuakeLogTest.py      38      0   100%
tests\ReadFileTest.py       6      1    83%
tests\__init__.py           3      0   100%
-------------------------------------------
TOTAL                     168     32    81%
```

Not all functions were properly covered, but they were registered as `TODO`s in ReadFileTest.

If we run `python -m coverage html`, we should expect to see in the `htmlcov\index.html` file a web page about the coverage of the code and information about each file. 

### Fun Facts of development

It was also added to the Github repo, a small Github actions yml file. 