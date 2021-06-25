import re
pattern="[a-zA-Z0-9]{1}"
n=input("Enter string ")
if(re.search(pattern,n)):
    print("Found")
else:
    print("Not found")
print()

pat="[\w*a\w*b.\w*]"
m=input("Enter string ")
if(re.search(pat,m)):
    print("contains ab")
else:
    print("Does not contain ab")
print()

pa=r".*[0-9]$"
o=input("Enter string ")
if(re.search(pa,o)):
    print("Contains number at end of string")
else:
    print("Does not contain number at end of string")
print()


p=r"[0-9]{1,3}"
print("Numbers of length 1-3")
x=input("Enter sentence ")
results=re.finditer(p,x)
for i in results:
    print(i.group(0))
print()

p1="^[A-Z]+$"
y=input("Enter string ")
print(bool(re.match(p1,y)))

