

"""
Code Challenge
  Name: 
    Normally Distributed Random Data
  Filename: 
    normal_dist.py
  Problem Statement:
    Create a normally distributed random data with parameters:
    Centered around 150.
    Standard Deviation of 20.
    Total 1000 data points.
    
    Plot the histogram using matplotlib (bucket size =100) and observe the shape.
    Calculate Standard Deviation and Variance. 
"""
import numpy as np
                           #mean, sd, total
incomes = np.random.normal(150, 20, 1000)
#print("Mean value is: ", np.mean(incomes))
#print("Median value is: ", np.median(incomes))
import matplotlib.pyplot as plt
plt.hist(incomes,100)
plt.show()
print("Standard Deviation is: ", np.std(incomes))
print("Variance is: ", np.std(incomes)**2)

