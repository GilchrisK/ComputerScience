import sqlite3
class login():
    def saveMyData(self):
        try:
            conn = sqlite3.connect('student.db')
            print("Opened database successfully")


            conn.execute('''CREATE TABLE IF NOT EXISTS USERS
                            (STUDENT_EMAIL      TEXT    NOT NULL
                            STUDENT_USERNAME     TEXT PRIMARY KEY NOT NULL
                            STUDENT_PASSWORD TEXT NOT NULL);''')
            print("User Accounts Table is created successfully")
            conn.close()
            return True
        except:
            return False

    def insertData(self,givenEmail,givenUser, givenPassword):
        try:
            conn = sqlite3.connect('accounts.db')
            # insert data into database table
            conn.execute('''insert into USERS  (STUDENT_EMAIL, STUDENT_USERNAME,STUDENT_PASSWORD) values (?, ?, ?)''',
                         (givenEmail,givenUser, givenPassword))
            conn.commit()
            conn.close()
            return True
        except:
            return False



if __name__ == '__main__':
    myDB = login()
    myDB.saveMyData()
    myDB.insertData("Abid@gmail.com","abid2", "Abid_password")