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


# Loading raw json data into python specific data 
import json
json_string="""
{
    "student":
        {
        "student_name":
            {
            "first_name":"rahul",
            "last_name":"pandit"
            },
        "student_image":"alesa.in/aboutme.html",
        "department":"computer science",
        "Research Areas":
            
              {
              "America":"artificial intelligence",
               "india":"Machine Leraning"
              },
              
           
        "Contact_detail":
             {
             "email_id":["rahulpandit151197@gmail.com","roomseeker98@gmail.com"],
             "phone_no":["7665899329","382y98y9832"],
             "Aadhar_no":"487484899373847894"
             }
        }

}
"""

print (type(json_string))
my_data = json.loads(json_string)
print(my_data)
