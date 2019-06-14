"""

Code Challenge
  Name: 
    Regular Expression 1
  Filename: 
    regex1.py
  Problem Statement:
    You are given a string N. 
    Your task is to verify that N is a floating point number.
    Take Input From User

    In this task, a valid float number must satisfy all of the following 
    requirements:  
   
    Number can start with +, - or . symbol.
  Hint: 
    Using Regular Expression 
  Input:
    4  
    4.000
    -1.00
    +4.54
  Output:
    False
    True
    True
    True
"""
import re



#li=['4','4.0','-1.00','+4.54','$77.0','34.0']
li = []
while True:
    inp = input("Enter: ")
    if not inp:
        break
    li.append(inp)
for val in li:
 if re.findall('^[+-]?\d*\.\d+$',val):
     #^ that start and $ last and ^-$ start to end complete match
     #[+-]? +,- accurance one or not
     #\d* means digit zero or more before digit
     #\. after digit point
     #\d+ one point digit or more point digit
     print ('yes')
 else:
     print ('no')


