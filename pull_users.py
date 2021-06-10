# Connects and requests user data from designated users utilizing the Twitter API
# Dumps JSON information into sperated files.

import requests
import os
import json
import time

from requests.api import request

# Note: Twitter API keys must be exported into the environment before execution
# Consult Twitter API devoloper documention for additional information

# Set 1
twitter_handles = [17351972, 300114634, 153031349, 21915474, 50883209,
    32171828, 183398746, 752072829278023680, 16252784, 23114836,
    15383636]

def auth():
    return os.environ.get("BEARER_TOKEN")

def create_url(handles):
    user_ids = ','.join(map(str, handles))
    user_fields = 'user.fields=created_at,description,id,location,name,public_metrics,url,username,verified'
    return "https://api.twitter.com/2/users?ids={}&{}".format(user_ids, user_fields)

def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers

def connect_to_endpoint(url, headers):
    response = requests.request("GET", url, headers=headers)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()

def main():
    # Establish connection
    bearer_token = auth()
    headers = create_headers(bearer_token)

    # Url creation
    url = create_url(twitter_handles)
    print("Grabbing pages for users")

    # First Response
    json_response = connect_to_endpoint(url, headers)
    
    print("Users Grabbed")

    with open('data/users.json', 'w') as outfile:
        json.dump(json_response, outfile, indent=2)

if __name__ == "__main__":
    main()