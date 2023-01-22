#!C:\Python311\python.exe
import mysql.connector
import cgi

print("content-type:text/html\r\n\r\n")
print("<html>")
print("<body>")

print("<h1>Hello :)</h1>")

Form=cgi.FieldStorage()
fname=Form.getvalue("Name")
fpass=Form.getvalue("Password")
print("Thanks for register",fname)

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="application")

mycursor=mydb.cursor();
sql="insert into login page(Name,Password) values(%s,%s)"
val=(fname,fpass);

mycursor.execute(sql,val)

mydb.commit();

print("</body>")
print("</html>")
