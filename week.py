import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
from datetime import datetime, timedelta
from main import rowing, csv_data, running, cycling, other
data = csv_data[1:]

class week():
    def __init__(self, monday):
        self.monday = monday
        self.all_times = []

    def show_week(self):
        start_date = self.monday
        current_date = start_date
        #creates an array of the week with dates
        the_week = []  
        for i in range(7):            
            the_week.append(current_date)
            current_date += timedelta(days=1)

        self.all_times = calc_time(start_date, data, the_week)          # the data is self but the rest aren't you can change that
        run_val = calc_time(start_date, running, the_week)
        cycling_val =  calc_time(start_date, cycling, the_week)
        #other_val = calc_time(start_date, other, the_week)             # need to add other as well as streching maybe auto do so it adds 10 mins if ever recored
        all_times_min, run_min, cycling_min = to_min(self.all_times), to_min(run_val), to_min(cycling_val)
        
        times_graph_format = []
        for i in range(7):
            times_graph_format.append(str(the_week[i])[5:])
    
        plt.yticks(np.arange(0, max(all_times_min), 20))
        plt.grid(True, which='major', axis='y', linestyle='-', linewidth=.5)
        plt.bar(times_graph_format, all_times_min, zorder= 2, color = "blue", label="Rowing")
        plt.bar(times_graph_format, run_min, zorder= 2, color = "red", label="Running") 
        plt.bar(times_graph_format, cycling_min, zorder= 2, color = "green", label="Cycling")
        # add streching and other and probly weights
        plt.legend()
        plt.xlabel("Date")
        plt.ylabel("Minutes")
        plt.title("The Week of " + str(times_graph_format[0]))
        plt.show()
        
    def total_time(self):
        # have to be called after the graph shoud more some of show graph into init function
        sum = '0:00'
        for i in range(7):
            sum = add_times(sum, self.all_times[i])
        return sum
    
    def aerobic_num(self):
        return
    def threshold_num(self):
        return
    def vo2_max_num(self):
        return
    
    def pi_chart(self):
        return
       
        

def to_min(times):
    return ([int(time.split(':')[0])*60 + int(time.split(':')[1]) for time in times])

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


        
# monday_1 = datetime(2023, 6, 5).date()
# week_1 = week(monday_1)
# week_1.show_week()
monday_2 = datetime(2023, 6, 12).date()
week_2 = week(monday_2)
week_2.show_week()
print(week_2.total_time())
# monday_3 = datetime(2023, 6, 19).date()
# week_3 = week(monday_3)
# week_3.show_week()
