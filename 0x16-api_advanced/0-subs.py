#!/usr/bin/python3

"""
Module: number_of_subscribers

This module provides a function to query the Reddit API and retrieve the number of subscribers for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Retrieve the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers for the subreddit.
             If the subreddit is invalid or an error occurs during the request, 0 is returned.
    """

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
