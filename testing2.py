
import pandas as pd
import csv
import pandas as pd
import re
from streamz import Stream
from streamz.dataframe import DataFrame
#from streamz.dataframe.core import Reduction
from functools import reduce

df = pd.read_csv(r'C:\Users\user\Downloads\Features.csv')
#file =df[['Id', 'Tweet' , 'Following' , 'Folowers' , 'Actions', 'IS_Retweet' , 'LOcation' , 'Type']]
print('``````````````````````````````````````````  This is the data in file ````````````````````````````````````````````````````` ')
print(df)
print('**************************************part one*******************************************************')
df['actions'] = df['actions'].fillna(0) # fillna replace nan with zeros 
print(df)


print('**************************************part two*******************************************************')
column_name = 'followers'
summation = reduce(lambda x, y: x + y, df[column_name])
print("summation of followers are : " ,summation)

#  It takes two parameters, x and y, representing the accumulated value and 
# the current element of the column, respectively. The lambda function simply adds x and y together.

print('**************************************part three*******************************************************')
uk_tweets = df[df['location'] == 'UK']
print(uk_tweets['Id'])

print('**************************************part four*******************************************************')
spam_count = df[df['Type'] == 'Spam'].shape[0] # note that The .shape[0] attribute returns the number of rows matching the condition.
print("Number of spam tweets:", spam_count)

print('**************************************part five*******************************************************')
followingAbove5k = df[df['following'] > 5000]
print(followingAbove5k['Id'])

print('**************************************part six*******************************************************')
hashtag_tweets = df[df['Tweet'].str.contains('#')]
print(hashtag_tweets['Id'])

print('**************************************part seven*******************************************************')
pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'

# Filter the DataFrame and extract the tweet IDs
url_tweets = df[df['Tweet'].str.contains(pattern, flags=re.IGNORECASE, regex=True)]
tweet_ids = url_tweets['Id']
for tweet_id in tweet_ids:
    print(tweet_id)
