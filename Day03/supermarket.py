
"""
Code Challenge
  Name: 
    Supermarket
  Filename: 
    supermarket.py
  Problem Statement:
    You are the manager of a supermarket. 
    You have a list of items together with their prices that consumers bought on a particular day. 
    Your task is to print each item_name and net_price in order of its first occurrence. 
    Take Input from User  
  Hint: 
    item_name = Name of the item. 
    net_price = Quantity of the item sold multiplied by the price of each item.
    try to use new class for dictionary : OrderedDict
  Input:
    BANANA FRIES 12
    POTATO CHIPS 30
    APPLE JUICE 10
    CANDY 5
    APPLE JUICE 10
    CANDY 5
    CANDY 5
    CANDY 5
    POTATO CHIPS 30
  Output:
    BANANA FRIES 12
    POTATO CHIPS 60
    APPLE JUICE 20
    CANDY 20

"""

# Taking multiple input from user
my_dict ={}
     
while(True):
     user_input = input("Enter Fruits-name and price: ")
 
     value = user_input.split(" ")
     #split all the contents in one string
     if user_input:
         if ' '.join(value[:-1]) not in my_dict:
             #connect two charactor into one and remove last values using[:-1]
             my_dict[' '.join(value[:-1])]=int(value[-1])
             #add into dictonary key and values
         else:
             my_dict[' '.join(value[:-1])]=int(my_dict[' '.join(value[:-1])])+int(value[-1])
              # if my_dict[' '.join(value[:-1])] we focasting into integer then it will give values
              #of key
        
     if not user_input:
         break
     
        




