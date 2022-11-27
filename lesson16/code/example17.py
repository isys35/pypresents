import csv

csv.register_dialect('myDialect',
                     delimiter=';',
                     skipinitialspace=True,
                     quoting=csv.QUOTE_ALL)

with open('file1.csv', 'r') as f:
    data = csv.reader(f, dialect='myDialect')
    for row in data:
        print(row)

with open('file2.csv', 'r') as f:
    data = csv.reader(f, dialect='myDialect')
    for row in data:
        print(row)