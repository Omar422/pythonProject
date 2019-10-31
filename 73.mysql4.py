# 73 . Python MySql p4

"""
# Update Table: You can update existing records in a table by using the "UPDATE" statement.
# Important!: Notice the statement: mydb.commit() It is required to make the changes,
    otherwise no changes are made to the table.
# Notice the WHERE clause in the UPDATE syntax: The WHERE clause specifies which record or records
    that should be updated. If you omit the WHERE clause, all records will be updated!
# You can limit the number of records returned from the query, by using the "LIMIT" statement.
# If you want to return five records, starting from the third record, you can use the "OFFSET" keyword
# You can combine rows from two or more tables, based on a related column between them
    by using a JOIN statement.
#  the LEFT JOIN statement: show all records.
"""

import mysql.connector

con = mysql.connector.connect(
    host    =   "localhost",
    user    =   "root",
    password=   "omarroot000",
    database=   "pythondb"
)

mycursor = con.cursor()

q = "UPDATE categories SET name = 'Python' WHERE name = 'Python3'"
mycursor.execute(q)
con.commit()
print(mycursor.rowcount,"Record(s) Updated")

print('\nAll Records:')
mycursor.execute("SELECT * FROM categories")
for x in mycursor.fetchall():
    print(x)

print('\nLIMIT 2 OFFSET 2:')
mycursor.execute("SELECT * FROM categories LIMIT 2 OFFSET 2")
for x in mycursor.fetchall():
    print(x)

print('\n INNER JOIN:')
mycursor.execute("SELECT categories.name AS cat, articles.article AS art FROM categories \
                    INNER JOIN articles ON categories.info = articles.id")
for x in mycursor.fetchall():
    print(x)

print('\n LEFT JOIN:')
mycursor.execute("SELECT categories.name AS cat, articles.article AS art FROM categories \
                    LEFT JOIN articles ON categories.info = articles.id")

for x in mycursor.fetchall():
    print(x)

print('\n RIGHT JOIN:')
mycursor.execute("SELECT categories.name AS cat, articles.article AS art FROM categories \
                    RIGHT JOIN articles ON categories.info = articles.id")
for x in mycursor.fetchall():
    print(x)
