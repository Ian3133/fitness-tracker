import csv

#removed_sections = [2,3, 10, 11,14,15, ]
kept_sections = [0,1,4,5,6,7,8,9,12,25]

def read_csv_file(file_path):
    data = []
    with open(file_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            data.append(row)
    return data


csv_file_path = 'Activities.csv'
csv_data = read_csv_file(csv_file_path)
print(csv_data[5])

