# Напечатать строчку за строчкой
for cellObj in sheet['A1':'C3']:
      for cell in cellObj:
              print(cells.coordinate, cells.value)
      print('--- END ---')