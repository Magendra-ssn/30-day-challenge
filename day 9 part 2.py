#Q6 positive or negative
n=eval(input("Enter number "))
if(n>=0):
    print("Number is positive")
else:
    print("Number is negative")
print()
#Q7 days to ages
m=int(input("Enter number of days "))
x=m/365
print("Number of ages : ",x)
print()

#Q9 trigonometry using python
import math
y=30
print("find sin(30)")
print(math.sin(math.radians(90)))
print()

#Q10 Calculator
print("CALCULATOR")
a=input('Enter operator ')
b=int(input("Enter 1st number "))
c=int(input("Enter 2nd number "))
if(a=='+'):
    print(b+c)
elif(a=='-'):
    print(b-c)
elif(a=='*'):
    print(b*c)
elif(a=='/'):
    print(b/c)
else:
    print("Invalid operator")




