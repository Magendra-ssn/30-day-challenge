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

#Q2 sort list and convert into set
l=[1,2,7,8,3,4,5]
print("List = ",l)
l.sort()
print("List after sorting : ",l)
lset=set(l)
print("converted to set : ",lset)
print()

#Q3 get items list from dictionary and sort without function
dic={'mag':1,'mage':2,'magendra':10,'maggie':8}
it=dic.keys()
x=list(it)
x.sort()
print("Sorting keys using function ")
print("{",end="")
for i in range(len(x)):
    print(x[i],":",dic[x[i]],",",end="")
print("}")

#without function
di={'mag':1,'mage':2,'magendra':10,'maggie':8}
i=di.keys()
y=list(i)
z=[]
for i in range(len(y)): #sorting wihtout using function
    for j in range(i+1,len(y)):
        if(y[i]>y[j]):
            temp=y[i]
            y[i]=y[j]
            y[j]=temp


print("Sorting keys without function ")
print("{",end="")
for i in range(len(x)):
    print(y[i],":",di[x[i]],",",end="")
print("}")
print()

#Q4 replace first occurence of a word
m=input("Enter string ")
n=input("Enter substring ")
o=input("Enter string to be replaced ")
p=m.split()
for i in range(len(p)):
    if(p[i]==n):
        p[i]=o
        break
str=""
for ele in p:
    str+=ele
    str+=" "
print("After replacing : ",str)








