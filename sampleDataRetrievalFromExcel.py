# Sample script to retrieve value from excel sheet
# Using xlrd library

import xlrd

# Get the number of Rows in a sheet
def getNoOfRows(sheetname):
	return sheetname.nrows

# Get the number of Columns in a sheet	
def getNoOfColumns(sheetname):
	return sheetname.ncols

# Get the values from a cell
def getCellValuesFromXL(sheetname,rn,cn):
	return sheetname.cell_value(rn,cn)		


book = xlrd.open_workbook('Sample.xls')
sheet = book.sheet_by_index(0)
print(getCellValuesFromXL(sheet,0,0))
print(getCellValuesFromXL(sheet,0,1))
print(getNoOfRows(sheet))
print(getNoOfColumns(sheet))
