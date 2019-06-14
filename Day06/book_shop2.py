

"""
Code Challenge
  Name: 
    Book Shop
  Filename: 
    book_shop2.py
  Problem Statement:
    The same bookshop, but this time we work on a different list.
    
    The sublists of our lists look like this:
    [ordernumber, (article number, quantity, price per unit), 
    ... (article number, quantity, price per unit) ]
       
    [ [1, ("5464", 4, 9.99), ("8274",18,12.99), ("9744", 9, 44.95)], 
      [2, ("5464", 9, 9.99), ("9744", 9, 44.95)],
      [3, ("5464", 9, 9.99), ("88112", 11, 24.99)],
      [4, ("8732", 7, 11.99), ("7733",11,18.99), ("88112", 5, 39.95)] ]
    
   Write a program which returns a list of list with 
    [order number, total amount of order].
    
   Write a Python program, You need to write a solution without 
   using lambda,map,list comprehension first and then with lambda,map,reduce
      
  Hint: 
    use lambda, map and reduce concept to solve the problem  
    from functools import reduce
    
  Input:
      orders = [ [1, ("5464", 4, 9.99), ("8274",18,12.99), ("9744", 9, 44.95)], 
                 [2, ("5464", 9, 9.99), ("9744", 9, 44.95)],
                 [3, ("5464", 9, 9.99), ("88112", 11, 24.99)],
                 [4, ("8732", 7, 11.99), ("7733",11,18.99), ("88112", 5, 39.95)] 
               ]
     
  Output:
       [[1, 678.33], [2, 494.46], [3, 364.8], [4, 492.57]]     

"""


#without using lambda function

orders = [ ['1', ("5464", 4, 9.99), ("8274",18,12.99), ("9744", 9, 44.95)], 
         ['2', ("5464", 9, 9.99), ("9744", 9, 44.95)],
         ['3', ("5464", 9, 9.99), ("88112", 11, 24.99)],
         ['4', ("8732", 7, 11.99), ("7733",11,18.99), ("88112", 5, 39.95)] ]


bookshop=[]
for order in orders:
    order_no=order[0]
    info=order[1:]
    value=0
    for amount in info:
        value=value+float(amount[1])*float(amount[2])
        
    bookshop.append([order_no,value])
print(bookshop)

#with using lambda function

from functools import reduce
min_order = 100
#index list gives index and all multiply of items and price in each list
index = list(map(lambda order:[order[0]]+list(map(lambda y:y[1]*y[2],order[1:])), orders))
print(index)
#value list gives the total of price in each list of index
value =list(map(lambda value:[value[0]]+[round(reduce(lambda x,y:x+y,value[1:]))],index))
print(list(value))
#if the value of price is less 100 then it increase by 10rs.
bookshop=list(map(lambda x:x if x[1]>=min_order else (x[0],x[1]+10),value))


  