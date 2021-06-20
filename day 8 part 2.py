#Q5 change occurences of first char to capital
st=input("Enter string ")
a=st[0]
b=a.upper()
c=st.replace(a,b)
print("After replacing ",c)
print()

#Q6 find repeated items in a list
l=[1,2,3,1,4,3]
l1=[]
l2=[]
for i in l:

    if(i not in l1):
        l1.append(i)
    else:
        l2.append(i)
print("Repeated items are :",l2)
print()

#Q7 finding sum and dividing
m=5
n=6
o=7
su=m+n+o
p=int(input("Enter number to be divided"))
print("After dividing the sum : ",su/p)
print()

#Q8 mean,median and mode
import statistics
num1=25
num2=37
num3=25

mean=(num1+num2+num3)/3
lis=[num1,num2,num3]
print("Mean of numbers = ",mean)
print("Median of numbers = ",statistics.median(lis))
print("Mode of numbers = ",statistics.mode(lis))
print()

#Q9 swapping cases
stri='MagendrA'
print("string before swappping cases : ",str)
strin=''
for j in range(len(stri)):
    if(stri[j].isupper()==1):
       b=stri[j].lower()
       strin+=b
    elif(stri[j].islower()==1):
        c=stri[j].upper()
        strin+=c
print("After swapping cases : ",strin)
print()

#Q10
a=18
print("Integer : ",a)
print("Binary : ",bin(a))
print("Octa Decimal : ",oct(a))

