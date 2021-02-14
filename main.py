import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="******",
    database="mydatabase"
)
mycursor=mydb.cursor()
mycursor.execute("select * from passwords")
result=mycursor.fetchall()
for i in result:
    print(i)