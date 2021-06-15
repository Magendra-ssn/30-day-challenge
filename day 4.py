#Q1

(a,b,c)=(30,30,30)
a/=50
b*=50
c+=60
print("after operation")
print(a,b,c)

#Q1 output
#after operation
#0.6 1500 90

#Q2

x = 'hello'
y = x[0:2]+'g'+x[3:len(x)] #since strings cannot be mutated
print(y)

#Q2 output
#heglo

#Q3
(a,b)=(24,5.12)
print("Before converting : ")
print("int a = ",a)
print("float b = ",b)

c=float(a)
d=int(b)
print("After converting : ")
print("float a = ",c)
print("int b = ",d)

#Q3 output
#Before converting :
#int a =  24
#float b =  5.12
#After converting :
#float a =  24.0
#int b =  5