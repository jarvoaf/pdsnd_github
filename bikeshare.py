import time
import pandas as pd

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
    city = input("Which city would you like to look at?\nPlease type Chicago, New York City or Washington: ")
    city = city.lower()
    while city not in ["chicago", "new york city", "washington"]:
        print("That was not a valid city, please try again.")
        city = input("Which city would you like to look at?\nPlease type Chicago, New York City or Washington: ")
        

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Which month would you like to look at?\nPlease type January, February.....June, or All: ")
    month = month.lower()
    while month not in ["january", "february", "march", "april", "may", "june", "all"]:
        print("That was not a valid choice, please try again")
        month = input("Which month would you like to look at?\nPlease type January, February.....June, or All: ")
        

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Which day would you like to look at?\nPlease type Monday, Tuesday.....Sunday, or All: ")
    day = day.lower()
    while day not in ["all", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]:
        print("That was not a valid choice, please try again.")
    

    print('-'*60)
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
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # extract month and day of week from Start Time to create new columns
    # see README.txt Notes 1 and 2
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        # see README Note 3
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    # see README.txt Note 4
    most_common_month = df['month'].mode()[0]
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    most_common_month_name = months[most_common_month - 1]
    print(f"The most common month is {most_common_month_name}.")

    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print(f"The most common day of the week is {most_common_day}.")
    
    # TO DO: display the most common start hour
    # see README.txt Note 5
    most_common_start_hour = df["Start Time"].dt.hour.mode()[0]
    print(f"The most common start hour is {most_common_start_hour}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*60)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df["Start Station"].mode()[0]
    print(f"The commonly used starting station is {most_common_start_station}")
    
    # TO DO: display most commonly used end station
    most_common_end_station = df["End Station"].mode()[0]
    print(f"The commonly used ending station is {most_common_end_station}")
    
    # TO DO: display most frequent combination of start station and end station trip
    # see README.txt Note 6
    most_common_start_end_station = (df["Start Station"] + " to " + df["End Station"]).mode()[0]
    print(f"The most frequent combination of starting and ending stations is {most_common_start_end_station}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*60)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df["Trip Duration"].sum()
    print(f"Total travel time is {round(total_travel_time/86400, 2)} days")

    # TO DO: display mean travel time hours
    mean_travel_time = df["Trip Duration"].mean()
    print(f"Mean travel time is {round(mean_travel_time/60)} minutes")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*60)
    
def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_of_user_types = df["User Type"].value_counts()
    print(f"Counts of the user types are:\n{count_of_user_types}")

    # TO DO: Display counts of gender
    # see README.txt Note 7
    if city == "washington":
        print("\nGender is not captured for Washington")
    else:    
        count_of_gender = df["Gender"].value_counts()
        print(f"\nCounts of gender are:\n{count_of_gender}")

    # TO DO: Display earliest, most recent, and most common year of birth    
    if city == "washington":
        print("\nBirt Year is not captured for Washington")
    else:
        earliest_birth_year = int(df["Birth Year"].min())                       # Birth Year is float in source,  
        most_recent_birth_year = int(df["Birth Year"].max())                    # convert to integer so results look  
        most_common_birth_year = int(df["Birth Year"].mode()[0])                # the same as a year should display
        print(f"\nThe earliest year of birth is {earliest_birth_year}")       
        print(f"\nThe most recent year of birth is {most_recent_birth_year}")
        print(f"\nThe most common year of birth is {most_common_birth_year}")        

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*60)
    
def raw_data (df):
    """Displays the filtererd data 5 rows
    at a time each time enter is pressed"""
    print('Press enter to see row data, type no to skip')
    x = 0
    while (input() != 'no'):
        x += 5
        print(df.head(x))
        
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
    