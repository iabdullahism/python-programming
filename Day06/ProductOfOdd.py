"""
This Python function accepts a list of numbers and computes the product of all the odd numbers:

def productOfOdds(list):
    result = 1
    for i in list:
        if i % 2 == 1:
            result *= i
    return result
    
Rewrite the Python code using map, filter, and reduce:

def productOfOdds(list):
    return reduce(r_func, filter(f_func, map(m_func, list)))

    
"""


from functools import reduce

user_input=input("enter the number by comma seperate..>").split(" ")
My_list=list(user_input)
    
Odd_list=list(filter(lambda x:int(x)%2!=0,My_list))
print("odd_no list-",Odd_list)
Product_odd=reduce(lambda x,y:int(x)*int(y),Odd_list)
print("Product of odd no..",Product_odd)
