"""
Code Challenge
  Name: 
    Teen Calculator
  Filename: 
    teen_cal.py
  Problem Statement:
    Take dictionary as input from user with keys, a b c, with some integer 
    values and print their sum. However, if any of the values is a teen -- 
    in the range 13 to 19 inclusive -- then that value counts as 0, except 
    15 and 16 do not count as a teens. Write a separate helper "def 
    fix_teen(n):"that takes in an int value and returns that value fixed for
    the teen rule. In this way, you avoid repeating the teen code 3 times  
  Input: 
    {"a" : 2, "b" : 15, "c" : 13}
  Output:
    Sum = 17
"""



# Taking multiple input from user
p=0
def fix_teen(n):
    if(n==13 or n==14 or n== 17 or n== 18 or n== 19):
        return 0
    elif(n==15 or n==16):
        return n
    else:
        return n

my_dict ={}

while(True):
     user_input = input("Enter Keys and Inputs: ")
 
     value = user_input.split(" ")
     #split all the contents in one string
     if user_input:
         if ' '.join(value[:-1]) not in my_dict:
             #connect two charactor into one and remove last values using[:-1]
             my_dict[' '.join(value[:-1])]=int(value[-1])
             #add into dictonary key and values
        
        
     if not user_input:
         break
     
for value in my_dict.values() :
   p= p+fix_teen(value)
   
print(p)