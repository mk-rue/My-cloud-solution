import pymysql

connection = pymysql.connect(host='localhost',user='root',password='',database='company_db')

cursor = connection.cursor()

cursor.execute("SELECT* FORM company")
rows = cursor.fetchall()
connection.close()
for row in rows:
    print(row)