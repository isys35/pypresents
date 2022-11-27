# Retrieve the value of a certain cell
sheet['A1'].value

# Select element 'B2' of your sheet 
c = sheet['B2']

# Retrieve the row number of your element
c.row

# Retrieve the column letter of your element
c.column

# Retrieve the coordinates of the cell 
c.coordinate