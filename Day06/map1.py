
"""
Code Challenge
  Filename: 
    map1.py
  Problem Statement:
      import random

    names = ['Mary', 'Isla', 'Sam']
    code_names = ['Mr. Pink', 'Mr. Orange', 'Mr. Blonde']

    for i in range(len(names)):
        names[i] = random.choice(code_names)

    print (names)

As you can see, this algorithm can potentially assign the same 
secret code name to multiple secret agents. 


Rewrite the above code using map and lambda.


"""
 
    
    
import random
userList=[]
while(True):
    user_name=input("enter names >")
    if not user_name:
        break
    else:
        userList.append(user_name)    
    
    
code_names = ['Mr. Gaurav singh', 'Mr. Narender Singh Patel', 'Mr. Amit-Swami']   

print(list(result)) 
Secreate_name=list((map(lambda username:random.choice(code_names), userList)))
print(Secreate_name)    

   
    
    
    
    
 