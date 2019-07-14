

"""
Code Challenge
  Name: 
    Book Shop
  Filename: 
    book_shop1.py
  Problem Statement:
    Imagine an accounting routine used in a book shop.
    It works on a list with sublists, which look like this:
        
    Order Number  Book Title  Author Quantity  Price per Item
    34587 Learning Python, Mark Lutz  4 40.95
    98762 Programming Python, Mark Lutz 5 56.80
    77226 Head First Python, Paul Barry 3 32.95
    88112 Einführung in Python3, Bernd Klein  3 24.99    
    
    
    Write a Python program, You need to write a solution without using lambda,map,list comprehension first and then with lambda,map,reduce
    
    A) which returns Order Summary as a list with 2-tuples. 
       Each tuple consists of the order number and the product of the price per items 
       and the quantity. 
    
       The product should be increased by 10 INR if the value of the order is smaller 
    than 100.00 INR.

  Hint: 
    Write a Python program using lambda and map.

  Input:
    orders = [["34587", "Learning Python, Mark Lutz", 4, 40.95], 
              ["98762", "Programming Python, Mark Lutz", 5, 56.80], 
              ["77226", "Head First Python, Paul Barry", 3,32.95],
              ["88112", "Einführung in Python3, Bernd Klein",  3, 24.99]
             ]
  Output:
      [('34587', 163.8), ('98762', 284.0), ('77226', 108.85), ('88112', 84.97)]
      

"""
#without using lambda,map and reduce function
result_list=[]
calculate_list=[]
orders = [["34587", "Learning Python, Mark Lutz", 4, 40.95], 
              ["98762", "Programming Python, Mark Lutz", 5, 56.80], 
              ["77226", "Head First Python, Paul Barry", 3,32.95],
              ["88112", "Einführung in Python3, Bernd Klein",  3, 24.99]
             ]

for order in orders:
    calculate_list.append((order[0],order[2]*order[3]))
  
print(calculate_list)    
for value in calculate_list:
    if value[1]>100:
        result_list.append((value[0],value[1]))
    else:
        p=value[1]+10
        result_list.append((value[0],p))


print(result_list)

#with using lambda redude and filter functions
calculate_list1=list(map(lambda order:(order[0],order[2]*order[3]),orders))
result_list1=list(map(lambda value:(value[0],value[1]) if value[1]>100 else (value[0],value[1]+10),calculate_list1))
print(result_list1)
