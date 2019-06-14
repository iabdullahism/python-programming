
"""
Code Challenge
  Name: 
    Create a list of absentee
  Filename: 
    absentee.py
  Problem Statement:
    Make a program that create a file absentee.txt
    The program should take max 25 students name one by one
    When the user enter a blank line, it should terminate the input
    Store all the name of students in the file    
    Once all the students names have been entered, it should display the list
    
"""

i=0
max_student=25
#max no of input 25
file = open('absentee.txt', mode='wt')
#topen function create a new files absentee.txt
while(i<max_student):
    #while loop terminate when the max data=25
    user_input=input("enter the student name >")
    if not user_input:
        break
       
    file.write(user_input+"\n")
    i=i+1
#after write file close this file absentee.txt
file.close()
    
with open('absentee.txt', mode='rt') as file :
   file_contents = file.readlines()
   print (file_contents)
    


    

