"""
Code Challenge
  Name: 
    Centered Average
  Filename: 
    centered.py
  Problem Statement:
    Return the "centered" average of an array of integers, which we'll say is 
    the mean average of the values, except ignoring the largest and 
    smallest values in the array. 
    If there are multiple copies of the smallest value, ignore just one copy, 
    and likewise for the largest value. 
    Use int division to produce the final average. You may assume that the 
    array is length 3 or more.
    Take input from user  
  Input: 
    1, 2, 3, 4, 100
  Output:
    3
"""

avarage_list=[]

user_input=input("enter comma seperate :>").split(",")

for i in user_input:
    avarage_list.append(int(i))
    
avarage_list.sort()

avarage_list1=avarage_list[1:-1]

q=sum(avarage_list1)/len(avarage_list1)
print(round(q))




