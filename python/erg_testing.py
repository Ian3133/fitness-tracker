import sys
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy
import datetime

                #(0 = 48
rowing_times = [1.2, 2.2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# for i, value in enumerate(rowing_times):
#     plt.annotate("1:"+str(48-value), xy=(i, value), xytext=(i, value + 1),
#                  ha='center', va='bottom')

# Generate data for x-axis (time values)
start_time = datetime.datetime.strptime('01:48', '%M:%S')
end_time = datetime.datetime.strptime('01:42', '%M:%S')
delta = datetime.timedelta(seconds=.5)  # Time interval between data points
times = []
current_time = start_time
while current_time != end_time:
    times.append(current_time.strftime('%M:%S'))  # Format time as minute:second
    current_time -= delta 

# Replace this equation with your own
equation_values = [(numpy.log(x+1)*2*7/7.5)  for x in range(12)]
for i, value in enumerate(equation_values):
     plt.annotate("1:"+str(48 - equation_values[i])[:4], xy=(i, value), xytext=(i, value + 1),
                   va='bottom')

test_days = []
next_week= datetime.datetime(2023, 6, 6)
week = datetime.timedelta(days=7)
for i in range(12):
    test_days.append((next_week.strftime("%m-%d")))
    next_week += week

#print (test_days)

# Create the line graph
plt.plot(test_days, times, ' ')
plt.plot(equation_values, label='Goal')
x = [x for x in range(12)]
plt.fill_between(x, equation_values, color="#ffcccb")
plt.bar(x, rowing_times)
#plt.bar(test_days, , align="edge")
plt.ylabel('Splits')
plt.title('20min Erg, rate:24, HR ~ 185')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)

# Display the graph
plt.tight_layout()
plt.savefig("fitness-tracker/images/erg.jpg")
plt.show()


# add a on track and "not on track" as a you need to be ___ speed next week. 
#also connect HR