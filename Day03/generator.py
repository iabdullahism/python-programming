# Taking multiple input from user

"""
Code Challenge
  Name: 
    generator
  Filename: 
    generator.py
  Problem Statement:
    This program accepts a sequence of comma separated numbers from user 
    and generates a list and tuple with those numbers.  
  Input: 
    2, 4, 7, 8, 9, 12
  Output:
    List : ['2', ' 4', ' 7', ' 8', ' 9', '12'] 
    Tuple : ('2', ' 4', ' 7', ' 8', ' 9', '122')
"""

Create_list = []

while True:
    user_input = input("Enter values >")
    
    #append this entry to the touple
    Create_list.append(user_input)
    
    if not user_input:
        break
#print list
print(Create_list)        
    
#convert list into touple using forcasting
Create_touple=tuple(Create_list)
print(Create_touple)

