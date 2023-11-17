import sqlite3
def createTable():
    conn = sqlite3.connect('test.db')
    print("Opened database successfully")
    # use CREATE TABLE IF NOT EXISTS COMPANY instead to avoid crashing
    conn.execute('''CREATE TABLE IF NOT EXISTS COMPANY
            (staffID INT PRIMARY KEY NOT NULL,
             name TEXT NOT NULL,
              room INT NOT NULL,
               address CHAR(50),
                salary REAL);''')
    print("Table created successfully")
    conn.close()

# def insertData():
#     conn = sqlite3.connect('test.db')
#     # to improve, i.e. using variables instead,
#     # see
# # https://stokesfc.sharepoint.com/:u:/s/Computing/ESdSsKJk3qJHkXwlKDnR4ggBqyI
# # Yp44NNokyyH5ranSMOA?e=1xv2UT
#     conn.execute("INSERT INTO COMPANY (staffID,name, room, address, salary)\
#                  VALUES (1, 'Paul', 32, 'Stoke', 20000.00 )");
#     # here is few records will be inserted:
#     conn.execute("INSERT INTO COMPANY (staffID,name, room, address, salary)\
#                  VALUES (2, 'Allen', 25, 'Newcastle', 15000.00 )");  # first record
#
#     conn.execute("INSERT INTO COMPANY (staffID,name, room, address, salary)\
#                  VALUES (3, 'Ali', 23, 'Stafford', 20000.00 )");    # second record
#
#     conn.execute("INSERT INTO COMPANY (staffID,name, room, address, salary)\
#                  VALUES (4, 'Mandy', 25, 'Fenton ', 65000.00 )");  # third record
#
#     conn.commit() #if missing you will not be able to store data
#     print("Records created successfully")
#     conn.close()
#
# def selectData():
#     conn = sqlite3.connect('test.db') # connect to existing database
#     print("Opened database successfully")
#     cursor = conn.execute("SELECT staffid, name, salary from COMPANY")
#     #print(cursor)
#     # cursor is an object that is used to make the connection for executing SQL queries.
#     # It acts as middleware between SQLite database connection and SQL query.
#     # It is created after giving connection to SQLite database.
#     for row in cursor: # row means the record
#         print("Staff ID = ", row[0]) # row[0] means the value of the first field in the record
#         print("Staff NAME = ", row[1]) #row[1] means the value of the second field in the record
#         print("Staff SALARY = ", row[2], "\n") # “\n” will add a line to make it more presentable
#     print("Operation done successfully")
#     conn.close()
#
#
#
#
if __name__ == "__main__":
    createTable()
#     insertData()
#     selectData()