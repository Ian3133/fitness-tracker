import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta
from main import rowing, csv_data






today = datetime.now().date()
start_date = today - timedelta(days=10)  
current_date = start_date
    
all_days = []
while current_date <= today:              # creates a list of all the dates back
    all_days.append(current_date)# change this so not include year
    current_date += timedelta(days=1)
    
data = rowing


values = [0]*10
count = 3 # ned to change later
for i in range(10):
    latest_row = datetime(int(data[count][1][:4]), int(data[count][1][5:7]), int(data[count][1][8:10])).date()
    #print(latest_row)
    #print(all_days[i])
    if all_days[i] == latest_row: # need to make this a loop for multiple activies on the same day
        values[i] += 1
        count -= 1
print(values)
    
        

