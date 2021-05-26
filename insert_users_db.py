import os
import json
import pyodbc

user_file_name = 'data/users.json'

with open(user_file_name) as u:
    users_json = json.load(u)


user_info = []

for user in users_json['data']:
    verify = 1 if user['verified'] else 0
    loc = user['location'] if 'location' in user else None
    user_info.append({
        'id': user['id'],
        'name': user['name'],
        'handle': user['username'],
        'link': user['url'],
        'location': loc,
        'date': user['created_at'],
        'description': user['description'],
        'verified': verify,
        'followers': user['public_metrics']['followers_count'],
        'following': user['public_metrics']['following_count'],
        'tweet': user['public_metrics']['tweet_count'],
        'listed': user['public_metrics']['listed_count']
    })


conn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=DESKTOP-R2AJUTJ;"
                      "Database=Info430ProjectDB;"
                      "Trusted_Connection=yes;")

cursor = conn.cursor()
for itm in user_info:
    sql_user = 'exec [dbo].[insert_user] @ID=?, @Name=?, @Handle=?, @Link=?, @Location=?, @Date=?, @Description=?, @Verified=?, @Followers=?, @Following=?, @TweetCount=?, @Listed=?'
    sql_user_values = (itm['id'], itm['name'], itm['handle'], itm['link'],
                    itm['location'], itm['date'], itm['description'], itm['verified'],
                    itm['followers'], itm['following'], itm['tweet'], itm['listed'])
    cursor.execute(sql_user, (sql_user_values))
conn.commit()
cursor.close()
