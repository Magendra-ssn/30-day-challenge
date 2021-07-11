#Q1
l1=['eat','work','repeat']
obj1=enumerate(l1)
print(l1)
print("Enumerate object : ",type(obj1))
print("Counter value with list value")
for ele in enumerate(l1):
    print(ele)
print()

#Q2
t1=('hi','bye','goodnight','goodmorning')
obj2=enumerate(t1)
print("Counter value with tuple value")
for i in obj2:
    print(i)
