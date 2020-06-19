import sqlite3

# Create dataBase and conect

db = sqlite3.connect("app.db")
db.execute(
    "CREATE TABLE if not exists skills (name TEXT,progress integer, user_id integer)")

db.close
