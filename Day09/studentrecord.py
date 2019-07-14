"""

Code Challenge 1
Write a python code to insert records to a sqlite
named db_University for 10 students with fields like 
Student_Name, Student_Age, Student_Roll_no, Student_Branch.

"""


import mysql.connector 
# connect to  MySQL server along with Database name

conn = mysql.connector.connect(user='rahulpandit', password='rahulpandit123',
                              host='db4free.net', database = 'roomseeker')
#, database = 'roomseeker'
c = conn.cursor()
c.execute("DROP Table student_data;")
# creating cursor

#cursor tells that where the position of row
c.execute ("""CREATE TABLE student_data(
          id INTEGER,
          student_name  TEXT,
          student_age INTEGER,
          Student_Roll_no INTEGER,
          Student_Branch TEXT
          )""")

c.execute("INSERT INTO student_data VALUES (01,'Sylvester', 23,7827,'computer science')")
c.execute("INSERT INTO student_data VALUES (02,'rahulpandit',78, 289,'computer science')")
c.execute("INSERT INTO student_data VALUES (02,'rahulpandit',78, 289,'computer science')")
c.execute("INSERT INTO student_data VALUES (02,'rahulpandit',78, 289,'computer science')")
c.execute("INSERT INTO student_data VALUES (02,'rahulpandit',78, 289,'computer science')")
c.execute("INSERT INTO student_data VALUES (02,'rahulpandit',78, 289,'computer science')")

conn.commit()

c.execute("SELECT * FROM student_data")
data=c.fetchall()
for value in data:
    print(value[1])
        
        
        
        ')        