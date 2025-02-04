# US Bikeshare Data Analysis Project

## Overview
This Python project analyzes bike share system data for three major US cities: Chicago, New York City, and Washington. The interactive program allows users to explore bike sharing patterns and statistics by filtering data by city, month, and day of the week.

### Date Created
Tuesday July 11, 2022

### Features
- Filter bike share data by:
  - City (Chicago, New York City, Washington)
  - Month (January through June)
  - Day of the week
- View statistics about:
  - Most popular times for travel
  - Most frequently used stations
  - Trip durations
  - User demographics
- Option to view raw data in 5-row increments

### Files Used
- `bikeshare.py` - Main Python script containing the analysis code
- `chicago.csv` - Bike share data for Chicago
- `new_york_city.csv` - Bike share data for New York City
- `washington.csv` - Bike share data for Washington
- `README.md` - Project documentation

### Dependencies
- Python 3
- pandas
- numpy
- time
- statistics

### How to Run
1. Ensure all dependencies are installed
2. Place the CSV data files in the same directory as the script
3. Run `python bikeshare.py`
4. Follow the interactive prompts to analyze the data

### Program Features
The script provides the following statistics:
- Popular times of travel (most common month, day of week, hour of day)
- Popular stations and trip routes
- Trip duration statistics (total travel time, average travel time)
- User information (subscriber types, gender breakdown*, age statistics*)

*Note: Gender and age statistics are only available for Chicago and New York City

### Project Structure
- Master Branch: Contains the main project code
- Documentation Branch: Contains project documentation updates

### Credits
This project was created as part of the Udacity Programming for Data Science Nanodegree Program.
Inspired by udacity/pdsnd_github.
