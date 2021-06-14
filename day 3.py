from tkinter import *
import tkinter.font as font
root=Tk()

root.title("Employee registration form")
root.configure(background='blue')
root.geometry('600x400')
myfont=font.Font(family='Helvetica')

employee_name=Label(root,text="Employee name").grid(row=0,column=0)
employee_id=Label(root,text="Employee ID").grid(row=1,column=0)
employee_phone=Label(root,text="Employee phone").grid(row=2,column=0)
employee_wn=Label(root,text="watsapp number").grid(row=3,column=0)
employee_email=Label(root,text="Email ID").grid(row=4,column=0)
employee_city=Label(root,text="city").grid(row=5,column=0)
employee_state=Label(root,text="state").grid(row=6,column=0)
employee_salary=Label(root,text="Employee salary").grid(row=7,column=0)
employee_allowance=Label(root,text="Employee allowance").grid(row=8,column=0)
employee_age=Label(root,text="Employee age").grid(row=9,column=0)


employee_name=Entry(root).grid(row=0,column=1)
employee_id=Entry(root).grid(row=1,column=1)
employee_phone=Entry(root).grid(row=2,column=1)
employee_wn=Entry(root).grid(row=3,column=1)
employee_email=Entry(root).grid(row=4,column=1)
employee_city=Entry(root).grid(row=5,column=1)
employee_state=Entry(root).grid(row=6,column=1)
employee_salary=Entry(root).grid(row=7,column=1)
employee_allowance=Entry(root).grid(row=8,column=1)
employee_age=Entry(root).grid(row=9,column=1)

checkbtn=Checkbutton(text="Agree to terms and conditions").grid(row=10,column=1)

def getval():
    print("Submitted succesfully ")
Button(text="Submit",font=myfont,command=getval).grid(row=12,column=1)




root.mainloop()