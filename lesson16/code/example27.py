# Import `xlrd`
import xlrd

# Open a workbook 
workbook = xlrd.open_workbook('example.xls')

# Loads only current sheets to memory
workbook = xlrd.open_workbook('example.xls', on_demand = True)