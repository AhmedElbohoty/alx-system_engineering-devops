#!/usr/bin/python3
"""
Write a function that queries the Reddit API and returns the number of
subscribers (not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0.
"""
import requests


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) to the subreddit

    Args:
        subreddit(string): the subreddit name

    Returns:
        numbers(number): the number of subscribers.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    if subreddit is None:
        return 0

    if not isinstance(subreddit, str):
        return 0

    headers = {"User-Agent": "Chrome"}

    try:
        response = requests.get(url, headers=headers,
                                timeout=5000, allow_redirects=False)

        if response.status_code == 200:
            data = response.json()
            return data.get("data").get("subscribers")
        else:
            return 0
    except Exception:
        return 0
