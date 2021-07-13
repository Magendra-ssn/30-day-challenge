from threading import *
from time import *
from datetime import date,datetime

class t1(Thread):
    def run(self):
        print(datetime.today())
        sleep(0.2)

class t2(Thread):
    def run(self):
        print(datetime.today())
        sleep(1)


a = t1()
a.start()
b=t2()
b.start()
print("\nnumber of active threads : ",active_count())





