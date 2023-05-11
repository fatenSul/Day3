
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
print(df)
print('**************************************part one*******************************************************')
df['actions'] = df['actions'].fillna(0)
print(df)





# Read the CSV file into a DataFrame
df = pd.read_csv(r'C:\Users\user\Downloads\Features.csv')

# Define the column name to compute the summation
column_name = 'followers'

# Apply the reduction function to compute the summation
summation = reduce(lambda x, y: x + y, df[column_name])

# Print the summation
print("summation of followers are : " ,summation)


uk_tweets = df[df['location'] == 'UK']

# Print the tweet IDs
print(uk_tweets['Id'])

Spam_count=0

spam_count = df[df['Type'] == 'Spam'].shape[0]

# Print the spam count
print("Number of spam tweets:", spam_count)


followingAbove5k = df[df['following'] > 5000]

print(followingAbove5k['Id'])


hashtag_tweets = df[df['Tweet'].str.contains('#')]
print(hashtag_tweets['Id'])



# Define the regex pattern to match URLs
pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'

# Filter the DataFrame and extract the tweet IDs
url_tweets = df[df['Tweet'].str.contains(pattern, flags=re.IGNORECASE, regex=True)]
tweet_ids = url_tweets['Id']

# Print the tweet IDs
for tweet_id in tweet_ids:
    print(tweet_id)
