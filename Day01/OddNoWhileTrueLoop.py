"""
#  Print all the even numbers from 1 to 10 using while True loop

"""

n=1
while(True):
    if(n<=10):
      if(n % 2 !=0):#this statement cheack the reminder is not zero divide by 2 then it is Odd no
         print(n)
         n=n+1
      else:
         n=n+1
         
    else:
      break
     # immediately exit the loop
