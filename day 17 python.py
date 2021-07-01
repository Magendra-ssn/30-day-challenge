import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="Magendra6the",database="employee")
dbse=mydb.cursor()
dbse.execute("SELECT * FROM emp")
for i in dbse:
    print(i)
dbse.close()
