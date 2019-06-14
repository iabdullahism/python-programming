
"""
Code Challenge
  Filename: 
    map2.py
  Problem Statement:

      names = ['Mary', 'Isla', 'Sam']

    for i in range(len(names)):
        names[i] = hash(names[i])

    print (names)



(Hopefully, the secret agents will have good memories and won’t forget each other’s secret code names during the secret mission.)


Rewrite the above code using map.
    

"""


name_list=[]
while(True):
    user_input=input("enter the user names .....>")
    if not user_input:
        break
    else:
        name_list.append(user_input)
    
hasNameList=list(map(lambda username:hash(username),name_list))

print(hasNameList)

 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    