# Retrieve cell value 
sheet.cell(row=1, column=2).value

# Print out values in column 2 
for i in range(1, 4):
     print(i, sheet.cell(row=i, column=2).value)