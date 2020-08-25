# Phillies Assignment - Adam Beck
## Overview
Problem1: Please see the attached markdown file.

Problem2: Located in two folders, *Problem2* and *Problem2_Output_Sample*.

## Problem 2 Installation (MacOS, Linux, and Windows with WSL)
Ensure that you have python3 installed. After cloning this repository, create a virtual environment and download this project's dependencies by running:

```bash
make venv
```

If you don't have python virtual environments installed, one way of installing it is:

```bash
sudo apt-get install python3-venv
```

Then to install the required packages, run:

```bash
make update
```

On some systems, this might fail because instead of `pip3`, you are using pip. Please run this command to use `pip` instead of `pip3`.

```bash
make update_with_pip
```

## Running
To run the program, simply:
```bash
make run
```

The output will be located in the *Problem2_Output* directory, with the current timestamp in the filename as a convenience.

## Assumptions and Known Issues
This program leans towards robustness rather than correctness when parsing salaries. For example, if a salary is *$$$3,234,355*, we consider it.
However, we never consider entries that contain an empty value or the commonly seen "no salary data" string.

The salary *No Data - $23,000,000* would be considered as *23,000,000*. This is because if the salary doesn't meet a few of the commonly seen cases, the program strips out just the digits of the salary. This means that numbers with commas that don't make sense, such as *23,0*, would also be considered.

I noticed the years seem to be 2016 and the level is "MLB". I'm assuming that this will never change (see step 5 in "Next Steps to Consider").

## Design Considerations
This is a purely backend program to give the user full control on how they want to process the output.

Output is split into three files:
1. A results.txt file which lists out the qualifying offer and total amount of salaries considered.
2. A top_players.csv file as a convenience. This contains the top 125 players that were considered, sorted by highest to lowest salary.
3. An all_players.csv file, noting the same information as the parsed webpage. There are two new columns added, *Salary Status Code* and *Salary Status Message* to show the user the reason why a player's salary was not considered or could not be parsed.

## Next Steps To Consider
Here's some next steps that I'd like to add:
1. To increase robustness, we could add command line arguments to accept a different threshold (e.g. 150 instead of the top 125 players).
2. Similarly, we could add arguments to try to compute the qualifying offer in various ways (e.g. with or without entries that contain more than one dollar sign).
3. Using a visualization tool such as matplotlib would be a great way to see a histogram of salaries.
4. Building on the previous two steps, we could see if there's any outliers, and add the option to remove them before calculating the qualifying offer.
5. Depending on what we know about where our input comes from, it would be wise to add the option to filter by year (the data seemed to always be 2016 and "MLB").
6. Using a sqlite3 database to store previous results would also seem like a good idea going forward.


## Screenshots
Example of the all_players.csv
![Alt text](/README_IMAGES/all_salaries.png))