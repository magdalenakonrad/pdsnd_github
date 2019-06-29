import time
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

    # ask user to input city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Which city would you like to analyze today New York City, Washington or Chicago?: ').lower()

    cities_list = ['new york city', 'washington', 'chicago']
    while city not in cities_list:
        city = input('Please check your answer and type again one of the cities: New York City, Washington or Chicago: ').lower()

    # ask user to input month (all, january, february, ... , june)
    month = input(
        'Would you like to filter by a month or not at all? Please type a name of a month e.g. January or all for no month filter: ').lower()
    month_numbers = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    while month not in month_numbers:
        month = input('Please check your answer and type again a month name or all for no month filter: ').lower()

    # ask user to input day of a week (all, monday, tuesday, ... sunday)
    day = input(
        'Which day of a week would you like to analyze? Please type e.g. Monday, Tuesday... or all for no day filter: ').title()
    days_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'All']
    while day not in days_list:
        day = input(
            'Please check your answer and type again a day of a week e.g. Monday, Tuesday... or all for no day filter: ').title()

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

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert Start Time into datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month from Start Time and create new column
    df['month'] = df['Start Time'].dt.month

    # extract day of a week from Start Time and create new column
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # create month filter
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

    # create day of a week filter
    if day != 'All':
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month = df['month'].mode()[0]
    print('The most popular month:', popular_month)


    # display the most common day of week
    popular_day_of_week = df['day_of_week'].mode()[0]
    print('The most popular day of a week:', popular_day_of_week)

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_start_hour = df['hour'].mode()[0]
    print('The most popular start hour:', popular_start_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station

    most_commonly_used_start_station = df['Start Station'].mode()[0]
    print('The most commonly used start station:', most_commonly_used_start_station)

    # display most commonly used end station

    most_commonly_used_end_station = df['End Station'].mode()[0]
    print('The most commonly used end station:', most_commonly_used_end_station)


    # display most frequent combination of start station and end station trip

    most_common_combination_Station = (df['Start Station'] + " - " + df['End Station']).mode()[0]
    print('The most common stations\' combination:', most_common_combination_Station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

     # display total travel time

    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time:', total_travel_time)

    # display mean travel time

    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time:', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types

    user_types = df['User Type'].value_counts()
    print('\nCount of user types:\n', user_types)

    # Display counts of gender

    try:
        gender_types = df['Gender'].value_counts()
        print('\nCount of gender:\n', gender_types)
    except KeyError:
        print('Count of gender: No data available within these filters')


    # Display earliest, most recent, and most common year of birth

    try:
        earliest_birth_year = df['Birth Year'].min()
        print('The earliest year of birth:', earliest_birth_year)
    except KeyError:
        print('The earliest year of birth: No data available within these filters')

    try:
        most_recent_birth_year = df['Birth Year'].max()
        print('The most recent year of birth:', most_recent_birth_year)
    except KeyError:
        print('The most recent year of birth: No data available within these filters')

    try:
        most_common_birth_year = df['Birth Year'].mode()[0]
        print('The most common year of birth:', most_common_birth_year)
    except KeyError:
        print('The most common year of birth: No data available within these filters')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    """Displays raw data upon request by a user."""

    raw_data_request = input('Would you like to view first five rows of raw data? Please enter Y or N: ').title()
    if raw_data_request =='Y':
        print(df.head())
    else:
        return

    x = 0
    while raw_data_request == 'Y':
        raw_data_request = input('Would you like to view next five rows of raw data? Please enter Y or N: ').title()
        if raw_data_request == 'Y':
            x += 5
            print(df.iloc[:x + 5])
        else:
            return

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter Y or N.\n')
        if restart.title() != 'Y':
            break


if __name__ == "__main__":
	main()
