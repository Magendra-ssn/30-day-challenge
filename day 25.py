#Q1
from datetime import datetime,date,timedelta
date_object = datetime.strptime('July 1 2014 2:43PM', '%B %d %Y %I:%M%p')
print(date_object)
print()

#Q2
dt = date.today() - timedelta(5)
print('Current Date :',date.today())
print('5 days before Current Date :',dt)
print()

#Q3
def date_datetime():
     my_date = date.today()
     my_time = datetime.min.time()
     my_datetime = datetime.combine(my_date, my_time)
     print("Converting date to date time : ",my_datetime)
date_datetime()
print()

#Q4
a=date.today()
for i in range(7):
    print(a+timedelta(i))

