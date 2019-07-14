"""

Code Challenge
  Name: 
    Student and Faculty JSON
  Filename: 
    student.json
    faculty.json
  Problem Statement:
    Create a student and Faculty JSON object and get it verified using jsonlint.com
    Write a JSON for faculty profile. 
    The JSON should have profile of minimum 2 faculty members. 
    The profile for each faculty should include below information atleast:

        First Name
        Last Name
        Photo (Just a random url)
        Department 
        Research Areas (can be multiple)
        Contact Details (should include phone number and email id and can have multiple )
   Hint:
       www.jsonlint.com
       
"""


# Converts  JSON Data types to Python Data Types 

# Loading raw json data into python specific data 
import json
json_string="""
{
  "Faculty":
      {
      "Faculty_name":
          {
          "fist_name":"Vikas",
          "last_name":"jain"
          },
      "Faculty_image":"www.google.com/ndnojew.jpg",
      "Department":"computer_science",
      "Research_Areas":
          {
          "StanFord_University":"machine_learning",
          "Oxford_university":"Data_minig"
          },
       "Faculty_Contact_detail":
          {
          "email":["rahulpandit151197@gmail.com","oxfordvikas@gmail.com"],
          "Mobile_no":["798369847","82798237439823"],
          "Aadhar_card_no":"8903327420"
          }
      }
}
"""
print(type(json_string))
my_data=json.loads(json_string)
print(my_data)