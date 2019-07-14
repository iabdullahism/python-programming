"""
Code Challenge
  Name: 
    Random Data
  Filename: 
    random_data.py
  Problem Statement:
    Create a random array of 40 integers from 5 - 15 using NumPy. 
    Find the most frequent value with and without Numpy.
  Hint:
      Try to use the Counter class and also bincount
      
      
"""
data_dict={}
from collections import Counter 
import numpy as np                         
x=np.random.randint(5,15,40 )
p=Counter(x)
print(p)
for k,v in p.items():
    data_dict[k]=v
  
 
sort_dict=sorted(data_dict.items(),key=lambda x:x[1])
print("the more frequent data is=",sort_dict[-1][0])