import xlwt
import xlrd
book=xlwt.Workbook()
sheet=book.add_sheet("sheet")

s_name=(['Magendra','S1',100],['Suganya','S2',90],['Sriram','S3',88],['Ponji','S4',80])
row=0
column=0
for name,ID,marks, in s_name:
    sheet.write(row,column,name)
    sheet.write(row,column+1,ID)
    sheet.write(row,column+2,marks)
    row+=1

book.save('student.xls')

import pandas as pd
from sqlalchemy import create_engine
df=pd.read_excel("student.xls",sheet_name="sheet",index_col=0)
engine=create_engine('mysql://root:Magendra6the@localhost/student')
df.to_sql("sheet", con=engine)



