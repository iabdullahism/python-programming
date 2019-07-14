
"""
Code Challenge
  Name: 
    Facorial
  Filename: 
    factorial.py
  Problem Statement:
    Find the factorial of a number. 
  Hint: 
    Factorial of 3 = 3 * 2 * 1= 6 
    Try to first find the function from math module using dir and help 
  Input:
    Take the number from the keyboard as input from the user.
"""

import math
#include math package

Fact_Num=input("enter a number>")
#enter input

Fact_Num=int(Fact_Num)

#type cast str to int

print(math.factorial(Fact_Num))
#call factorial function

