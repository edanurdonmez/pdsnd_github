import time
import statistics
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Please enter one of the cities chicago, new york city or washington which you want to learn more about: ')
    while True:
     if city not in ['chicago', 'new york city', 'washington']:
        city = input ('Sorry, this city you entered is not among the options. Please choose between cities of chicago, new york city or washington: ').lower()
        continue
     else:
        break

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('Please enter one of the month which you want to filter between january, february, march, april, may, june or write "all" if you want to see all of months: ')
    monthArray = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    while True:
     if month not in monthArray:
        month = input ('Sorry, this month you entered is not among the options. Please choose between months of january, february, march, april, may, june or write "all" if you want to see all of them: ').lower()
        continue
     else:
        break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Please enter one of the day which you want to filter it or write "all" if you want to see all of days: ')
    dayArray = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
    while True:
     if day not in dayArray:
        day = input ('Sorry, this day you entered is not among the options. Please choose between days of monday, tuesday, wednesday, thursday, friday, saturday, sunday or write "all" if you want to see all of them: ').lower()
        continue
     else:
        break

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filterpython bikeshare.py
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'], format='%Y%m%d %H:%M:%S')

    # extract month and day of week from Start Time to create new columns
    df['month_name'] = df['Start Time'].dt.month
    df['dayofweek'] = df['Start Time'].dt.weekday_name
  
   # filter by month if applicable
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    if months.__contains__(month):
        # use the index of the months list to get the correspondingint
        for index in range(0,6):
            if month == months[index]:
               month = index + 1
        # filter by month to create the new dataframe
        df = df[df['month_name'] == month]
        
    # filter by day of week if applicable
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    if days.__contains__(day):
        # filter by day of week to create the new dataframe
        df = df[df['dayofweek'] == day.title()]

    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = statistics.mode(df['month_name'])
    print('Most Common Month:', most_common_month)

    # TO DO: display the most common day of week
    most_common_day = statistics.mode(df['dayofweek'])
    print('Most Common Day:', most_common_day)

    # TO DO: display the most common start hour
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    most_common_hour = statistics.mode(df['hour'])
    print('Most Common Start Hour:', most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    Start_Station = df['Start Station'].mode()
    print('Most Commonly used Start Station:', Start_Station)


    # TO DO: display most commonly used end station
    End_Station = df['End Station'].mode()
    print('Most Commonly used End Station:', End_Station)

    # TO DO: display most frequent combination of start station and end station trip 
    Combination_Station = df.groupby(['Start Station','End Station']).size().nlargest(1)
    print('\nMost frequent combination of start station and end station trip: ', Start_Station, " & ", End_Station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
 

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    Total_Travel_Time = sum(df['Trip Duration'])
    print('Total Travel Time:', Total_Travel_Time/60, " Minutes")

    # TO DO: display mean travel time
    Mean_Travel_Time = df['Trip Duration'].mean()
    print('Mean Travel Time:', Mean_Travel_Time/60, " Minutes")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    User_Type = df['User Type'].value_counts()
    print('Counts of each user type\n', User_Type)
    
    # TO DO: Display counts of gender
    # TO DO: Display earliest, most recent, and most common year of birth
    # NOTE: adding 
    try:
        User_Gender = df['Gender'].value_counts()
        print('Counts of each gender type\n', User_Gender)
        Earliest_Year = df['Birth Year'].min()
        print('\nEarliest Year of Birth:', Earliest_Year)
        Most_Recent_Year = df['Birth Year'].max()
        print('\nMost Recent Year of Birth:', Most_Recent_Year)
        Most_Common_Year = df['Birth Year'].value_counts().idxmax()
        print('\nMost Common Year of Birth:', Most_Common_Year)
    except KeyError:
        pass
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    """Displays data for first 5 rows"""
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    start_loc = 0
    while (view_data == 'yes'):
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_data = input("Do you wish to continue?: ").lower()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
