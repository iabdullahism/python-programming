
"""
Code Challenge
  Filename: 
    factorial.py
  Problem Statement:
    Find the factorial of a number. 
  
"""
from math import  factorial as fact
#include math library and import factorial function

Fact_num=int(input("enter input to find factorial>"))
#take input and convert into int

Fact_num=math.factorial(Fact_num)
#call factorial function using math.factorial()
print(Fact_num)