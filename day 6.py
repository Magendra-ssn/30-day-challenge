#Q1 Merge 2 dictionaries
print("Before merging")
bat={1:'rohit',2:'kohli',3:'gill'}
bowl={4:'jadeja',5:'bumrah',6:'shami'}
print(bat)
print(bowl)
for i,j in bowl.items():
    bat[i]=j
print("After merging")
print(bat)
print()

#Q2 remove a key from dictionary
a={1:'hi',2:'hello',3:'bye'}
print("After removing")
a.pop(1)
print(a)
print()

#Q3 mapping two lists into a dictionary
keys=['red','green']
values=['34','35']
di=dict(zip(keys,values))
print("After mappping")
print(di)
print()

#Q4 Length of a set
set={'dhoni','bravo','jadeja'}
print(set)
x=len(set)
print("Length of set is : ",x)
print()

#Q5 Removing intersection of set2 from set1
set1={1,2,3,4,5}
set2={4,5,6,7,8}
print("set1 : ",set1)
print("set2 : ",set2)
print("After removing intersection")
set3=set1-set2
print(set3)


