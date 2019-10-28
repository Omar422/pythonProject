# 70 . Python MySql
"""
# Python can be used in database applications. One of the most popular databases is MySQL.
# To be able to experiment with the code examples in this tutorial, you should have MySQL
    installed on your computer.
# Python needs a MySQL driver to access the MySQL database. In this tutorial we will use the
    driver "MySQL Connector".
#  use PIP to install "MySQL Connector". PIP is most likely already
    installed in your Python environment.
# DB:
    # To create a database in MySQL, use the "CREATE DATABASE" statement.
    # You can check if a database exists by listing all databases in your system by using the
        "SHOW DATABASES" statement.
    # To create a table in MySQL, use the "CREATE TABLE" statement.
        Make sure you define the name of the database when you create the connection
    #  check if a table exist by listing all tables in your database with the "SHOW TABLES" statement
    # When creating a table, you should also create a column with a unique key for each record.
        This can be done by defining a PRIMARY KEY
    # use the statement "INT AUTO_INCREMENT PRIMARY KEY" which will insert a unique
        number for each record. Starting at 1 and increased by one for each record
    # If the table already exists, use the ALTER TABLE keyword.
"""

import mysql.connector

mydb = mysql.connector.connect(
    host    =   "localhost",
    user    =   "root",
    password=   "",
    database=   "pythondb"
)

# cursor : use to send queries to the db
myquery = mydb.cursor()
#myquery.execute("CREATE DATABASE pythondb")
#myquery.execute("SHOW DATABASES")
#for x in myquery:
    #print(x)

#myquery.execute("CREATE TABLE categories(name VARCHAR(255), description VARCHAR(255))")
#myquery.execute("ALTER TABLE categories ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
myquery.execute("SHOW TABLES")
for x in myquery:
    print(x)
