data = [
   ['Имя', 'Пол', 'Возраст'],
   ['Алексей', 'муж.', '20'],
   ['Алина', 'жен.', '21'],
]

csv = ''
for row in data:
   csv += ','.join(row) + '\n'