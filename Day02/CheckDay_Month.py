
# Make a function days_in_month to return
# the number of days in a specific month of a year


import CheckingLeap_year
def CountDay_Month(Month,Year):#Define function
    Month_List1=('january','March','May','July','August','Octomber','December') #create first list whcih contain all 31 days month 
    Month_List2=('April','June','september','November')
  #create second list which contain all 30 days month
    
  
    if(Month in Month_List1 ):
        return "31 Days"
            #Membership Operators 
         # in   ,  not in 
         # Used to check if some single item is in a larger collection  
# Return True if the item is in list

    elif(Month in Month_List2):
        return "30 Days"
    else:
        CheckLeapYear=CheckingLeap_year. Leap_Year(Year)
        if(CheckLeapYear):
          return "29 Days"
        else:
           return "28 Days"
    
    
Month_data=input("enter Month>")
Year_data=int(input("enter Year>"))
    #call the function passing one parameter
Days=CountDay_Month( Month_data, Year_data)
    #When the return the Data Store in Days variable
print(Days)
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    