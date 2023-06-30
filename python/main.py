import pandas as pd

kept_sections = [0, 1, 4, 5, 6, 7, 8, 9, 12, 25]

def edit_csv_file(file_path):
    df = pd.read_csv(file_path)
    df.loc[df["Activity Type"] == "Yoga", 'Time'] = '00:18:23'
    df.to_csv(file_path, index=False)

def read_csv_file(file_path):
    data = []
    df = pd.read_csv(file_path)
    for index, row in df.iterrows():
        modified_row = [row[col_index] for col_index in kept_sections if col_index < len(row)]
        data.append(modified_row)
    return data



csv_file_path = 'Activites\Activities (5).csv'        # need to change to accept all csv files there and make a big one or somthing or sql backend
edit_csv_file(csv_file_path)
csv_data = read_csv_file(csv_file_path)
data = csv_data
rowing = []
cycling = []
running = []
weights = []
streching = []
other = []

for row in csv_data:
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
 
#for row in csv_data: 
#     print(row)
    
    
#for row in cycling:
#    print(row)
#for row in running:
#    print(row)
#for row in other:
#    print(row)