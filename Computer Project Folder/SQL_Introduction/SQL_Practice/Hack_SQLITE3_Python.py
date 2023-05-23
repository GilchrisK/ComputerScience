import sqlite3
def create_Students_table():
# let us create a table
    db = "./students.db"
    conn = sqlite3.connect(db)
    c = conn.cursor()
    cmd = "CREATE TABLE IF Not EXISTS students (Name TEXT, Age INT)"
    c.execute(cmd)
    data = [("Robert", 10), ("Sally", 15), ("Matthew", 7)]
    c.executemany("INSERT INTO students VALUES (?,?)", data)
    conn.commit()
    print("students table created and 3 records added")

def print_all_records():
# print all
    db = "./students.db"
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute("SELECT * from students")
    allResults = c.fetchall()
    print(allResults)
    conn.close()




if __name__ == "__main__":
    create_Students_table()