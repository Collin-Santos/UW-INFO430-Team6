import requests
import os
import json
import time

from requests.api import request

# Set 1
twitter_handles = [17351972, 300114634, 153031349, 21915474, 50883209,
    32171828, 183398746, 752072829278023680, 16252784, 23114836,
    15383636]

def auth():
    return os.environ.get("BEARER_TOKEN")

def create_url():
    user_id = 17351972
    tweet_fields = "tweet.fields=author_id,created_at,public_metrics"
    exclude = "exclude=retweets,replies"
    max_results = "max_results=100"
    return "https://api.twitter.com/2/users/{}/tweets?{}&{}&{}".format(user_id, tweet_fields, exclude, max_results)

def paginated_url(next_page_token):
    user_id = 17351972
    tweet_fields = "tweet.fields=author_id,created_at,public_metrics"
    exclude = "exclude=retweets,replies"
    max_results = "max_results=100"
    pagination = "pagination_token={}".format(next_page_token)
    return "https://api.twitter.com/2/users/{}/tweets?{}&{}&{}&{}".format(user_id, tweet_fields, exclude, max_results, pagination)

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
    url = create_url()
    headers = create_headers(bearer_token)

    # First Response
    json_response = connect_to_endpoint(url, headers)

    # Store First
    page_count = 0
    container = {}
    container["page_{}".format(page_count)] = json_response
    
    print("Page {} Grabbed".format(page_count))
    time.sleep(15)

    # Pull first next token
    has_next_token = True
    try:
        next_token = json_response["meta"]["next_token"]
    except:
        print("Single Page Only")
        has_next_token = False

    # Iterate pages
    while has_next_token and page_count < 10:
        # Query
        next_url = paginated_url(next_token)
        next_response = connect_to_endpoint(next_url, headers)
        page_count += 1
        container["page_{}".format(page_count)] = next_response

        print("Page {} Grabbed".format(page_count))
        time.sleep(15)

        try:
            next_token = next_response["meta"]["next_token"]
        except:
            print("Reached End of Request")
            has_next_token = False

    with open('test_output_tweets_2.json', 'w') as outfile:
        json.dump(container, outfile)

if __name__ == "__main__":
    main()