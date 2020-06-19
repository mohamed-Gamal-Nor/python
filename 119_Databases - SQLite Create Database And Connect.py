import sqlite3

db = sqlite3.connect("app.db")

# setup cursor
cr = db.cursor()

cr.execute(
    "CREATE TABLE if not exists users (user_id integer,name TEXT)")
cr.execute(
    "CREATE TABLE if not exists skills (name TEXT,progress integer, user_id integer)")
#cr.execute("INSERT INTO users (user_id,name) values(1,'Ahmed')")
#cr.execute("INSERT INTO users (user_id,name) values(2,'osama')")
#cr.execute("INSERT INTO users (user_id,name) values(3,'Mohamed')")
mylist = ["Ahmed", "sayed", "mahmoud", "Mohamed", "mona", "abeer"]
for key, name in enumerate(mylist):
    cr.execute(f"INSERT INTO users (user_id,name) values({key+1},'{name}')")
# Save
db.commit()
# Clsoe Db
db.close()
