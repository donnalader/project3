# Starter code - OpenClassrooms WPS | P3

This repository contains the work that has been done so far on the chess tournament program.

### Data files

There are data files provided:
- JSON files for the chess clubs of Springfield and Cornville
- JSON files for two tournaments: one completed, and one in progress

### Models

This package contains the models already defined by the application:
* `Player` is a class that represents a chess player
* `Club` is a class that represents a chess club (including `Player`s)
* `ClubManager` is a manager class that allows to manage all clubs (and create new ones)

### Screens

This package contains classes that are used by the application to display information from the models on the screen.
Each screen returns a Command instance (= the action to be carried out).

### Commands

This package contains "commands" - instances of classes that are used to perform operations from the program.
Commands follow a *template pattern*. They **must** define the `execute` method.
When executed, a command returns a context.

### Main application

The main application is controlled by `manage_clubs.py`. Based on the current Context instance, it instantiates the screens and runs them. The command returned by the screen is then executed to obtain the next context.

The main application is an infinite loop and stops when a context has the attribute `run` set to False.

# How to Use the Tournament Manager
This is a commnand-line Pyhton application for managing chess (or any round-based) tournaments. Users can create tournaments, register players, run rounds, record match results, persist state to JSON, and generate polished HTML reports. 
### Project Overview
Tournament Manager is a Python Command Line Interface application that guides the user through the full lifecycle of a tournament:
1. Create a new tournament or load an existing one.
2. Register players and seed them into the bracket.
3. Generate rounds automatically with pairings.
4. Enter match results round by round.
5. Export results to a self-contained HTML report.
### Features
1. Tournament creation - name, location, date range and number of rounds.
2. Player management - add players with name and chess ID.
3. Automatic pairing - round generation with no repeat pairings.
4. Result entry - record wins, losses and draws per round.
5. Score tracking - running totals updated after every round.
6. JSON persistence - full state saved to and restored from .json files.
7. HTML report generation - stand alone reports with player standings.
8. flake8 HTNL reports - code quality reports included.
### Installation 
Clone the git repository: https://github.com/donnalader/project3.git
### How to Run the Program
python manage_clubs.py and the menu screens are self-explanatory and user-friendly. 
### How State is Saved and Loaded
All tournament data is automatically persisted to JSON files in the data directory after every change - no manual save step is needed.
  1. after a tournament is created
  2. after each player is added
  3. after each round is generated.
In-progress tournaments are in the in-progress.json. When a tournament is completed, the tournament actions menu has a option called 'Finish the Tournament' and that takes it out of the in-progress file and puts it is the completed.json file.
## Structure
All tournament files are divided into separate packages for Models, Screens and Commands following the MVC pattern. 
## Flake8 Report
I ran the flake8 report in python using: python -m flake8 --format=html --html=flake8-report


