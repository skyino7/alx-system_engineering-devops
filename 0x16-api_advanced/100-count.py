#!/usr/bin/python3
"""recursive function that queries the Reddit API,
parses the title of all hot articles,
and prints a sorted count of given keywords
(case-insensitive, delimited by spaces. """

import requests


def count_words(subreddit, word_list, after=None, word_count={}):
    """Recursive function that queries the Reddit API,
    parses the title of all hot articles,
    and prints a sorted count of given keywords
    (case-insensitive, delimited by spaces. """

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
        title = post.get('data').get('title').lower().split()
        for word in word_list:
            if word.lower() in title:
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1

    if after is not None:
        return count_words(subreddit, word_list, after, word_count)

    if len(word_count) == 0:
        return

    for k, v in sorted(word_count.items(), key=lambda item: item[1],
                       reverse=True):
        print('{}: {}'.format(k, v))
