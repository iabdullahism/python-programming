
"""
Code Challenge
  Name: 
    Baltimore City Analysis
  Filename: 
    baltimore.py
  Problem Statement:
    Read the Baltimore_City_Employee_Salaries_FY2014.csv file 
    and perform the following task :

    1. remove the dollar signs in the AnnualSalary field and assign it as a float
    2. Group the data on JobTitle and AnnualSalary, and aggregate with sum, mean, etc.
       Sort the data and display to show who get the highest salary
    x. Try to group on JobTitle only and sort the data and display
    x. How many employess are there for each JobRoles and Graph it
    5. Graph and show which Job Title spends the most groospay
    6. List All the Agency ID and Agency Name 
    7. Find all the missing Gross data in the dataset 
    
  Hint:



"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv("Baltimore_City_Employee_Salaries_FY2014.csv")

"""
 1. remove the dollar signs in the AnnualSalary field and assign it as a float
"""
#df['AnnualSalary']=df['AnnualSalary'].str.lstrip('$')
#df['AnnualSalary']=df['AnnualSalary'].astype(float)



"""
2- Group the data on JobTitle and AnnualSalary, and aggregate with sum, mean, etc.
 Sort the data and display to show who get the highest salary
"""	   
	   


        
df.describe()
max_salary= df.sort_values( by='AnnualSalary',ascending = [False])
print("max salary of ",max_salary[['JobTitle','AnnualSalary']].max())




"""
5. Graph and show which Job Title spends the most groospay
"""
#fill nan values  to mean
df['GrossPay']=df['GrossPay'].fillna(0)
most_groos_pay=df.sort_values(by='GrossPay',ascending = [False])
job_groosData=most_groos_pay[['JobTitle','GrossPay']]

#i remove groos pay contains zero

job_groosData1=job_groosData[(job_groosData['GrossPay']!=0.00)].dropna()
x=list(job_groosData1['JobTitle'].values)
y=job_groosData1['GrossPay']
index=list(range(len(x)))
plt.plot(index,y)
plt.xlabel("job Title")
plt.ylabel("Gross pay")
#plt.xticks(index,x,rotation=-90)
plt.legend()
plt.title("Job Title spends the most groospay")
plt.show()


"""
6-List All the Agency ID and Agency Name 
"""



p=df.groupby(['Agency', 'AgencyID'])
q=list(p.groups.keys())

"""
    7. Find all the missing Gross data in the dataset 
"""
#i already conver missing data into datase so if you want to find 
#before fillna then
df[df['GrossPay'].isnull()]

























