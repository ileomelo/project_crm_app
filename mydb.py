import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'leo123456',
)

# Prepare a cursor object
cursorObject = dataBase.cursor()

# Create Data Base
cursorObject.execute("CREATE DATABASE db_app_crm")

print("All Done!!")