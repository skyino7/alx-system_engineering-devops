#!/usr/bin/python3
"""recursive function that queries the Reddit API and
returns a list containing the titles of all hot articles
for a given subreddit"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """Recursive function that queries the Reddit API and
    returns a list containing the titles of all hot articles
    for a given subreddit."""

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'limit': 100, 'after': after}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return None

    hot_posts = response.json().get('data').get('children')
    after = response.json().get('data').get('after')

    for post in hot_posts:
        hot_list.append(post.get('data').get('title'))

    if after is not None:
        return recurse(subreddit, hot_list, after)
    return hot_list
