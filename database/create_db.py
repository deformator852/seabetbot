import sqlite3

conn = sqlite3.connect("admins.db")
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS admins (
    admin INTEGER PRIMARY KEY
);
''')
conn.commit()
conn.close()

