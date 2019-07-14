"""
Code Challenge
  Name: 
    Pangram
  Filename: 
    pangram.py
  Problem Statement:
    Write a Python function to check whether a string is PANGRAM or not
    Take input from User and give the output as PANGRAM or NOT PANGRAM.
  Hint:
    Pangrams are words or sentences containing every letter of the alphabet at least once.
    For example: "The quick brown fox jumps over the lazy dog"  is a PANGRAM.
  Input: 
    The five boxing wizards jumps.
  Output:
    NOT PANGRAM
"""

def panagramFunction(user_string):
       StringData=['a','b','c','d','e','f','g','h','i','j' \
                   ,'k','l','m','n','o','p','q','r','s','t','u','v' \
                   ,'w','x','y']
       for number in user_string:
           i=0
           LengthUserString=len(number)
         
           while(i<LengthUserString):
             
               if(number[i] in StringData):
                   StringData.remove(number[i])
                  
                   i=i+1
               else:
                    
                  i=i+1
                  
                    
       LengthStringdata=len(StringData)
       if(LengthStringdata>0):
           print( "Not a Panagram String")
       else:
         print("Its a Panagram String")

InputPanagramString = input("Enter values >").split(' ')
panagramFunction(InputPanagramString)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    