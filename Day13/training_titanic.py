"""
Code Challenge
  Name: 
    Exploratory Data Analysis - Titanic Analysis
  Filename: 
    titanic.py
  Dataset:
    training_titanic.csv
  Problem Statement:
      It’s a real-world data containing the details of titanic ships 
      passengers list.
      Import the training set "training_titanic.csv"
  Answer the Following:
     1. How many people in the given training set survived the disaster ?
     2.How many people in the given training set died ?
	 
      3.Calculate and print the survival rates as proportions (percentage) 
      by setting the normalize argument to True.
      Males that survived vs males that passed away
      Females that survived vs Females that passed away
      
      4.Does age play a role?
      since it's probable that children were saved first.
      
      Another variable that could influence survival is age; 
      since it's probable that children were saved first.

      You can test this by creating a new column with a categorical variable Child. 
      Child will take the value 1 in cases where age is less than 18, 
      and a value of 0 in cases where age is greater than or equal to 18.
 
      Then assign the value 0 to observations where the passenger 
      is greater than or equal to 18 years in the new Child column.
      Compare the normalized survival rates for those who are <18 and 
      those who are older. 
    
      To add this new variable you need to do two things
        1.     create a new column, and
        2.     Provide the values for each observation (i.e., row) based on the age of the passenger.
    
  Hint: 
      To calculate this, you can use the value_counts() method in 
      combination with standard bracket notation to select a single column of
      a DataFrame
"""
import pandas as pd
import numpy as np

#Read csv file
titanic_data = pd.read_csv("training_titanic.csv")
"""
first read csv file and then analysis the data using info method if some mission 
values then add mean value in
this most important step 
"""
titanic_data['Age'] = titanic_data['Age'].replace(0, np.NaN)

titanic_data = titanic_data.fillna(titanic_data.mean())

#print(titanic_data.info())
#first question

#1. how many people servised in disaster      
People_servived=titanic_data['Survived'].value_counts()
print("People servives in disester= ",People_servived[1],"Peoples")

# 2.How many people in the given training set died ?
print("People Dead in disester= ",People_servived[0],"Peoples")
#  3.Calculate and print the survival rates as proportions (percentage) 
# by setting the normalize argument to True.
# Males that survived vs males that passed away
# Females that survived vs Females that passed away
ratio=titanic_data.groupby(['Survived','Sex']).apply(lambda x: len(x))
#for divide the data among male survivde/male dead and female servived/dead
ratio_list=list(ratio)
print("Males that survived vs males that passed away=",(ratio_list[3]/(ratio_list[3]+ratio_list[1]))*100,"%")   
print("Females that survived vs Females that passed away=",(ratio_list[2]/(ratio_list[2]+ratio_list[0]))*100,"%")   

# Does age play a role? that means child is less saved either the others 

child=titanic_data["Survived"][(titanic_data['Age']<18) & (titanic_data['Survived']==1)].value_counts()
others=titanic_data["Survived"][(titanic_data['Age']>18) & (titanic_data['Survived']==1)].value_counts()
if(list(child)[0]>list(others)[0]):
	print("childern  saved compare to mature people")
else:
	print("childern less saved compare to mature people")
	
"""
   To add this new variable you need to do two things
        1.     create a new column, and
        2.     Provide the values for each observation (i.e., row) based on the age of the passenger.
    
"""

titanic_data["child_data"] = titanic_data["Sex"].map(lambda x: 0 if x == 'male' else 1 )
titanic_data['age<18']=titanic_data['Age'].map(lambda x: 0 if x>18 else 1)
titanic_data['age>18']=titanic_data['Age'].map(lambda x: 0 if x<18 else 1)
      





""""
this is my approch
2-
child_save=df[(df['Age']<=20) &(df['Survived']==1)]
child_group=list(child_save['Age'].value_counts())
sum1=sum(child_group)
print("save child",sum1)


young=df[((df['Age']>20) &(df['Age']<=40)) &(df['Survived']==1)]
young_group=list(young['Age'].value_counts())
sum2=sum(young_group)
print("save young",sum2)

old=df[(df['Age']>40)&(df['Survived']==1)]
old_group=list(old['Age'].value_counts())
sum3=sum(old_group)
print("save old",sum3)
"""

"""
3 df["child"]=df['Age'].map(lambda x: 1 if x<18 else 0)
"""