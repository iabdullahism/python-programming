
"""
Code Challenge
  Name: 
    Romeo and Juliet
  Filename: 
    romeo.py
  Problem Statement:
    Let’s start with a very simple file of words taken from the text of 
    Romeo and Juliet. (romeo.txt)
    We will write a Python program to read through the lines of the file
    break each line into a list of words
    and then loop through each of the words in the line,
    and count each word using a dictionary.    
"""
i=0
my_dict={}
#dict1={}
with open('romeo.txt', mode='rt') as file :
   file_contents = file.read().split()
#   for i in file_contents:
#       if i in dict1:
#           dict1[i]+=1
#       else:
#           dict1[i]=1
   

my_set=set(file_contents)
ListLength=len(file_contents)

my_dict={}
for value in my_set:
    #itarate value in set one by one
    i=0
    j=0
    while(i<ListLength):
        #when i is not equal then my_list gives values and check value is 
        #equal to the sets value or not if it is equal than j will increase by one
        if(value==file_contents[i]):
            
            j=j+1
            i=i+1
        else:
            i=i+1
    my_dict[value]=j        

print(my_dict)      
        
       