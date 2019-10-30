# 71 . Python MySql p2

"""
# The ORDER BY statement to sort the result in ascending or descending order.
# The ORDER BY keyword sorts the result ascending by default. To sort the result in
    descending order, use the DESC keyword
# Delete: delete records from an existing table by using the "DELETE FROM" statement
# Important!: Notice the statement: mydb.commit() It is required to make the changes
    otherwise no changes are made to the table
# Notice the WHERE clause in the DELETE syntax: The WHERE clause specifies which
    record(s) that should be deleted. If you omit the WHERE clause, all records will be deleted!
# delete an existing table by using the "DROP TABLE" statement.
# If the table you want to delete is already deleted, or for any other reason does not exist, you can
    use the IF EXISTS keyword to avoid getting an error.
"""

import mysql.connector

con = mysql.connector.connect(
    host    =   "localhost",
    user    =   "root",
    password=   "omarroot000",
    database=   "pythondb"
)

mycursor = con.cursor()

q = "SELECT * FROM categories ORDER BY name DESC"
mycursor.execute(q)

result = mycursor.fetchall()
for x in result:
    print(x)

q = "DELETE FROM categories WHERE name = 'Javascript'"
mycursor.execute(q)
con.commit()
print(mycursor.rowcount,"record(s) deleted")

mycursor.execute("SELECT * FROM categories ORDER BY name DESC")

result = mycursor.fetchall()
for x in result:
    print(x)

#mycursor.execute("CREATE TABLE categories_tt(name VARCHAR(255), description VARCHAR(255))")
mycursor.execute("SHOW TABLES")
print("Tables:")
for tbl in mycursor:
    print(tbl)

mycursor.execute("DROP TABLE categories_tt")
mycursor.execute("SHOW TABLES")
print("Tables:")
for tbl in mycursor:
    print(tbl)
