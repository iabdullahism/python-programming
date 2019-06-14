
"""
Code Challenge
  Name: 
    Currency Converter Convert  from USD to INR
  Filename: 
    currecncyconv.py
  Problem Statement:
    You need to fetch the current conversion prices from the JSON  
    using REST API
  Hint:
    http://free.currencyconverterapi.com/api/v5/convert?q=USD_INR&compact=y
    Check with http://api.fixer.io/latest?base=USD&symbol=EUR&appid=103455d127aaaae6c530
    
"""

import requests
url="https://free.currconv.com/api/v7/convert?q=USD_INR&compact=ultra&apiKey=103455d127aaaae6c530"
print(url)
#get data using send url this data is json format
send = requests.get(url)
jsondata1=send.json()
print(jsondata1)

