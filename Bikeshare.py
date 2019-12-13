washington# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 11:47:38 2019

@author: jay
"""

import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

CITIES = ['chicago', 'washington','new york city']

DAYS = ['all', 'monday', 'tuesday','wednesday', 'thursday', 'friday', 'saturday', 'sunday']

MONTHS = ['all', 'january', 'febuary', 'march', 'april', 'may', 'june']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello Friend! Join me and Let\'s explore some data on US bikeshare!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('which city do you want us to start with New York City, Chicago or Washington? \n>').lower()
        if city in CITIES:
            break

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input('Now select a month to explore. \n Bikeshare data is available form January to June.\n> ')
        if month in MONTHS:
            break

        # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Lastly, type any day of the week you want to explore. \n(e.g. all, monday, tuesday, friday) \n> ')
        if day in DAYS:
            break

    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    #load data file from DataFrame
    df = pd.read_csv(CITY_DATA[city])

    #convert the Start Time into datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    #extract month and day of week and hour from Start Time to creat new column
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    #if applicable, filter by month
    if month != 'all':
        month = MONTHS.index(month) + 1
        df = df[df['month'] == month]

    #filter by day of the week
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()


    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    Most_common_month = df['month'].value_counts().idxmax()
    print("The most common month is :", Most_common_month)


    # display the most common day of week
    Most_common_day_of_week = df['day_of_week'].value_counts().mode()
    print("The most common day of the week is :", Most_common_day_of_week)


    # display the most common start hour
    most_common_start_hour = df['hour'].value_counts().idxmax()
    print("The most common start hour is :", most_common_start_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_start_station = df['Start Station'].value_counts().idxmax()
    print("The most commonly used start station :", most_common_start_station)

    # display most commonly used end station
    most_common_end_station = df['End Station'].value_counts().idxmax()
    print("The most commonly used end station :", most_common_end_station)

    # display most frequent combination of start station and end station trip
    most_common_start_end_station = df[['Start Station', 'End Station']].mode().loc[0]
    print("The most frequently used start station and end station : {}, {}"\
            .format(most_common_start_end_station[0], most_common_start_end_station[1]))



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    if 'Gender' in df.columns:
        # Display counts of gender
        gender = df['Gender'].value_counts()
        print(gender)

    if 'Birth Year' in df.columns:
        # Display earliest, most recent, and most common year of birth
        print('Earliest year of Birth:', df['Birth Year'].min())
        print('Most Recent year of Birth:', df['Birth Year'].max())
        print('Most Common year of Birth:', df['Birth Year'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        yes = input('\nWould you like to restart and explore further? Type \'yes\' or \'no\'\n> ')
        if yes.lower() != 'yes':
            break




if __name__ == "__main__":
	main()
