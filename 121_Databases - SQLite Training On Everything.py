import sqlite3


def get_all_data():
    try:
        db = sqlite3.connect("app.db")
        print("conect to Datebase is successfully")
        cr = db.cursor()
        cr.execute("SELECT * FROM users")
        result = cr.fetchall()
        print(f"Data Base has {len(result)} Rows.")

        for row in result:
            print(f"USer_ID => {row[0]}", end=" ")
            print(f"USer_Name => {row[1]}")
    except sqlite3.Error as er:
        print(f"error Reading Data {er}")
    finally:
        if(db):
            db.close()
            print("date Base Conection is close")


get_all_data()
