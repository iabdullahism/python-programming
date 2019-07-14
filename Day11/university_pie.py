"""
Code Challenge ( Pie Chart )
  Name: 
    university data
  Filename: 
    university_pie.py
  Problem Statement:
    Write a python code and make a pie chart using following conditions:
        1.Read data from csv (University_data.csv)
        2.count GRE score for each university and plot a pie chart
        3.explode minimun gre score university
"""
import csv
import matplotlib.pyplot as plt

university_dict={}
with open("University_data.csv") as file:
    file_read=csv.reader(file,delimiter=",")
    next(file_read)
    for data in file_read:
        if data[0] in university_dict:
            university_dict[data[0]]+=int(data[1])
        else:
            university_dict[data[0]]=int(data[1])
university_name=[]
gre_score=[]
for item in university_dict:
    university_name.append(item)
    gre_score.append(university_dict[item])
    
colors =['blue','red','yellow','green','orange']
#colors =['#008fd5','#fc4f30','#e5ae37','#6d904f']
explode = (0, 0, 0, 0,0.5)
plt.pie(gre_score,labels=university_name, colors=colors, wedgeprops={'edgecolor':'black'},autopct='%.0f%%',explode=explode)
#wedgeprops fill color of radous and autopact tells the percentage of the each piece and
#explode 

plt.show()    
#first we make a dictonary that takes key as a university name and value their scores

  
            