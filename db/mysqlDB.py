import mysql.connector

conn = mysql.connector.connect(user='root', password='1234asdf', database='mysql', use_unicode=True)
cursor = conn.cursor()

cursor.execute('select * from USER_INFO')
values = cursor.fetchall()
print(values)
cursor.close()
conn.close()
