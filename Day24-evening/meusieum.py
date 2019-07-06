
"""
Q3. 
Data: "data.csv"

This data is provided by The Metropolitan Museum of Art Open Access
1. Visualize the various countries from where the artworks are coming.
2. Visualize the top 2 classification for the artworks
3. Visualize the artist interested in the artworks
4. Visualize the top 2 culture for the artworks
"""
import pandas as pd
import numpy as np

dataset=pd.read_csv("data.csv")
from matplotlib import pyplot

from matplotlib import pyplot as plt
"""
1. Visualize the various countries from where the artworks are coming.
"""
country=dataset['Country'].value_counts()
country_name=list(country.index)
artist_no=list(country.values)
plt.pie(artist_no,labels=country_name,autopct='%.0f%%')
plt.show()

"""
2. Visualize the top 2 classification for the artworks
"""

artworks=dataset['Artist Role'].value_counts().head(2)
print("top 2 artwork",artworks)

"""
3. Visualize the artist interested in the artworks
"""
art=dataset['Artist Role'].value_counts()
art_name=list(art.index)
art_values=list(art.values)


plt.pie(art_values,labels=art_name,autopct='%.0f%%')
plt.show()


"""
4. Visualize the top 2 culture for the artworks
"""
top_culture=dataset['Culture'].value_counts().head(2)
print(top_culture)







