
"""
Code Challenge
  Name: 
    IGN Analysis
  Filename: 
    ign.py
  Problem Statement:
    Read the ign.csv file and perform the following task :
   
   Let's say we want to find games released for the Xbox One 
   that have a score of more than 7.
   
   review distribution for the Xbox One vs the review distribution 
   for the PlayStation 4.We can do this via a histogram, which will plot the 
   frequencies for different score ranges.
   
   
   
  Hint:

    The columns contain information about that game:

    score_phrase — how IGN described the game in one word. 
                   This is linked to the score it received.
    title — the name of the game.
    url — the URL where you can see the full review.
    platform — the platform the game was reviewed on (PC, PS4, etc).
    score — the score for the game, from 1.0 to 10.0.
    genre — the genre of the game.
    editors_choice — N if the game wasn't an editor's choice, Y if it was. This is tied to score.
    release_year — the year the game was released.
    release_month — the month the game was released.
    release_day — the day the game was released.



xbox_one_filter = (reviews["score"] > 7) & (reviews["platform"] == "Xbox One")
filtered_reviews = reviews[xbox_one_filter]
filtered_reviews.head()
      
%matplotlib inline
reviews[reviews["platform"] == "Xbox One"]["score"].plot(kind="hist")

reviews[reviews["platform"] == "PlayStation 4"]["score"].plot(kind="hist")

filtered_reviews["score"].hist()
        
"""

import pandas as pd
import numpy as np
df=pd.read_csv("ign.csv")


# Or

"""   review distribution for the Xbox One vs the review distribution 
   for the PlayStation 4.We can do this via a histogram, which will plot the 
   frequencies for different score ranges.
"""
#calculate total xbox and playstation 4 in every year
"""
we want to collcet all frequeny of xbox and playstation in yearwise sepereate column
and print total frequency in year and plot graph
"""
xbox_one_filter= df[(df['score'] > 7) &  (df['platform'] == 'Xbox One' )]

          
#xbox_one_filter[['score','platform','release_year']]
"""
p.groupby('release_year')['platform'].value_counts()
this is my own approach
"""
frequeny_xbox_one=xbox_one_filter.groupby(['release_year','platform']).apply(lambda x: len(x))

frequeny_xbox_one_list=list(frequeny_xbox_one.values)
#frequeny_xbox_one_list gives total in evry year of xbox
year_xbox_one_list=list(map(lambda x:x[0],list(frequeny_xbox_one.index)))
#year_xbox_one_lisl gives year
#now calculte the total PlayStation 4 dowloads in every year

PlayStation_filter= df[(df['score'] > 7) & (df['platform'] == 'PlayStation 4' )]
           
#xbox_one_filter[['score','platform','release_year']]

frequeny_PlayStation=PlayStation_filter.groupby(['release_year','platform']).apply(lambda x: len(x))
#frequeny_PlayStation_list total of playstation 4
frequeny_PlayStation_list=list(frequeny_PlayStation)
#year_PlayStation_list gives year download playstation4
year_PlayStation_list=list(map(lambda x:x[0],list(frequeny_PlayStation.index)))

#plot histogram between year and frequency of both playstation and xbox

from matplotlib import pyplot as plt

plt.plot(year_PlayStation_list,frequeny_PlayStation_list,label="play station")
plt.plot(year_xbox_one_list,frequeny_xbox_one_list,label="x box")
plt.xlabel("years")
plt.ylabel("more downloads")
plt.title("the frequencies for different score ranges" )
plt.legend()
plt.show()


