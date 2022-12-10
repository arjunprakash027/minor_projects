import sqlite3

def create_table():
    conn = sqlite3.connect("databases/test.db")
    #print("Database created/connected succussfully")
    conn.execute(
         '''
         CREATE TABLE IF NOT EXISTS TRIVIA
         (
         ID INT PRIMARY KEY     NOT NULL,
         DATE            TEXT     NOT NULL,
         INFO           TEXT    NOT NULL
         );''')
    #print ("Table created successfully")

    conn.close()

def insert_values(a,b):
    conn = sqlite3.connect("databases/test.db")
    cursor = conn.cursor()
    sqlite_select_query = """SELECT * from TRIVIA"""
    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()
    next_record = len(records) + 1
    params = (next_record,a,b)
    conn.execute("INSERT INTO TRIVIA VALUES (?, ?, ?)", params)
    conn.commit()
    #print ("Records created successfully")
    conn.close()

def readSqliteTable():
    try:
        sqliteConnection = sqlite3.connect("databases/test.db")
        cursor = sqliteConnection.cursor()

        sqlite_select_query = """SELECT * from TRIVIA"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
     #   print("Total rows are:  ", len(records))
     #  print("Printing each row")
        for row in records:
            print("Id: ", row[0])
            print("date: ", row[1])
            print("info: ", row[2])
            print("\n")

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")




if __name__ == "__main__":
    create_table()
#    insert_values("10/11","a very good day indeed")
    readSqliteTable()



