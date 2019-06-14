#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Code Challenge 2
Perform similar steps as in the above code challenge but store the contents in 
an online mongo atlas database.

"""
import dns
import pymongo
client = pymongo.MongoClient("mongodb+srv://rahulpandit:rahulpandit123@cluster0-e2nbu.mongodb.net/test?retryWrites=true&w=majority")
mydb = client.roomseeker
#database name
def add_employee(idd, first, last, pay):
    unique_employee = mydb.employees.find_one({"id":idd})
    #if unique_employee:
    #    return "Employee already exists"
    #else:
    mydb.python123.insert_one(
            {
            "id" : idd,
            "first" : first,
            "last" : last,
            "pay" : pay
            })
    return "Employee added successfully"



#for insert data we have to make function
add_employee(1,'Sylvester', 'Fernandes', '50000')
add_employee(2,'Yogendra', 'Singh', 70000)
add_employee(3,'Rohit', 'Mishra', 30000)
add_employee(4,'Kunal', 'Vaid', 30000)
add_employee(5,'Devendra', 'Shekhawat', 30000)

#and also get the data from database we alse make a function
def fetch_all_employee():
    user = mydb.python123.find()
    for i in user:
        print (i)
        
fetch_all_employee()        