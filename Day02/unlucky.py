
"""
Code Challenge
  Name: 
    Unlucky 13
  Filename: 
    unlucky.py
  Problem Statement:
    Return the sum of the numbers in the array, returning 0 for an empty array. 
    Except the number 13 is very unlucky, so it does not count and numbers that 
    come immediately after a 13 also do not count
    Take input from user  
  Input: 
    13, 1, 2, 13, 2, 1, 13
  Output:
    3
"""

def lucky_num(LuckyList):
     l1=len(LuckyList)
     i=0
     j=0
     while(i<l1):
         if(LuckyList[i]==13):
             i=i+2
         else:
             if(i==0):
                 j=j+LuckyList[i]
                 i=i+1
             elif(LuckyList[i-1]==13):
                 i=i+1
             else:
                  j=j+LuckyList[i]
                  i=i+1
     print(j)       
 
    


LuckyList=[]
user_input=input("enter inger num by comma seperate :> ").split(",")
for i in user_input:
    LuckyList.append(int(i))
  

lucky_num(LuckyList)