
"""
Code Challenge
  Name: 
    String Handling
  Filename: 
    stringhand.py
  Problem Statement:
    Take first and last name in single command from the user and print  
    them in reverse order with a space between them, 
    find the index using find/index function and then print using slicing concept of the index
  Input:
      Sylvester Fernandes
  Output: 
      Fernandes Sylvester     
"""

UserName="Sylvester Fernandes"
#input sample UserName

UserName=UserName[::-1]
#Reverse Username 

print(UserName)

print(UserName.index('F'))
#check the position of any charactor of String Using Index function

UserName=UserName.replace(" ","")
#Remove WhiteSpace Using Replace Function
print(UserName)
