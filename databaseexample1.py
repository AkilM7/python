import sqlite3 #module 
connection = sqlite3.connect("/home/akil/Documents/payilagam python/sqldatabase.db")  #C:\\PySQL\\Academy.db
cursor = connection.cursor()
student_data = [("Thiru","C","M","75.2","1998-05-17"),
                ("Raja","B","F","75.2","1998-04-17"),
                ("Bala","A","M","72.2","1999-05-17"),
                ("Kannan","D","M","87.2","1998-05-27")]
for p in student_data:
    format_str = """INSERT INTO Student(Rollno, Sname, Grade, Gender,
                    Average,birth_date)
                    VALUES(Null, "{name}","{gr}","{gender}","{avg}",
                    "{birthdate}");"""
        # {} space holder
    sql_command = format_str.format(name=p[0],gr=p[1],gender=p[2],
                                    avg=p[3],birthdate=p[4])
    cursor.execute(sql_command)
connection.commit()
connection.close()
print("Records added")
