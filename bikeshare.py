#!/usr/bin/env python
# coding: utf-8

# In[3]:


import time
import pandas as pd
import numpy as np
from pandas import Timestamp as ts
filename= 'data1/new_york_city.csv'
file=pd.read_csv(filename)
file2=pd.read_csv('data1/chicago.csv')
file3=pd.read_csv('data1/washington.csv')
city_d = { 'chicago': file2,
              'new york': file,
              'washington': file3 }
def filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    months_list = ['index zero','jan', 'feb', 'march', 'april', 'may', 'june','all']
    days_list=['sat','sun','mon','tue','wed','thu','fri','all']
    print('Hi! Let\'s get you to know about some of the bikeshare data in the united states')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city=input('please tell me the city that you want to know about \n choose from chicago,new york city or washington')
        city=city.lower()
        if city == 'chicago' or city =='new york' or city =='washington':
            break
        print('\ninvalid input please choose from chicago,new york city or washington')
   
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
            month=input('please tell me a month that you want to know about \n choose from jan,feb,april,may,june or just choose "all" of them if you do not want time analysis or to filter by month')
            month=month.lower()
            if month in months_list:
                break
            print('\ninvalid input please choose from jan,feb,april,may,june')    
               


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day=input('please tell me a day that you want to know about \n choose from sat,sun,mon,tue,wed,thu,fri or just choose "all" of them if you do not want time analysis or to filter by day')
        day=day.lower()
        if day in days_list:
            break
        print('\ninvalid input please choose from sat,sun,mon,tue,wed,thu,fri')
    
    
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    
    
    months = {'jan':1, 'feb':2,'march':3,'april':4,'may':5,'june':6}
    days={'sat':0,'sun':1,'mon':2,'tue':3,'wed':4,'thu':5,'fri':6}
    df=pd.DataFrame(city_d[city])
    
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.dayofweek
    df['hour']=df['Start Time'].dt.hour
    if day != 'all':
              
            df=df[df['day_of_week']==days[day]]
    if month != 'all':
        df=df[df['month']==months[month]]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    months_list = ['index zero','january', 'february', 'march', 'april', 'may', 'june']
    print('the most common month is',months_list[df['month'].mode()[0]],'\ntheir count is :',df['month'].value_counts().max())
    


    # TO DO: display the most common day of week
    days_list=['sat','sun','mon','tue','wed','thu','fri']

    print('\nthe most common day is ',days_list[df['day_of_week'].mode()[0]],'\ntheir count is :',df['day_of_week'].value_counts().max())


    # TO DO: display the most common start hour
    
    print('\nthe most common start hour is',df['hour'].mode()[0],'\ntheir count is :',df['hour'].value_counts().max())
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('the most commonly used start station is :',df['Start Station'].mode()[0],'\nit has been used for ',df['Start Station'].value_counts().max(),' times')
    
    # TO DO: display most commonly used end station
    print('the most commonly used end station is :',df['End Station'].mode()[0],'\nit has been used for ',df['End Station'].value_counts().max(),' times')
    
    


    # TO DO: display most frequent combination of start station and end station trip
    df['combination_stations']='starts at '+df['Start Station']+'and ends at '+df['End Station']
    print('the most frequent combination used ',df['combination_stations'].mode()[0],'\nAnd it has been used for'
    ,df['combination_stations'].value_counts().max(),' times')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('total travel time is :',df['Trip Duration'].sum(),'seconds\n')


    # TO DO: display mean travel time
    print('Average travel time is :',df['Trip Duration'].mean(),'seconds\n')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('the count of each user type is \n',df['User Type'].value_counts())


    # TO DO: Display counts of gender
    if city=='chicago' or city=='new york':
        print('the count of each gender is \n',df['Gender'].value_counts())
        print('the earliest birth year is :',df['Birth Year'].min())
        print('\nthe most recent birth year is :',df['Birth Year'].max())
        print('\nthe most common birth year is :',df['Birth Year'].mode()[0],'\nits count is :',df['Birth Year'].value_counts().max())
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        i=5
        while i < len(df):
            choice=input('do you want to see some raw data? yes or no')
            choice=choice.lower()
            if choice == 'no':
                break   
            print(df[:i+1])        
              
              
        
        print('no more raw data :)')
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()


# In[ ]:





# In[ ]:





# In[ ]:




