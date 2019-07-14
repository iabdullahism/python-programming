
"""
Code Challenge
  Name: 
    weeks
  Filename: 
    weeks.py
  Problem Statement:
    Write a program that adds missing days to existing tuple of days
  Input: 
    ('Monday', 'Wednesday', 'Thursday', 'Saturday')
  Output:
    ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
"""



Week_list=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
User_input=input("enter input >").split(' ')
Length_weeklist=len(Week_list)
i=0
while(i<Length_weeklist):
    if(Week_list[i] in User_input):
        i=i+1
    else:
        User_input.insert(i,Week_list[i])
        i=i+1
         
print(User_input)
User_touple=tuple(User_input)
print(User_touple)