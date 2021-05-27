import os
import json
import pyodbc
from connection_info import *

def gather_data(twitter_handle):
    tweets_file_name = 'data/tweets_{}.json'.format(twitter_handle)
    with open(tweets_file_name) as t:
        tweets_json = json.load(t)

    tweets = []
    count = 0
    while 'page_{}'.format(count) in tweets_json:
        if 'data' not in tweets_json['page_{}'.format(count)]:
            break
        page_tweets = tweets_json['page_{}'.format(count)]['data']
        for tweet in page_tweets:
            tweets.append({
                'id': tweet['id'],
                'userid': tweet['author_id'],
                'content': tweet['text'],
                'date': tweet['created_at'],
                'retweet': tweet['public_metrics']['retweet_count'],
                'reply': tweet['public_metrics']['reply_count'],
                'like': tweet['public_metrics']['like_count'],
                'quote': tweet['public_metrics']['quote_count']
            })
        count += 1
    return tweets

if __name__ == '__main__':
    twitter_handles = [17351972, 300114634, 153031349, 21915474, 50883209,
    32171828, 183398746, 752072829278023680, 16252784, 23114836,
    15383636]
    data = []
    for handle in twitter_handles:
        data.append(gather_data(handle))
    
    """ # For local connection
    conn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                        "Server=DESKTOP-R2AJUTJ;"
                        "Database=Info430ProjectDB;"
                        "Trusted_Connection=yes;")
    """
    # For server connections
    conn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    
    cursor = conn.cursor()

    for user in data:
        for tweet_info in user:
            sql_tweet = 'exec [dbo].[insert_tweet] @ID=?, @UserID=?, @Content=?, @Date=?, @Retweet=?, @Reply=?, @Like=?, @Quote=?'
            sql_tweet_values = (tweet_info['id'], tweet_info['userid'], tweet_info['content'], tweet_info['date'],
                                tweet_info['retweet'], tweet_info['reply'], tweet_info['like'], tweet_info['quote'])
            cursor.execute(sql_tweet, (sql_tweet_values))
    
    conn.commit()
    cursor.close()
    