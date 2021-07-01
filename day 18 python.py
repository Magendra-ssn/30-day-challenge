import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="Magendra6the",database="magendra")
dbse=mydb.cursor()

dbse.execute("SELECT * FROM hospital")
for i in dbse:
    print(i)

#Q2
dbse=mydb.cursor()
dbse.execute("SELECT * FROM hospital WHERE pateint<10")
print("doctors with patients less than 10 ")
for i in dbse:
    print(i)

print("Docotrs with no patients")
dbse.execute("SELECT * FROM hospital WHERE pateint=0")
for j in dbse:
    print(j)