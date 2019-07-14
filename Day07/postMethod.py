# Code Challenge

"""
Research the below wesbite and post some data on it
https://requestbin.com
"""
import requests
import json

Host="https://ena3sd52t8o66.x.pipedream.net/"
data = {"firstname":"rahulpandit","language":"English"}

headers = {"Content-Type":"application/json","Content-Length":len(data),"data":json.dumps(data)}

def post_method():
    response = requests.post(Host,data,headers)
    return response

print ( post_method().text )


def get_method():
    response = requests.get("https://ena3sd52t8o66.x.pipedream.net/get?firstname=Dev&language=English")
    return response

print (get_method().text)

