"""
Code Challenge
  Name: 
    Character Frequency
  Filename: 
    frequency.py
  Problem Statement:
    This program accepts a string from User and counts the number of characters (character frequency) in the input string.  
  Input: 
    www.google.com
  Output:
    {'c': 1, 'e': 1, 'g': 2, 'm': 1, 'l': 1, 'o': 3, '.': 2, 'w': 3}
"""
my_list=[]
#define empty list
my_dict={}
#define empty dictonary

user_input=input("enter string>")
#enter user_input string 
my_list=list(user_input)
#convert string into list
my_set=set(my_list)
#convert list into sets
ListLength=len(my_list)
#len function give length
for value in my_set:
    #itarate value in set one by one
    i=0
    j=0
    while(i<ListLength):
        #when i is not equal then my_list gives values and check value is 
        #equal to the sets value or not if it is equal than j will increase by one
        if(value==my_list[i]):
            
            j=j+1
            i=i+1
        else:
            i=i+1
    my_dict[value]=j        

print(my_dict)      
        
        
        
        
        
        
        
        
        
        
        
        
        
     
        
        
        