
"""
Code Challenge
  Filename: 
    height.py
  Problem Statement:

      people = [{'name': 'Mary', 'height': 160},
                {'name': 'Isla', 'height': 80},
                {'name': 'Sam'}]

    height_total = 0
    height_count = 0
    for person in people:
        if 'height' in person:
            height_total += person['height']
            height_count += 1

    if height_count > 0:
        average_height = height_total / height_count

        print (average_height)
    
Try rewriting the code below using map, reduce and filter. 
Filter takes a function and a collection. 
It returns a collection of every item for which the function returned True.
    

"""
from functools import reduce
mydict={}
people = [{'name': 'Mary', 'height': 160},
                {'name': 'Isla', 'height': 80},
                {'name': 'Sam'}]


my_filter_list = list(filter ( lambda x:'height' in x, people))
print(my_filter_list)   
map_list=list(map(lambda n:n['height'],my_filter_list)) 
sumMylist=reduce(lambda x,y:x+y,map_list)
avarageMylist=sumMylist/len(map_list)
print(avarageMylist)
