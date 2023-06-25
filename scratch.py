import matplotlib.pyplot as plt
from datetime import datetime

date_data = ['2023-01-01', '2023-02-15', '2023-03-10', '2023-04-22', '2023-05-07']
y_values = [5, 10, 8, 12, 9]

# Convert date strings to datetime objects
datetime_objects = [datetime.strptime(date, '%Y-%m-%d') for date in date_data]

# Format the datetime objects to show only month and day
formatted_dates = [datetime.strftime(dt, '%b %d') for dt in datetime_objects]

# Plot the data
plt.plot(formatted_dates, y_values, marker='o')
plt.xlabel('Date')
plt.ylabel('Data')
plt.title('Plot of Data over Dates')
plt.xticks(rotation=45)
plt.show()