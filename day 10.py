#Lets make a real life banking system using inheritence of classes. Joint account of a father and child with restricted access for the child

class bank_account:
    def __init__(self,name,balance):
        self.name=name

        self.balance=balance

    def details(self):
        print("Name : ",self.name)
        print("Account balance : ",self.balance)

class child_account(bank_account):
    def restricted(self):
        print("This account is restricted as the user is below 18")

s=0
while(s!=1):
 print("1.Emplyee\n2.Account holder")
 x=int(input("Select a option "))

 if(x==1):
  n=input('Enter your name ')
  if(n=='Jenny'):
    np=input('Hi Jenny Enter your password ')
    if(np=='1234'):
     m=input("Enter account holder's name ")
     n=float(input("Enter account balance "))
     if(m=='Magendra'):
      a=child_account(m,n)
     elif(m=='Rahul'):
      b=child_account(m,n)
  else:
    print("invalid user ")

 elif(x==2):
    p=input('Enter your name ' )
    if(p=='Magendra'):
     pi=input('Hi Magendra Enter your password ')
     if(pi=='3170'):
      a.details()
     else:
         print("Wrong password")
    elif(p=='Rahul'):
     pw=input("Hi Rahul Enter your password")
     if(pw=='3245'):
      b.details()
    else:
     a.restricted()
 s=int(input("Press 1 to exit and 0 to continue "))
