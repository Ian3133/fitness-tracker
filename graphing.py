import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta
from main import rowing, csv_data, running, cycling


def show_all_activites(all_data, days_back):
    today = datetime.now().date()
    start_date = today - timedelta(days=days_back)  
    current_date = start_date
    
    all_days = []  
    while current_date <= today:            
        all_days.append(current_date)# change this so not include year   .strftime("%m-%d")
        current_date += timedelta(days=1)

    #activites = traverse_back(data, start_date) 
    all_values = calc_values(all_data, all_days, days_back, start_date)
    plt.bar(all_days, all_values, width = 1, color = "blue") # rowing and other counted here
    run_vals = calc_values(running, all_days, days_back,start_date)
    plt.bar(all_days, run_vals, width = 1, color = "red") # showing running
    cycle_bars = calc_values(cycling, all_days, days_back,start_date)
    plt.bar(all_days, cycle_bars, width = 1, color = "green") # showing cycling
    # can add others and make clearer but find demo 
    #others like streching and weights


    plt.xlabel("Date")
    plt.ylabel("activities")
    plt.title("All Training")
    plt.show()

def calc_values(data, all_days, days_back, start_date):
    activites = traverse_back(data, start_date)
    values = [0]*len(all_days)
    count = activites     -2 
    for i in range(days_back):
        oldest_act = datetime(int(data[count][1][:4]), int(data[count][1][5:7]), int(data[count][1][8:10])).date() 
        if all_days[i] == oldest_act: 
            values[i] += 1
            count -= 1
            while all_days[i] == datetime(int(data[count-1][1][:4]), int(data[count-1][1][5:7]), int(data[count-1][1][8:10])).date():
                values[i] += 1
                count -= 1
    return values

def traverse_back(data, start_date):
    """find how far back till we reach the date given returns the number, including activites within the start date 
    need to input start_date as datetime() not with .date()"""
    count = 0
    date = datetime(int(data[0][1][:4]), int(data[0][1][5:7]), int(data[0][1][8:10])).date()
    today = datetime.today()
    while(date >= start_date):
        if count >= len(data):
            print("out of bounds")
            break
        else:
            date = datetime(int(data[count][1][:4]), int(data[count][1][5:7]), int(data[count][1][8:10])).date()
            count+= 1
    return(count)

show_all_activites(csv_data[1:], 15)

