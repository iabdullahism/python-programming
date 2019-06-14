"""
Code Challenge
  Name: 
    Pallindromic Integer
  Filename: 
    pallindromic.py
  Problem Statement:
    You are given a space separated list of integers. 
    If all the integers are positive and if any integer is a palindromic integer, 
    then you need to print True else print False.
    (Take Input from User)  
  Hint: 
      A palindromic number or numeral palindrome is a number that remains the same
      when its digits are reversed. 
      Like 16461, for example, it is "symmetrical"
      Shorter logic can be developed using any and all and List comprehension
  Input: 
    12 9 61 5 14
  Output:
    True
"""
#first create my list
my_list = [] 
user_input = input("Enter values >").split(' ')
#split function use to take multiple input at a time
LenMy_list=len(user_input)
#get length of list using length function
i=0
#initilize i=0
index=0
#initilize index=0
while(i<LenMy_list):#while loop is running when the index i is not equal of My_list Length
    
    if(user_input[i][::-1]==user_input[i]):
        #here check Palindrom of each element using slicing
         i=i+1
      #increase i to 1
         
    else:
        index=index+1  #this index indicates that if any false in list it wiil increase by 1
        i=i+1
        
         
if(index >=1):
    #when While loop False Then Control goto this statement and if the Index
    #is greate than zero that means minimam one false Occurs that it print false
   print("False")
else:
   print("true")


