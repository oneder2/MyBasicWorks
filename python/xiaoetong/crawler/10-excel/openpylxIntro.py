import openpyxl


# create workbook
wb = openpyxl.Workbook()

# choose working subtable
ws = wb.active

# modify name of working subtable
ws.title = 'subtable0'

# add data, append will add a new row.
# the first row are always the table head
ws.append(['name', 'gender', 'age'])
# the following rows will be data
ws.append(['Aang', 'male', '18'])
ws.append(['Joseph', 'male', '18'])
ws.append(['Caleb', 'male', '22'])
ws.append(['Jacob', 'male', '19'])
ws.append(['Ridvic', 'male', '18'])

wb.save('student.xlsx')


