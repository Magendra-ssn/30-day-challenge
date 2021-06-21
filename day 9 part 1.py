#Q1 add 2 to every value in a list
l=[1,2,3,4,5,6,7]
print("List is ",l)
l1=[]
for i in l:
    j=i+2
    l1.append(j)
print("After adding 2 to every element list is ",l1)
print()



#Q3 fibonacci series
n1=int(input("Enter number of terms "))
print("FIBONACCI SERIES")
x=0
y=1
print(x,end=" ")
for i in range(n1-1):
    a=x+y
    print(a,end=" ")
    x=y
    y=a
print()

#Q4 Armstrong number
#sum of cube of digits is eqaul to the number
print()
m=371
n=m
armsu=0
while(m>0):
   d=m%10

   e=d*d*d
   armsu+=e
   m//=10

if(armsu==n):
    print(n," is a armstrong number")

#Q5 multiplication table of 9
print()
print("Multiplication table of 9 ")
for i in range(1,10,1):
    print(i," * 9 = ",i*9)





