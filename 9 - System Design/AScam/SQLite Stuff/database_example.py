import sqlite3

db = sqlite3.connect('test.db')

cursor = db.cursor()
# cursor.execute('''CREATE TABLE profile(id INTEGER, firstname TEXT, lastname TEXT)''')
cursor.execute('''INSERT INTO profile(id, firstname, lastname)
				VALUES(?,?,?)''', (1, 'Bob', 'Ross'))

db.commit()
db.close()
