import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
from datetime import datetime, timedelta
from main import data, streching, running, cycling, weights, rowing, other
#print(streching)
from graphing import calc_time_and_hr, add_times, to_min, traverse_back
class week():
    def __init__(self, monday):
        self.monday = monday
        self.the_week = []
        self.start_up()
        
    def start_up(self):
        start_date = self.monday
        current_date = start_date
        for i in range(7):            
            self.the_week.append(current_date)
            current_date += timedelta(days=1)

        self.all_times, self.all_hr = calc_time_and_hr(start_date, data, self.the_week)         
        run_val, run_hr= calc_time_and_hr(start_date, running, self.the_week)
        cycling_val, cycling_hr =  calc_time_and_hr(start_date, cycling, self.the_week)
        weights_val, extra = calc_time_and_hr(start_date, weights, self.the_week)
        #other_val, extra = calc_time_and_hr(start_date, other, self.the_week)            
        #strech_val, extra = calc_time_and_hr(start_date, streching, self.the_week)
        
        #print(strech_val)
        
        self.all_times_min, self.run_min, self.cycling_min = to_min(self.all_times), to_min(run_val), to_min(cycling_val)
        self.weights_min = to_min(weights_val) # self.other_min = to_min(other_val)
        print(self.weights_min)
        #self.strech_min =  to_min(strech_val)    # maybe double check this so not every day and actlly add to total times or change in data 
        
        
        
    def show_week(self):
              
        times_graph_format = []
        for i in range(7):
            times_graph_format.append(str(self.the_week[i])[5:])
    
        plt.yticks(np.arange(0, max(self.all_times_min), 20))
        plt.grid(True, which='major', axis='y', linestyle='-', linewidth=.5)
        plt.bar(times_graph_format, self.all_times_min, zorder= 2, color = "blue", label="Rowing")
        plt.bar(times_graph_format, self.run_min, zorder= 2, color = "red", label="Running") 
        plt.bar(times_graph_format, self.cycling_min, zorder= 2, color = "green", label="Cycling")
        plt.bar(times_graph_format, self.weights_min, zorder= 2, color = "purple", label="Weights")
        #plt.bar(times_graph_format, self.other_min, zorder= 2, color = "yellow", label="Other Exersize")
        #print(type(self.strech_min[2]))
        #print(type(self.all_times_min[2]))
        #plt.bar(times_graph_format, self.strech_min, zorder= 2, color = "orange", label="Streching")
        
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
        value = 0
        times = [num for num in self.all_times_min if num != 0]
        for i in range(len(self.all_hr)):
            activity = self.all_hr[i]
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
            
    def threshold_num(self):           # need to check the multiplying factor 
        value = 0
        times = [num for num in self.all_times_min if num != 0]
        for i in range(len(self.all_hr)):
            activity = self.all_hr[i]
            if activity > 190:
                value += times[i] * .4
            elif activity > 175:
                value +=  times[i] * .5
            elif activity > 165:
                value += times[i] * .1
            else:
                value += 0
        return value
    
    def vo2_max_num(self):
        value = 0
        times = [num for num in self.all_times_min if num != 0]
        for i in range(len(self.all_hr)):
            activity = self.all_hr[i]
            if activity > 190:
                value += times[i] * .9
            elif activity > 185:
                value +=  times[i] * .4
            elif activity > 165:
                value +=  times[i] * .005
            else:
                value += 0
        return value
    
    def pi_chart(self):
        values = [self.aerobic_num(), self.threshold_num(), self.vo2_max_num()] 
        labels = ["Aerobic Training", "Lactic Threshold Training", "VO2 Max Training"]
        colors = ['green', "purple", "red"]

        plt.pie(values, labels=labels, colors=colors)
        plt.legend()
        plt.xticks(rotation=45)
        plt.show()
   
#print(data[0])
#print(add_times(data[14][4][:-3], data[15][4][:-3]))
        
# monday_1 = datetime(2023, 6, 12).date()
# week_1 = week(monday_1)
# week_1.show_week()


# monday_2 = datetime(2023, 6, 23).date()
# week_2 = week(monday_2)
# print(week_2.total_time())
# week_2.show_week()
#print(week_2.total_time())
#print(week_2.aerobic_num(), week_2.threshold_num(), week_2.vo2_max_num())
#week_2.pi_chart()
#monday_3 = datetime(2023, 6, 19).date()
#week_3 = week(monday_3)
#week_3.show_week()

