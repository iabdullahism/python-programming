"""
Code Challenge ( Line Plot )

We have to find sea level rise in past 100 years
Read the file sealevel.csv which has data for 135 years

It has two parts in the data, year and the sea level rise in inches

Read the csv file using the csv reader and create two list
    1) Which stores the years from 1880 to 2014
    2) Which stores the sealevel increase in inches
    
Now plot the data using Line Plot
The plot should have the valid title,labels, ticks ( x and y ), legend

Is the  sea level increasing almost every year.

"""
years=[]
sealevel=[]
from matplotlib import pyplot as plt
import csv
with open("sealevel.csv") as file:
    file_reader=csv.reader(file,delimiter=",")
    next(file_reader)
    for data in file_reader:
        years.append(int(data[0]))
        sealevel.append(float(data[1]))
        
        
plt.plot(years,sealevel,label='Sea level')
plt.title("Is the  sea level increasing almost every year")
plt.xlabel("years")
plt.ylabel("sea level rise in inches")
plt.legend()
plt.show()        


