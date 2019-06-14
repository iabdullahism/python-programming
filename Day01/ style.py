"""
Code Challenge
  Name: 
    Styling of String
  Filename: 
    style.py
  Problem Statement:
    Convert to uppercase character
    Convert to lower character 
    Convert to CamelCase or TitleCase.
  Hint: 
    Try to find some function in the str class and see its help on how to use it.
    Using dir and help functions
  Input:
    Take the name as input from the keyboard. ( SyLvEsTeR )
"""


Sample_str="HHGjhbjhHbjhTFFSIkkalk"
#convert the following string into lower case string by using .lower function
lower_characte=Sample_str.lower()
print(lower_characte)

#convert upper case letter

upper_characte=Sample_str.upper()
print(upper_characte)
#convert string into uppercase letter

CamelCase=Sample_str.title()
#title function used to create Camelcase string
print(CamelCase)
