
"""
Code Challenge
  Name: 
    Name Printing Checkerboard pattern
  Filename: 
    checker.py
  Problem Statement:
    Print the checkerboard pattern using escape Codes and Unicode 
    with multiple print statements and the multiplication operator 
  Hint: 
    Eight characters sequence in a line and 
    the next line should start with a space
    try to use the * operator for printing
  Input:
    No input required
  Output:
    * * * * * * * *
     * * * * * * * *
    * * * * * * * *
     * * * * * * * *
    * * * * * * * *
     * * * * * * * *
    * * * * * * * *

"""
string="*"*9
#the first statement will make 9 charactor string
q1=" ".join( string )
#q1 string create first space  and print 8 star digit at last
q2=" ".join( string )

#q2 string start with star and not read last charactor
print(q1[1:])
print(q2[0:-1])
print(q1[1:])
print(q2[0:-1])
print(q1[1:])
print(q2[0:-1])



"""
s=" * "*8
print(s)
s1=s
s2=s
print(s1.lstrip())
print(s1.rstrip())
print(s1.lstrip())
print(s1.rstrip())

"""

