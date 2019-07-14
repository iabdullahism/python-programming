"""
Code Challenge
  Name: 
    copy command
  Filename: 
    copy.py
  Problem Statement:
    Make a program that create a copy of a file    
"""










with open('words.txt', mode='rt') as file :
    #open file as read mode
       with open('copy.txt', mode='wt') as file1:
           #create a file copy.txt as write mode
              for line in file:
                  #read file word.txt as line by line
                 file1.write(line)
                 #copy the data of word.txt into copy.txt


