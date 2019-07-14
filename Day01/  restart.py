"""
Code Challenge
  Name: 
    Replacing of Characters
  Filename: 
    restart.py
  Problem Statement:
    In a hardcoded string RESTART, replace all the R with $ except the first occurrence and print it.
  Input:
    RESTART
  Output: 
    RESTA$T
"""
     Sample_String="restart"
     firstchar = Sample_String[0]
     #take first charcator into firstchar variable
    modifiedstr = Sample_String[1:].replace('r', "$")
    #using replace function to replcae a specific charactor 
    print(firstchar+ modifiedstr)
    