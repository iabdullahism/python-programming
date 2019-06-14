
"""
Code Challenge
  Name: 
    Reverse Function
  Filename: 
    reverse.py
  Problem Statement:
    Define a function reverse() that computes the reversal of a string.
    Without using Python's inbuilt function
    Take input from User  
  Input: 
    I am testing
  Output:
    gnitset ma I  
"""

def Reverse(User_string):
      Reverse_String=User_string[::-1]
      print( Reverse_String)
      
Input_String=input("enter String for reverse >")
Reverse(Input_String)