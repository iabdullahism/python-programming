"""
Code Challenge
  Name: 
    E-commerce Data Exploration
  Filename: 
    ecommerce.py
  Problem Statement:
      To create an array of random e-commerce data of total amount spent per transaction. 
      Segment this incomes data into 50 buckets (number of bars) and plot it as a histogram.
      Find the mean and median of this data using NumPy package.
      Add outliers 
          
  Hint:
      Execute the code snippet below.
      import numpy as np
      import matplotlib.pyplot as plt
      incomes = np.random.normal(100.0, 20.0, 10000)
      print (incomes)
 
    outlier is an observation that lies an abnormal distance from other values 
    
"""

import numpy as np
import matplotlib.pyplot as plt
                           #mean,sd,range
spent_time= np.random.normal(100.0, 20.0, 10000)
plt.hist(spent_time,50) 

plt.xlabel('Time in(Seconds)')
plt.ylabel('Customers')
plt.title("a person total amount spent per transaction")
plt.show()
print("Mean value is: ", np.mean(spent_time))
print("Median value is: ", np.median(spent_time))

from scipy import stats
print("Mode value is: ", stats.mode(spent_time)[0])
 
print(plt.boxplot(spent_time))



#when we added a row data then after check mean and median of the data
#Median Remains Almost SAME
spent_time = np.append(spent_time, [10000000000])
plt.hist(spent_time,50) 
#here 50 means total 50 lines in graph
plt.xlabel('Time in(Seconds)')
plt.ylabel('Customers')
plt.show()
print(plt.boxplot(spent_time))
print("Median after added outlyares: ", np.median(spent_time))

#Mean Changes distinctly
print("Mean after added outlyares: ", np.mean(spent_time))
print("Mode value is: ", stats.mode(spent_time)[0])

#in outlayers data mean incerse very fast but median remains about same
#for check outlayers boxplot



