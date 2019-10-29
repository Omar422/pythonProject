# 71 . Python MySql p2

"""
# Insert Into Table: To fill a table in MySQL, use the "INSERT INTO" statement.
# Important!: Notice the statement: mydb.commit(). It is required to make the changes,
    otherwise no changes are made to the table.
# To insert multiple rows into a table, use the executemany() method.
    The second parameter of the executemany() method is a list of tuples, containing the data you want to insert.
# To select from a table in MySQL, use the "SELECT" statement.
# Note: We use the fetchall() method, which fetches all rows from the last executed statement.
#  select only some of the columns in a table with the "SELECT" statement followed by the
    column name(s)
# The fetchone() method will return the first row of the result.
# When selecting records from a table, you can filter the selection by using the "WHERE" statement.
# You can also select the records that starts, includes, or ends with a given letter or phrase.
    Use the % to represent wildcard characters.
"""

import mysql.connector

con = mysql.connector.connect(
    host    =   "localhost",
    user    =   "root",
    password=   "omarroot000",
    database=   "pythondb"
)

ex = con.cursor()

q = "INSERT INTO categories (name, description) VALUES (%s, %s)"
v = ("Programming", "Programming Articles")
ex.execute(q,v)
print(ex.rowcount, "Record Inserted")
v = [
        ("Python", "Programming Articles"),
        ("JAVA", "Programming Articles"),
        ("C#", "Programming Articles"),
        ("Javascript", "Programming Articles"),
        ("PHP", "Programming Articles")
    ]
ex.executemany(q,v)
# commit هذه الدالة تستخدم لحفظ المتغيرات التي تمت في قاعدة البيانات
con.commit()
print(ex.rowcount, "Record Inserted" )
print("---------------\nlast ID:",ex.lastrowid )

ex.execute("SELECT id,description FROM categories WHERE name = 'Python' ")
print("---------------\nUse where")
fetchall = ex.fetchall()
for i in fetchall:
    print(i)

ex.execute("SELECT name FROM categories WHERE name LIKE '%mming%' ")
print("---------------\nUse %")
fetchall = ex.fetchall()
for i in fetchall:
    print(i)

ex.execute("SELECT id, name FROM categories")
fetchall = ex.fetchall()
for x in fetchall:
    print(x)

ex.execute("SELECT id, name FROM categories")
print("---------------\nUse fetchone")
print(ex.fetchone())
