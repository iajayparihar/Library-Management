import sqlite3


conn = sqlite3.connect('instance/mydb.db')
cursor = conn.cursor()

delete_id = 1


cursor.execute('DELETE FROM borrow WHERE user_id = ?', (delete_id,))
# cursor.execute('Truncate table borrow')


conn.commit()


conn.close()
print('data deleted success')