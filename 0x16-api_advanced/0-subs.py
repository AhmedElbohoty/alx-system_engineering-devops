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

    if subreddit is None:
        return 0

    if not isinstance(subreddit, str):
        return 0

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    allow_redirects = False
    timeout = 5000

    try:
        response = requests.get(url, headers=headers,
                                allow_redirects=allow_redirects,
                                timeout=timeout)

        if response.status_code != 200:
            return None

        data = response.json().get('data')

        if data is None:
            return None

        if data.get("subscribers") is None:
            return 0

        return data.get("subscribers")

    except Exception:
        return 0
