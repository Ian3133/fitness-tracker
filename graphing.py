
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta
from main import rowing, csv_data

#print(csv_data[0])
#print(str(datetime.now().date())
#print(csv_data[1][1])
#print(datetime(2023,1,4))
#print(rowing[0][1][8:10])
#conv = datetime(int(rowing[0][1][:4]), int(rowing[0][1][5:7]), int(rowing[0][1][8:10]))
#print(datetime.today() < conv)


def show_all_activites(data, days_back):
    today = datetime.now().date()
    start_date = today - timedelta(days=days_back)  
    current_date = start_date
    
    all_days = []  
    while current_date <= today:              # creates a list of all the dates back
        all_days.append(current_date)# change this so not include year
        current_date += timedelta(days=1)
    #print(start_date, "this one")
    plt.bar(all_days, [0]*len(all_days), align="center")
    #print(all_days)
   # activites = traverse_back(data, start_date) # amount of workouts in time fram
    #print(all_days)
       
    values = [0]*len(all_days)
    count = 3
    for i in range(days_back):
        oldest_act = datetime(int(data[count][1][:4]), int(data[count][1][5:7]), int(data[count][1][8:10])).date() 
        if all_days[i] == oldest_act: # need to make this a loop for multiple activies on the same day
            values[i] += 1
            count -= 1
    print(values)
    
        
    plt.bar(all_days, values, align="center")
    plt.xlabel("x-label")
    plt.ylabel("y-label")
    plt.title("title here")
    plt.show()


def traverse_back(data, start_date):
    """find how far back till we reach the date given returns the number, including activites within the start date """
    count = 0
    date = datetime(int(data[0][1][:4]), int(data[0][1][5:7]), int(data[0][1][8:10])).date()
    today = datetime.today()
    while(date >= start_date):
        if count >= len(data):
            print("out of bounds")
            break
        else:
            date = datetime(int(data[count][1][:4]), int(data[count][1][5:7]), int(data[count][1][8:10]))
            count+= 1
    return(count)
#example call for above
#ex_val = datetime(2023, 6, 12)
#print(traverse_back(rowing, ex_val))




show_all_activites(rowing, 21)


'''
#plt.plot(rowing[1],rowing[4])
# Add labels and title
##plt.xlabel('X-axis')
#plt.ylabel('Y-axis')
#plt.title('Rows')
# Display the graph
#plt.show()
#plt.savefig('plot.png') for turning into a png where a website 


dates = [
    datetime(2023, 1, 1),
    datetime(2023, 2, 1),
    datetime(2023, 3, 1),
    datetime(2023, 4, 1),
    datetime(2023, 5, 1)
]

values = [5, 10, 8, 12, 6]

# Convert dates to matplotlib format
dates_num = mdates.date2num(dates)

# Create scatter plot
plt.scatter(dates_num, values)

# Format x-axis as dates
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))

# Rotate x-axis labels for better visibility
#plt.xticks(rotation=45)

# Add labels and title
plt.xlabel('Date')
plt.ylabel('Value')
plt.title('Scatter Plot')

# Display the plot
plt.show()


'''