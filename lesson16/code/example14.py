import csv

with open('file.csv', 'r', encoding='UTF-8') as f:
    data = csv.reader(f, delimiter=';')
    for row in data:
        print(row)