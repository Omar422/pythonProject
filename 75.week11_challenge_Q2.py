import mysql.connector

con = mysql.connector.connect (
  host = "localhost",
  user = "root",
  password = "omarroot000",
  database = "pythondb"
)

mycursor = con.cursor()

create = "CREATE TABLE Employee( id INT AUTO_INCREMENT PRIMARY KEY, \
                    FirstName VARCHAR(255), LastName VARCHAR(255), \
                    Age INT(11), Gender VARCHAR(10), Salary VARCHAR(10))"
mycursor.execute(create)

q = "INSERT INTO Employee (FirstName, LastName, Age, Gender, Salary) VALUES (%s, %s, %s, %s, %s)"
add = [
    ("Ahmed","ALi","30","Male","10000"),
    ("Khalid","Muhammad","34","Male","7000"),
    ("Norah","Saleh","29","Female","7000")
]
mycursor.executemany(q, add)
con.commit()
print("\n", mycursor.rowcount,"record(s) Added")

mycursor.execute("SELECT * FROM Employee")
print("---------------\nAll Fields:")
for i in mycursor.fetchall():
    print(i)

mycursor.execute("SELECT FirstName,Gender,Salary FROM Employee ")
print("---------------\nFirstName, Gender, Salary")
for i in mycursor.fetchall():
    print(i)

mycursor.execute("SELECT * FROM Employee ORDER BY FirstName DESC")
print("---------------\nORDER BY FirstName DESC")
for i in mycursor.fetchall():
    print(i)

mycursor.execute("DELETE FROM Employee WHERE Age=34")
con.commit()
print(mycursor.rowcount,"record(s) deleted")


mycursor.execute("SELECT * FROM Employee")
print("---------------\nAll Fields:")
for i in mycursor.fetchall():
    print(i)
