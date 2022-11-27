import csv

with open('file.csv', 'r') as f:
    data = csv.DictReader(f, delimiter=';')
    for row in data:
        print(row)