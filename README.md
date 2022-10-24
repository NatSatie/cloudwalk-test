# Quake Game Log  Parser Code Challenge

### Summary


## Introduction

The main problem is to find more information about the main kills in the game, however, there's a few circuntances that makes reading the log complex.

1. There's one or more Quake game
2. The user might change username before the game starts
3. The game might not have properly shutdown properly

## How to run the application

### Run the application

```
python main.py -i input/qgames.log -o output/qgame
```

-i or --input: 
-o or --output: 

### Run the tests and coverage



```
python -m coverage run -m unittest
python -m coverage report
```