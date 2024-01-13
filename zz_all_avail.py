import sqlite3

# Connect to the SQLite database (replace 'your_database.db' with the actual name of your SQLite database file)
conn = sqlite3.connect('instance/mydb.db')
cursor = conn.cursor()

cursor.execute("UPDATE book SET status = 'Available'")
conn.commit()
conn.close()
print('now all Books are Available')