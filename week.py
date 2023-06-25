import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta
from main import rowing, csv_data, running, cycling


def show_week(monday, data):
    # change below to monday after 
    start_date = monday
    current_date = start_date
    
    the_week = []  
    for i in range(7):            
        the_week.append(current_date)# change this so not include year   .strftime("%m-%d")
        current_date += timedelta(days=1)


    #activites = traverse_back(data, start_date) 
    all_times = calc_time(start_date, data, the_week)  
    times = [datetime.strptime(time_str, "%H:%M").strftime("%H:%M") for time_str in all_times]
    print(times)
    plt.bar(the_week, times, width = 1, color = "blue") # rowing and other counted here
    
    
    
    
    
    # run_vals = calc_time(start_date, running, the_week)
    # plt.bar(the_week, run_vals, width = 1, color = "red") # showing running
    # cycle_bars = calc_time(start_date, cycling, the_week)       # problem arose here
    # plt.bar(the_week, cycle_bars, width = 1, color = "green") # showing cycling
    # # can add others and make clearer but find demo 
    #others like streching and weights


    plt.xlabel("Date")
    plt.ylabel("activities")
    plt.title("the week of ____")
    plt.show()
    
#datetime(2023,6,6).date()

def calc_time(monday, data, the_week):  # need to change to time right now just activites
    index_of_m = traverse_back(monday, data, len(data)) - 2
    times = ["0:00"]*7 
    
    for i in range(7):
        oldest_act = datetime(int(data[index_of_m][1][:4]), int(data[index_of_m][1][5:7]), int(data[index_of_m][1][8:10])).date() 
        if the_week[i] == oldest_act: 
            times[i] = add_times(times[i], data[index_of_m][4][:-3])
            index_of_m -= 1
            while the_week[i] == datetime(int(data[index_of_m-1][1][:4]), int(data[index_of_m-1][1][5:7]), int(data[index_of_m-1][1][8:10])).date():
                #deals with multiple workouts on the same day
                times[i] = add_times(times[i], data[index_of_m][4][:-3])
                index_of_m -= 1
    return times

def traverse_back(monday, W_data, max_data):
    """find how far back till we reach the date given returns the number, including activites within the start date 
    need to input start_date as datetime() not with .date()"""
    count = 0
    current_date = datetime(int(W_data[0][1][:4]), int(W_data[0][1][5:7]), int(W_data[0][1][8:10])).date()
    lastest_data = datetime.today().date()
    end = monday
    while(current_date >= end):   
        if count >= max_data:
            print("out of bounds")
            break
        current_date = datetime(int(W_data[count][1][:4]), int(W_data[count][1][5:7]), int(W_data[count][1][8:10])).date()
        count+= 1
        
    return(count)

def add_times(time1, time2):
    # Parse the time strings have to be in hour minute format no seconds or . 
    
    format_str = "%H:%M"
    datetime1 = datetime.strptime(time1, format_str)
    datetime2 = datetime.strptime(time2, format_str)

    # Add the datetime objects together
    result = datetime1 + timedelta(hours=datetime2.hour, minutes=datetime2.minute)

    return result.strftime(format_str)


start = datetime(2023,6,12).date()
show_week(start, csv_data[1:])

class week():
    def __init__(self, data):
        self.data = data

    def show_week(self, data):
        print(5)
        
        
        
        
        
    def total_time(self, data):
        #will calc the time for all the data given
        exit(0)
        
    
        
        
    def aerobic_level(self, data):
        # calc value + threshon and what not
         exit(0)
        