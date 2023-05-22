#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests

import requests

def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Custom User Agent"}

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            return data["data"]["subscribers"]
        elif response.status_code == 404:
            return 0
        else:
            print(f"Error: {response.status_code}")
            return 0
    except requests.RequestException as e:
        print(f"Error: {str(e)}")
        return 0
