try:
    print(x)

except NameError :
    print("Name error")

#Calculator
a=int(input("Enter 1st Number "))
b=int(input("Enter 2nd number "))

c=input("Enter operation ")
try:
    if(c=='+'):
        print(a+b)
    elif(c=='-'):
        print(a-b)
    elif(c=='*'):
        print(a*b)
    elif(c=='/'):
        print(a/b)
except:
    print("Wrong sign")
finally:
    print("Thank you for using our calculator ")

#Q3
try:
    print
except NameError:
    print("Name error")
else:
    print("Other type of error")
print()

print(" Q4 : try catch is needed only if expected error is small and does not affect the program, in case of fatal errors try catch block is not recommended")
print()

#Q5
try:
    n=int(input("Enter a number"))
    print(n)
except:
    print("Sorry sir")




