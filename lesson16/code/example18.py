import csv

lines = [
    ['Alexander Melnikov', '31', 'm'],
    ['Mihail Tolstoy', '28', 'm'],
]

with open('file_w.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    for line in lines:
        writer.writerow(line)
    # или просто
    # writer.writerows(lines)