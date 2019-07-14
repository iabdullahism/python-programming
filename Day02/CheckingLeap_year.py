
# Make a function to find whether a year is a leap year or no, return True or False 


#Defining the function with argument and default


 
def Leap_Year(Year_Data):  #Defining function With one argument
  if((Year_Data % 4==0) and (Year_Data % 100 !=0)):
      #if value of year is divisible by 4 and not divisible by 100 then it is a leap year
    return True 
       #if condition true return value true
  elif(Year_Data % 400 == 0):
      #if value of year is divisible by 400 then it is leap year
      return True
    #if condition true  return value true
  else:
      return False
      #if condition False  return value false

    


Year_Data=int(input("enter Year>"))
#call the function by passing one argument
My_Leap_Year=Leap_Year(Year_Data)
print ( My_Leap_Year) 