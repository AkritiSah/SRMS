import sqlite3
def create_db():
    con=sqlite3.connect(database="rms.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS course(id INTEGER KEY AUTOINCREMENT,name text,duration text,charges text,discription text)")
    con.commit()

    create_db() 