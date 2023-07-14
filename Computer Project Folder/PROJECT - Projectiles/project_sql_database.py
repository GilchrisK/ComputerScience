import sqlite3
# _________________________ Creating the class and methods __________________
class login():
    # _____________ method to create tables _________________________________
    def createTable(self):
        try:
            conn = sqlite3.connect('accounts.db')
            print("Opened database successfully")

            conn.execute('''CREATE TABLE IF NOT EXISTS USERS 
                           (UserName      TEXT     PRIMARY KEY     NOT NULL,
                            password      TEXT    NOT NULL);''')

            print("Users Accounts Table is created successfully")
            conn.close()
            return True
        except:
            return False

    # _____________ method to insert data into the table _________________________________
    def insertData(self, givenUser, givenPassword):

        try:
            conn = sqlite3.connect('accounts.db')
            # insert data into database table
            conn.execute('''insert into USERS  (UserName, password) values (?, ?)''',
                         (givenUser, givenPassword))
            conn.commit()  # do not forget to commit the data (i.e. save the data on the table
            conn.close()
            return True
        except:
            return False


if __name__=="__main__":
    myDB = login()
    myDB.createTable()
    myDB.insertData("abid2", "Abid_password")


# import sqlite3
#
# def crt_adminAccount_table(): # creating table for student accounts
#     conn = sqlite3.connect('studentAccount.db')
#     print("Opened database successfully")
#
# # using create if exists to prevent the code to crash if the database already exists.
#     conn.execute('''CREATE TABLE IF NOT EXISTS DEPARTMENTS
#                    (STUDENT_ID         INT     PRIMARY KEY     NOT NULL,
#                     STUDENT_EMAIL      TEXT    NOT NULL,
#                     STUDENT_USERNAME     TEXT NOT NULL,
#                     STUDENT_PASSWORD TEXT NOT NULL
#                     );''')
#     print("Table created successfully!")
#     conn.close()
#
#
# def InsertData_studentDatabase():
#     pass
#
#
#
# if __name__ == '__main__':
#     crt_adminAccount_table()