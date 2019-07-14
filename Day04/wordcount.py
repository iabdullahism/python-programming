"""
Code Challenge
  Name: 
    Word count
  Filename: 
    wordcount.py
  Problem Statement:
    Unix systems contain many utility functions. 
    One of the most useful to me is wc, the "word count" program. 
    If you run wc against a text file, it'll count the characters, words, 
    and lines that the file contains.
     
    The challenge for this exercise is to write a version of wc in Python. 
    However, your version of wc will return four different types of information 
    about the files:
 
        Number of characters (including whitespace)
        Number of words (separated by whitespace)
        .Number of lines
       . Number of unique words
    
    The program should ask the user for the name of an input file, 
    and then produce output for that file. 
    
"""
"""
Unique_list=[]
my_dict={}
user_file=input("enter file name :>")
with open(user_file, mode='rt') as file :
   file_contents = file.read().split(" ")
  
 #create a dictonary of words and related their frequency  
for i in file_contents:
    if i in my_dict:
        my_dict[i]+=1
    else:
        my_dict[i]=1



#print all unique word in text file  
for j in my_dict:
       if(my_dict[j]==1):
           
            Unique_list.append(j)
       else:
            continue
print("unique word list")  
uniqueNumber=0      
for unique in Unique_list:
    uniqueNumber+=1
   # print(unique)
print("total unique no.=",uniqueNumber)    
       
#count line no

with open(user_file, mode='rt') as file :
   file_contents = file.readlines()
   
print("total line no=",len(file_contents))   

#print all the charactor in text file including white space
with open(user_file, mode='rt') as file :
   file_context = file.read().split("\n")  

CharactorCount=' '.join(file_context)
print("total charactor in text file",len(CharactorCount))

"""



filename = input("Enter a filename: ")
 
number_of_characters = 0
number_of_words = 0
unique_words = set()
 
for number_of_lines, line in enumerate(open(filename), 1):
    number_of_characters += len(line)
    number_of_words += len(line.split())
    unique_words.update(line.split())
 
print("Number of lines: {}".format(number_of_lines))
print("Number of characters: {}".format(number_of_characters))
print("Number of words: {}".format(number_of_words))
print("Number of unique words: {}".format(len(unique_words)))
 


