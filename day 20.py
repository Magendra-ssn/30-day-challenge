import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="Magendra6the",database="mydatabase")
dbse=mydb.cursor()

#dbse.execute("CREATE DATABASE emp")
#dbse.execute("USE emp")

dbse.execute("CREATE TABLE e (e_name VARCHAR(40),ID SMALLINT PRIMARY KEY,salary INT)")
dbse.execute("INSERT INTO e VALUES ('paul',1,100000)")
dbse.execute("INSERT INTO e VALUES( 'Rahul',2,20000)")
dbse.execute("INSERT INTO e VALUES( 'Gautam',3,30000)")
dbse.execute("INSERT INTO e VALUES( 'Surya',4,40000)")
dbse.execute("INSERT INTO e VALUES( 'Rishab',5,50000)")
dbse.execute("INSERT INTO e VALUES( 'Harish',6,60000)")
dbse.execute("INSERT INTO e VALUES( 'Sahit',7,70000)")
#dbse.commit()
dbse.execute("SELECT * FROM e")
print("The database")
for i in dbse:
    print(i)
dbse.execute("SELECT MIN(salary),MAX(salary) FROM e")
for j in dbse:
    print(j)
dbse.execute("SELECT COUNT(ID) FROM e")
for k in dbse:
    print(k)
dbse.execute("SELECT LEFT(e_name,3) AS ExtractString FROM e")
for a in dbse:
    print(a)


