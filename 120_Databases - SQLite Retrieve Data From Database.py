import sqlite3

db = sqlite3.connect("app.db")

# setup cursor
cr = db.cursor()

cr.execute(
    "CREATE TABLE if not exists users (user_id integer,name TEXT)")
cr.execute(
    "CREATE TABLE if not exists skills (name TEXT,progress integer, user_id integer)")
# fetch data
cr.execute("SELECT user_id,name FROM users")
# print(cr.fetchone())
# print(cr.fetchone())
# print(cr.fetchone())
print('=' * 50)
# print(cr.fetchall())
print(cr.fetchmany(3))
db.commit()
# Clsoe Db
db.close()
