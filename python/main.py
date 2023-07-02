import pandas as pd
import csv

kept_sections = [0, 1, 4, 5, 6, 7, 8, 9, 12, 25]

def read_csv_file(file_path):
    data = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            modified_row = [row[col_index] for col_index in kept_sections if col_index < len(row)]
            data.append(modified_row)
    return data

csv_file_path = 'fitness-tracker\Activites\Activities (7).csv'
csv_data = read_csv_file(csv_file_path)
data = csv_data[1:]
rowing = []
cycling = []
running = []
weights = []
streching = []
other = []

for row in data:
    if row[0] == "Indoor Rowing" or row[0] == "Rowing":
        rowing.append(row)
    elif row[0] == "Yoga":
        streching.append(row)
    elif row[0] == "Indoor Cycling" or row[0] == "Cycling":
        cycling.append(row)
    elif row[0] == "Running" or row[0] == "Treadmill Running":
        running.append(row)
    elif row[0] == "Strength Training":
        weights.append(row)
    else:
        other.append(row)
 
#for row in data: 
#     print(row)
    
    
#for row in cycling:
#    print(row)
#for row in running:
#    print(row)
#for row in other:
#    print(row)
