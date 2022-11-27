import csv

with open('file.csv', 'r', encoding='UTF-8') as f:
    data = csv.reader(f, delimiter=';', skipinitialspace=True)
    for row in data:
        print(row)