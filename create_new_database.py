import sqlite3

conn=sqlite3.connect("UPDB.db")
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS user(
userID INTEGER PRIMARY KEY,
username VARCHAR(20) NOT NULL,
firstname VARCHAR(20) NOT NULL,
surname VARCHAR(20) NOT NULL,
password TEXT NOT NULL);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS bank(
userID INTEGER NOT NULL,
website VARCHAR(20) NOT NULL,
website_password TEXT NOT NULL);
''')

cursor.execute("SELECT * FROM user")
print(cursor.fetchall())

cursor.execute("SELECT * FROM bank")
print(cursor.fetchall())

conn.commit()
conn.close()
