import csv

with open('file.csv', 'r') as f:
    data = csv.reader(f)
    for row in data:
        print(row)