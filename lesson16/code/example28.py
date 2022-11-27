# Load a specific sheet by name
worksheet = workbook.sheet_by_name('Sheet1')

# Load a specific sheet by index 
worksheet = workbook.sheet_by_index(0)

# Retrieve the value from cell at indices (0,0) 
sheet.cell(0, 0).value