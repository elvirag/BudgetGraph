import xlsxwriter 
  
# Workbook() takes one, non-optional, argument  
# which is the filename that we want to create. 
workbook = xlsxwriter.Workbook('hello.xlsx') 
  
# The workbook object is then used to add new  
# worksheet via the add_worksheet() method. 
worksheet = workbook.add_worksheet() 
  
# Use the worksheet object to write 
# data via the write() method. 
worksheet.write('A1', 'Date') 
worksheet.write('B1', 'Expense') 
worksheet.write('C1', 'Amount') 
worksheet.write('D1', 'Category')
worksheet.write('E1', 'Means of Purchase') 
worksheet.write('F1', 'Buisness') 
  
# Finally, close the Excel file 
# via the close() method. 
workbook.close() 