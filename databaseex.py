import sqlite3 #module 
connection = sqlite3.connect("/home/akil/Documents/payilagam python/sqldatabase.db")  #C:\\PySQL\\Academy.db
cursor = connection.cursor()
sql_command = """
             CREATE TABLE Student(
             RollNo INTEGER PRIMARY KEY,
             Sname VARCHAR(20),
             Grade CHAR(1),
             gender CHAR(1),
             Average DECIMAL(5,2),
             birth_date DATE);"""
cursor.execute(sql_command)
sql_command = """INSERT INTO
               Student(RollNo,Sname,Grade,Gender,Average,birth_date)
                VALUES(null, "Akshay", 'B','M', "87.8","2001-12-12");"""
cursor.execute(sql_command)
connection.commit()  #ctrl+s
print("Student Table Created")
