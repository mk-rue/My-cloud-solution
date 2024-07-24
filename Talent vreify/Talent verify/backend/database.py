import mysql.connector

connection = mysql.connector.connect(host="localhost",user="root",password="",database="company_db")

if connection.is_connected():
    print('connected successfully')
    #perform db opperations
else:
    print('Failed to connect')


connection.close()