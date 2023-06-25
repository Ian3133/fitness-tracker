import csv



kept_sections = [0,1,4,5,6,7,8,9,12,25]

def read_csv_file(file_path):
    data = []
    with open(file_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            modified_row = [row[col_index] for col_index in kept_sections if col_index < len(row)]
            data.append(modified_row)
    return data


csv_file_path = 'Activites\Activities.csv'        # need to change to accept all csv files there and make a big one or somthing or sql backend
csv_data = read_csv_file(csv_file_path)
rowing = []
cycling = []
running = []
other = []

for row in csv_data:
    if row[0] == "Indoor Rowing" or row[0] == "Rowing":
        rowing.append(row)
    elif row[0] == "Indoor Cycling" or row[0] == "Cycling":
        cycling.append(row)
    elif row[0] == "Running" or row[0] == "Treadmill Running":
        running.append(row)
    else:
        other.append(row)


#for row in csv_data: 
#     print(row)
    
    
#for row in cycling:
#    print(row)
#for row in running:
#    print(row)
#for row in other:
#    print(row)
