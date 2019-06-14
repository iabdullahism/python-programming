"""

Code Challenge
  Name: 
    Fizz Buzz
  Filename: 
    fizzbuzz.py
  Problem Statement:
    Write a Python program which iterates the integers from 1 to 100(included). 
    For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". 
    For numbers which are multiples of both three and five print "FizzBuzz". 
  User Input 
    Not required  
  Output:
    1
    2
    Fizz
    4 
    Buzz  
"""

n=1
while(n<=100):
       if(n % 3 ==0 and n % 5 != 0):
           #this if statement print the number which is divide by 3 and Print "Fizz"
         print("Fizz")
         n=n+1
     
       elif(n % 5 == 0 and n % 3 != 0):
           #this elif statement print the number which is divide by 5 and print "Buzz"
            print("buzz")
            n=n+1
            
       elif(n % 5 == 0 and n % 3 == 0):
           #this if statement print the number which is divide by 3 and 5 or Print "FizzBuzz"
            print("FizzBuzz")
            n=n+1 
        
       else:
         print(n)
         n=n+1
     #when no is Odd go to else loop and increaments by 1
