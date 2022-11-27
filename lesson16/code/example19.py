import csv

lines = [
    {'name': 'Alexander Melnikov', 'age': 38, 'sex': 'm'},
    {'name': 'Mihail Tolstoy', 'age': 28, 'sex': 'm'},
]

with open('file_w.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['age','sex','name'])
    for line in lines:
        writer.writerow(line)
    # или просто
    # writer.writerows(lines)