"""
Code Challenge
  Name: 
    Formatted String
  Filename: 
    format2.py
  Problem Statement:
    Write a program to print the output in the given format. 
    Take input from the user. 
  Hint:
    Try to serach for some function in the str class using help() and dir()
  Input:
    Welcome to Pink City Jaipur
  Output:
    Welcome*to*Pink*City*Jaipur
"""


 formatString=input("Enter Sample String>")
 #take input from users using input function
 
formatString=formatString.replace(" ","*")
#replace whiteSpace To "*" using replace Function
print(formatString)