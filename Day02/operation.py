"""
Code Challenge
  Name: 
    Operations Function
  Filename: 
    operation.py
  Problem Statement:
    Write following functions for list operations. Take list as input from the User
    Add(), Multiply(), Largest(), Smallest(), Sorting(), Remove_Duplicates(), Print()
    Only call Print() function to display the results in the below displayed 
    format (i.e all the functions must be called inside the print() function 
    and only the Print() is to be called in the main script)

  Input: 
    5,2,6,2,3
  Output:
    Sum = 18
    Multiply = 360
    Largest = 6
    Smallest = 2
    Sorted = [2, 2, 3, 5, 6]
    Without Duplicates = [2, 3, 5, 6]  
"""
def Add(Operation_list1):
    i=0
    for value in Operation_list1:
         i=i+int(value)
         
    print("Addition of list element-",i)    
    
    
def Multiply(Operation_list2):
     j=1
     for value in Operation_list2:
         j=j*int(value)
         
     print("multification of list element-",j)    
    
def Sort_list(Operation_list2):
     print("sorted list-",sorted(Operation_list2))  
     
def Largest_data(Operation_list2):
     Operation_list2.sort()
     print("max Value in List-",Operation_list2[-1])
def RemoveDuplicate(Operation_list2):
    l2=[]
    for i in Operation_list2:
        if i not in l2:
            l2.append(i)
    print("after remove duplicate-",l2)  

  
Operation_list=[]
while(True):
    User_input=input("enter list data >")
    Operation_list.append( User_input)
    
    if not User_input:
        break
    
Operation_list2=Operation_list[:-1]
print(Operation_list2)
Add(Operation_list2)
Multiply(Operation_list2)
Sort_list(Operation_list2)   
Largest_data(Operation_list2)
RemoveDuplicate(Operation_list2)






