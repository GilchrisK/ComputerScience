import sqlite3
def make_table():
    conn = sqlite3.connect('db_homework.db')
    print("Opened database successfully")
    conn.execute('''CREATE TABLE IF NOT EXISTS tbl_subject
            (  HOMEWORK char(15) primary key not null,
               subject CHAR(10),
               date_due date NOT NULL
                );''')
    print("Table created successfully")
    conn.close()


def enter_homework(hw_details,var_subject,  given_date ):



    conn = sqlite3.connect('db_homework.db')
    conn.execute('''insert into tbl_subject (homework, subject, date_due) values (?,?,?)''',
                 (hw_details, var_subject, given_date))
    print("completed")
    conn.commit()
    conn.close()

def display_All_Homework():
    conn = sqlite3.connect('db_homework.db')
    cursor = conn.execute('''SELECT homework, subject, data_due''')


if __name__ == "__main__":
    make_table()

    var = True
    while var ==True:
        a = input(" Enter homework")
        b= input(" Enter a subject")
        c= input(" Enter a date")
        enter_homework(a, b, c)
        x = input("Do you want to add another record? ")
        if x == "No":
            var = False


