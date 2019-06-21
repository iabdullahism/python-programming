
"""
Code Challenge
  Name: 
    Baltimore City Analysis
  Filename: 
    baltimore.py
  Problem Statement:
    Read the Baltimore_City_Employee_Salaries_FY2014.csv file 
    and perform the following task :

    0. remove the dollar signs in the AnnualSalary field and assign it as a float
    0. Group the data on JobTitle and AnnualSalary, and aggregate with sum, mean, etc.
       Sort the data and display to show who get the highest salary
    0. Try to group on JobTitle only and sort the data and display
    0. How many employess are there for each JobRoles and Graph it
    0. Graph and show which Job Title spends the most
    0. List All the Agency ID and Agency Name 
    0. Find all the missing Gross data in the dataset 
    
  Hint:



"""
import pandas as pd
import numpy as np
df=pd.read_csv("Baltimore_City_Employee_Salaries_FY2014.csv")

"""
 1. remove the dollar signs in the AnnualSalary field and assign it as a float
"""
#df['AnnualSalary']=df['AnnualSalary'].str.lstrip('$')
#df['AnnualSalary']=df['AnnualSalary'].astype(float)

"""