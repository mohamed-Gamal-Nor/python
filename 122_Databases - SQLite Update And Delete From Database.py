import sqlite3

db = sqlite3.connect("app.db")

# setup cursor
cr = db.cursor()

cr.execute("UPDATE users SET name = 'Gamal' WHERE user_id = 1")
cr.execute("DELETE FROM users WHERE user_id = 1")
# fetch data
cr.execute("SELECT * FROM users ")

print('=' * 50)
print(cr.fetchall())
db.commit()
# Clsoe Db
db.close()
