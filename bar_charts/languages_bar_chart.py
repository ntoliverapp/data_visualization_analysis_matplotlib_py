import pandas as pd
import csv
import matplotlib.pyplot as plt
from collections import Counter
import numpy as np

data = pd.read_csv('data.csv')
ids = data['Responder_id']
lan_responses = data['LanguagesWorkedWith']



# with open('data.csv') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
    
    # row = next(csv_reader)
    # print(row)
    # print(row['LanguagesWorkedWith'])
    # print(row['LanguagesWorkedWith'].split(';'))
    
language_counter = Counter()
    
for response in lan_responses:
    language_counter.update(response.split(';'))
    
    # for row in csv_reader:
    #     language_counter.update(row['LanguagesWorkedWith'].split(';'))
        
    # print(language_counter.most_common(15))
    
# want languages on one axis and popularity on y axis 

languages = []
popularity = []

for item in language_counter.most_common(15): #looping over a list of tuples
    languages.append(item[0])
    popularity.append(item[1])   
 
# print(languages)
# print(popularity)   

languages.reverse()
popularity.reverse()

plt.barh(languages, popularity)

plt.title('Most Popular Languages')
plt.xlabel('Language Name')
plt.ylabel('Total count per lang.')

plt.tight_layout()

plt.savefig('languages_bar.png')
plt.show()
    

    
   
    
    