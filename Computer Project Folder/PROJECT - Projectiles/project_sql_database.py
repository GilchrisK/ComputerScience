import sqlite3

def crt_adminAccount_table(): # creating table for student accounts
    conn = sqlite3.connect('studentAccount.db')
    print("Opened database successfully")

# using create if exists to prevent the code to crash if the database already exists.
    conn.execute('''CREATE TABLE IF NOT EXISTS DEPARTMENTS 
                   (STUDENT_ID         INT     PRIMARY KEY     NOT NULL,
                    STUDENT_EMAIL      TEXT    NOT NULL,
                    STUDENT_USERNAME     TEXT NOT NULL,
                    STUDENT_PASSWORD TEXT NOT NULL
                    );''')
    print("Table created successfully!")
    conn.close()


def InsertData_studentDatabase():
    pass



if __name__ == '__main__':
    crt_adminAccount_table()