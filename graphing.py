import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta
from main import rowing, csv_data, running, cycling, data, weights
import numpy as np
from week import calc_time_and_hr, to_min







def plot_summer():
    summer_starts = datetime(2023, 6, 5).date()
    current_date = summer_starts
    summer = []
    for i in range(90):            
        summer.append(current_date)
        current_date += timedelta(days=1)
 
    all_times, all_hr = calc_time_and_hr(summer_starts, data, summer)         
    run_val, run_hr= calc_time_and_hr(summer_starts, running, summer)
    cycling_val, cycling_hr =  calc_time_and_hr(summer_starts, cycling, summer)
    #weights_val, extra = calc_time_and_hr(summer_starts, weights, summer)
    #other_val, extra = calc_time_and_hr(start_date, other, self.the_week)            
    #strech_val, extra = calc_time_and_hr(start_date, streching, self.the_week)
    
    #print(strech_val)
    
    all_times_min, run_min, cycling_min = to_min(all_times), to_min(run_val), to_min(cycling_val)
    #weights_min = to_min(weights_val) # self.other_min = to_min(other_val)
    #print(self.weights_min)
    #self.strech_min =  to_min(strech_val)    # maybe double check this so not every day and actlly add to total times or change in data 
    times_graph_format = []
    for i in range(90):
        times_graph_format.append(str(summer[i])[5:])
    #creates pi chart
    create_pie(all_hr,all_times_min)
    
    plt.yticks(np.arange(0, max(all_times_min), 20))
    plt.grid(True, which='major', axis='y', linestyle='-', linewidth=.5)
    #plt.bar(times_graph_format, times_graph_format)
    plt.bar(times_graph_format, all_times_min, zorder= 2, color = "blue", label="Rowing", width=.75)
    plt.bar(times_graph_format, run_min, zorder= 2, color = "red", label="Running", width=.75) 
    plt.bar(times_graph_format,cycling_min, zorder= 2, color = "green", label="Cycling", width=.75)
   # plt.bar(times_graph_format,weights_min, zorder= 2, color = "purple", label="Weights")
    #plt.bar(times_graph_format, self.other_min, zorder= 2, color = "yellow", label="Other Exersize")
        #print(type(self.strech_min[2]))
        #print(type(self.all_times_min[2]))
        #plt.bar(times_graph_format, self.strech_min, zorder= 2, color = "orange", label="Streching")
    
    plt.legend()
    plt.xticks(range(0, 90, 7), rotation=45)
    plt.xlabel("Date")
    plt.ylabel("Minutes")
    plt.title("Summer 2023")
    plt.savefig("images/summer.jpg")
    plt.show()

    
def aerobic_num(hr, all_times):
    value = 0
    times = [num for num in all_times if num != 0]
    for i in range(len(times)):
        activity = hr[i]
        if activity > 175:
            value += times[i] * .03
        elif activity > 166:
            value +=  times[i] * .06 
        elif activity > 155:
            value += times[i] * .1
        elif activity > 147:
            value += times[i] * .07
        else:
            value += times[i] * .02
    return value
        
def threshold_num(hr, all_times):           # need to check the multiplying factor 
    value = 0
    times = [num for num in all_times if num != 0]
    for i in range(len(times)):
        activity = hr[i]
        if activity > 190:
            value += times[i] * .4
        elif activity > 175:
            value +=  times[i] * .5
        elif activity > 165:
            value += times[i] * .1
        else:
            value += 0
    return value

def vo2_max_num(hr, all_times):
    value = 0
    times = [num for num in all_times if num != 0]
    for i in range(len(times)):
        activity = hr[i]
        if activity > 190:
            value += times[i] * .9
        elif activity > 185:
            value +=  times[i] * .4
        elif activity > 165:
            value +=  times[i] * .005
        else:
            value += 0
    return value

def create_pie(hr, all_times):
    values = [aerobic_num(hr, all_times), threshold_num(hr, all_times), vo2_max_num(hr, all_times)] 
    labels = ["Aerobic", "Lactic Threshold", "VO2 Max"]
    colors = ['green', 'purple', 'red']

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, colors=colors)
    
    # Set the background color of the figure
    fig.patch.set_facecolor('#f2f2f2')
    
    plt.title("Cumulative Training")
    plt.savefig("images/pi_summer.jpg") 
    plt.show()


plot_summer()






















# def show_all_activites(all_data, days_back):
    
#     today = datetime.now().date()
#     start_date = today - timedelta(days=days_back)  
#     current_date = start_date
    
#     all_days = []  
#     while current_date <= today:            
#         all_days.append(current_date)# change this so not include year   .strftime("%m-%d")
#         current_date += timedelta(days=1)

#     #activites = traverse_back(data, start_date) 
#     all_values = calc_values(all_data, all_days, days_back, start_date)
#     plt.bar(all_days, all_values, width = 1, color = "blue") # rowing and other counted here
#     run_vals = calc_values(running, all_days, days_back,start_date)
#     plt.bar(all_days, run_vals, width = 1, color = "red") # showing running
#     cycle_bars = calc_values(cycling, all_days, days_back,start_date)       # problem arose here
#     plt.bar(all_days, cycle_bars, width = 1, color = "green") # showing cycling
#     # can add others and make clearer but find demo 
#     #others like streching and weights


#     plt.xlabel("Date")
#     plt.ylabel("activities")
#     plt.title("All Training")
#     plt.show()


# def calc_values(data, all_days, days_back, start_date):
#     activites = traverse_back(data, start_date)
#     values = [0]*len(all_days)
#     count = activites     -2 
#     for i in range(days_back):
#         oldest_act = datetime(int(data[count][1][:4]), int(data[count][1][5:7]), int(data[count][1][8:10])).date() 
#         if all_days[i] == oldest_act: 
#             values[i] += 1
#             count -= 1
#             while all_days[i] == datetime(int(data[count-1][1][:4]), int(data[count-1][1][5:7]), int(data[count-1][1][8:10])).date():
#                 values[i] += 1
#                 count -= 1
#     return values

# def traverse_back(data, start_date):
#     """find how far back till we reach the date given returns the number, including activites within the start date 
#     need to input start_date as datetime() not with .date()"""
#     count = 0
#     date = datetime(int(data[0][1][:4]), int(data[0][1][5:7]), int(data[0][1][8:10])).date()
#     today = datetime.today()
#     while(date >= start_date):
#         if count >= len(data):
#             print("out of bounds")
#             break
#         else:
#             date = datetime(int(data[count][1][:4]), int(data[count][1][5:7]), int(data[count][1][8:10])).date()
#             count+= 1
#     return(count)

# show_all_activites(csv_data[1:], 3)

