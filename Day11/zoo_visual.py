
"""
Code Challenge ( Bar Plot )
  Name: 
    Zoo Visualisation
  Filename: 
    zoo_visual.py
  Problem Statement:
    Read the zoo.csv file
    Print the total number of water need by elephant / tiger / lion / zebra / kangaroo
    Show the total number of water needs by individual animal using a Bar Chart
  Hint:
      Use the concept of Dictionary
import csv
zoo_data = {}
with open('zoo.csv','rt') as ani:
    reader = csv.reader(ani,delimiter = ',')
    next(reader)
    for i in reader:
        if i[0] in zoo_data:
            zoo_data[i[0]] += int(i[2])
        else:
            zoo_data[i[0]] = int(i[2])

objects = tuple(map(lambda x: x ,zoo_data.keys()))
performance = list(map(lambda x: x ,zoo_data.values()))

"""


import csv
zoo_data = {}
with open('zoo.csv','rt') as ani:
    reader = csv.reader(ani,delimiter = ',')
    next(reader)
    for i in reader:
        if i[0] in zoo_data:
            zoo_data[i[0]]+=int(i[2])
        else:
            zoo_data[i[0]]=int(i[2])
            
animal_type=list(map(lambda x:x,zoo_data.keys()))            
required_water=list(map(lambda x:x,zoo_data.values()))
#make a lists 0,1,2,3,4
animal=[]
i=0
for i in range(len(animal_type)):
    animal.append(i)
#we cannot plot animal name so convert name into their related format
plt.ylim(0,3000)
plt.xlabel("Animal names")

# Setting the Y Label
plt.ylabel("Required water")

plt.title("total number of water needs by individual animal")

plt.xticks(animal,animal_type)
#the xticks format change no format to animal name

plt.bar(animal,required_water,label='required water of animal')  
plt.legend()
plt.show()
    
  