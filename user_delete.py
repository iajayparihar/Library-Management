import sqlite3


conn = sqlite3.connect('instance/mydb.db')
cursor = conn.cursor()

delete_id = 2


cursor.execute('DELETE FROM user WHERE id = ?', (delete_id,))


conn.commit()


conn.close()
print('data deleted success')