import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy
from main import running
from datetime import datetime, timedelta

def plot_time(time_str):
    # Define the starting time as 11:30
    start_time_str = "11:30"
    start_time = datetime.strptime(start_time_str, "%M:%S")

    # Convert the given time string to a timedelta object
    if len(time_str) == 4:
        time_delta = timedelta(minutes=int(time_str[:1]), seconds=int(time_str[2:]))
    else: 
        time_delta = timedelta(minutes=int(time_str[:2]), seconds=int(time_str[3:]))

    # Subtract the time delta from the starting time
    result_time = start_time - time_delta

    # Calculate the result in seconds
    result_seconds =  (result_time.minute * 60) + result_time.second

    return result_seconds /30 - 1
def plot_runs():
    plt.figure()
    running_splits = []
    runs_x = []
    var = 1/(len(running))
    i = 0 
    var_i = var
    for row in running:
        running_splits.append(plot_time(running[i][8]))
        i += 1
        runs_x.append(var_i)
        var_i += var
    running_splits = running_splits[::-1] 
        
    # Generate data for x-axis (time values)
    start_time = datetime.strptime('11:00', '%M:%S')
    end_time = datetime.strptime('08:00', '%M:%S')
    delta = timedelta(seconds=30)  # Time interval between data points
    times = []
    current_time = start_time
    while current_time != end_time:
        times.append(current_time.strftime('%M:%S'))  # Format time as minute:second
        current_time -= delta 


    x = [1/(x+1) for x in range(len(times))]
    x = x[::-1]
    plt.plot(x, times, " ")


    plt.scatter(runs_x, running_splits, zorder=2, color="red", s = 100)

    plt.ylabel('Splits')
    plt.title('Running Splits, each run')
    plt.xticks([])
    plt.xlabel("Runs")
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)

    # Display the graph
    plt.tight_layout()
    plt.savefig("fitness-tracker/images/running.jpg")