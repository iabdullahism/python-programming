"""
Hands On 1
"""
# Create a list of number from 1 to 20 using range function. 
# Using the slicing concept print all the even and odd numbers from the list 

My_list=[]
#decleare empty list
My_list = list(range(20))
#range function print list into given range
print (type(My_list))
#type function print type of object
print (My_list)

for number in My_list:
  if number % 2 == 1:  # if the number is odd
    continue       # don't process and skip to next iteration
  print(number)
print("done")
