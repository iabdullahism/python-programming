"""
Code Challenge
  Name: 
    Last Line
  Filename: 
    lastline.py
  Problem Statement:
    Ask the user for the name of a text file. 
    Display the final line of that file.
    Think of ways in which you can solve this problem, 
    and how it might relate to your daily work with Python.
"""

user_input=input("enter the file name >")
with open(user_input, mode='rt') as file :
   file_contents = file.readlines()
 
print (file_contents[-1])   