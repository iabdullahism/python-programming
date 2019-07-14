

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
import csv
import matplotlib.pyplot as plt

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

i=len(top_language)-10

for p in top_language[i:]:
    top_lang.append(p[0])
    vote.append(p[1])
#make a range index list to display language
index=[]
k=0
for i in range(len(top_lang)):
    index.append(k)
    k=k+1
    
plt.bar(index, vote)
plt.xlabel('programming language', fontsize=10)
plt.ylabel('rank and votes', fontsize=10)
plt.xticks(index, top_lang, fontsize=10, rotation=45)
plt.title('Top 10 programming language')
plt.show()







    