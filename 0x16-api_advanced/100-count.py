#!/usr/bin/env python3

"""

Recursive Function to Count Keywords in Reddit API

This script defines a recursive function that queries the Reddit API, parses the titles of hot articles in a given

subreddit, and prints a sorted count of given keywords.

Author: OpenAI (modified by [Your Name])

"""

import requests

def count_words(subreddit, word_list, after=None, count_dict=None):

    """

    Count occurrences of keywords in the titles of hot articles in a given subreddit.

    Args:

        subreddit (str): The name of the subreddit to search.

        word_list (list): A list of keywords to count.

        after (str): The identifier of the last processed post (used for pagination).

        count_dict (dict): A dictionary to store the counts of keywords.

    Returns:

        dict: A dictionary containing the counts of keywords.

    Raises:

        None

    """

    if count_dict is None:

        count_dict = {}

    headers = {'User-Agent': 'Mozilla/5.0'}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    params = {'limit': 100, 'after': after}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:

        data = response.json()

        posts = data['data']['children']

        if len(posts) == 0:

            return count_dict

        for post in posts:

            title = post['data']['title']

            title_words = title.lower().split()

            for word in word_list:

                count_dict[word] = count_dict.get(word, 0) + title_words.count(word.lower())

        after = data['data']['after']

        return count_words(subreddit, word_list, after, count_dict)

    else:

        return count_dict

def print_results(count_dict):

    """

    Print the counts of keywords in descending order.

    Args:

        count_dict (dict): A dictionary containing the counts of keywords.

    Returns:

        None

    Raises:

        None

    """

    sorted_counts = sorted(count_dict.items(), key=lambda x: (-x[1], x[0]))

    for word, count in sorted_counts:

        print(f"{word.lower()}: {count}")

if __name__ == "__main__":

    # Example usage:

    subreddit = "python"

    word_list = ["python", "reddit", "api"]

    count_dict = count_words(subreddit, word_list)

    print_results(count_dict)

