import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = "Aqwert54321"
)

cursorObject = dataBase.cursor()


cursorObject.execute("CREATE DATABASE aqxplay")

print("ALL DONE!")