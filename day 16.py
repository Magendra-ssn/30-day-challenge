#Q1
x=lambda a,b:a*b
print(x(2,2))
print()

#Q2
n=int(input("Enter number of elements in fibonacci series "))
lst=[0,1]
y=lambda c,d:int(c+d)
print(lst[0],"",lst[1],end=" ")
for i in range(n-2):
    z=y(lst[i],lst[i+1])
    print(z,end=" ")
    lst.append(z)
print()
#Q3
li=[1,2,3,4,5]
e=list(map(lambda x:x*2,li))
print("After multiplying list is : ",e)
print()

#Q4
l=[9,18,20,27,30]
f=tuple(filter(lambda x:(x%9==0),l))
print("Elemens divisible by 9 : ",f)
print()

#Q5
l1=[9,18,20,27,30,2,3,4,5,66,7]
f1=tuple(filter(lambda x:(x%2==0),l1))
print("number of even elements : ",len(f1))

