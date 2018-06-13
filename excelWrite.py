import xlwt

def writeToCell(sheetName,rn,cn,value):
	return sheetName.write(rn,cn,value)

book = xlwt.Workbook()
sheet = book.add_sheet('test')
writeToCell(sheet,0,0,"userName")
writeToCell(sheet,0,1,"passWord")
writeToCell(sheet,1,0,"TC1")
writeToCell(sheet,1,1,"TC2")
book.save('Sample.xls')