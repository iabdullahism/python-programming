"""
Code Challenge
  Name: 
    Vowels Finder
  Filename: 
    vowels.py
  Problem Statement:
    Remove all the vowels from the list of states  
  Hint: 
    Use nested for loops and in membership Operator
  Input:
    state_name = [ 'Alabama', 'California', 'Oklahoma', 'Florida']
  Output:
    ['lbm', 'Clfrn', 'klhm', 'Flrd']
    
"""

state_name=[ 'Alabama', 'California', 'Oklahoma', 'Florida']
vowels=['a','e','i','o','u','A','E','I','O','U']
final_list=[]
for state in state_name:
    l1=len(state)
   
    i=0
    temp_list=[]
    while(i<l1):
       
        if(state[i] in vowels):
      
      
         i=i+1
            
        else:
        
         temp_list.append(state[i])
         i=i+1
    final_list.append("".join(temp_list))   
 
print(final_list)    
            
         

          
