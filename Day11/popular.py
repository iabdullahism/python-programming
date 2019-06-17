

"""
Code Challenge ( Bar Plot )
  Name: 
    Most Popular Programming Language out of 28 Languages
  Filename: 
    popular.py
  Problem Statement:
    Read the bardata.csv file
    It has a the survey of 87,570 people at the StackOverFlow Annual Developer Day
    The data has two parts
      1) ID of the Responser
      2) Semicolon seperated data of the languages known by them
    
    We need to now read the csv file using the csv reader and create a dictionary 
    This dictionary should store the Language as the key and value as the number 
    of times the responder has voted for it.
    
    Now display the data in the form of Horizontal Bar Chart to show the popularity of the 
    top 10 languages and the votes from the developer 

  Hint:
      Use the concept of DictReader from csv 
      Also use the concept of Counter class from collections 
      and update it for each row of data
      
      with open ('data.csv') as csv_reader :
          csv_reader = csv.DictReader()
          
          language_counter = Counter()
          
          for row in csv_reader:
              language_counter.update(row['LanguageWorkedWith'].split(';'))
      
      # You could have used the zip function here 
      print(language_counter.most_common(10))
      languages=[]
      popularity=[]
      for item i language_counter.most_common(10):
          languages.append(item[0])
          popularity.append(item[1])
                 
"""
i=0
import csv
lang_dict={}
top_lang=[]
vote=[]
with open("bardata.csv") as file:
    file_reader=csv.reader(file,delimiter = ',')
    next(file_reader)
    for data in file_reader:
        language_list=data[1].split(";")
        for language in language_list:
            if language in lang_dict:
                lang_dict[language]+=int(1)
            else:
                lang_dict[language]=int(1)


top_language=sorted(lang_dict.items(), key= lambda x:x[1])

for record in top_language:
    top_lang.append(record[0])
    vote.append(int(record[1]))
    
    
