"""
Code Challenge
  Name: 
    Digit Letter Counter
  Filename: 
    digit_letter_counter.py
  Problem Statement:
    Write a Python program that accepts a string from User and calculate the number of digits and letters.
  Hint:
    Store the letters and Digits as keys in the dictionary  
  Input: 
    Python 3.2
  Output:
    Digits 2
    Letters 6 
"""

my_dict ={}

while(True):
     user_input = input("Enter Keys and Inputs: ")
 
     value = user_input.split(" ")
     #split all the contents in one string
     if user_input:
         if ' '.join(value[:-1]) not in my_dict:
             #connect two charactor into one and remove last values using[:-1]
             my_dict[' '.join(value[:-1])]=float(value[-1])
             #add into dictonary key and values
        
        
     if not user_input:
         break
     
        
for key,value in my_dict.items():
              
               count1=0
               count2=0
               count3=0
               for i in key:
                     if(i.isdigit()):
                         pass
                     count2=count2+1
               for j in str(value):
                     if(j.isdigit()):
                         count1=count1+1
                     pass
                                        
                     
               print(key,value)
               print("Letters is:",count2)
               print("Digits is:=",count1)
               print("\n")
              
               





