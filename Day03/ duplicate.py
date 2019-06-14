
"""
Code Challenge
  Name: 
    Duplicate
  Filename: 
    duplicate.py
  Problem Statement:
    With a given list [12,24,35,24,88,120,155,88,120,155]
    Write a program to print this list after removing all duplicate values 
    with original order reserved  
"""


Duplicate_list= [12,24,35,24,88,120,155,88,120,155]

Remove_duplicate=set(Duplicate_list)
#remove duplicate in list covert into the sets set is a collection of unique values
 
print(list(Remove_duplicate))
