#!/usr/bin/python3
'''
    This script contains a function to retrieve the top ten posts for a specified subreddit.
'''
import requests
from sys import argv


def top_ten(subreddit):
    '''
        Retrieves the top ten posts for a given subreddit.
    '''
    user_agent = {'User-Agent': 'Lizzie'}
    url = requests.get('https://www.reddit.com/r/{}/hot/.json?limit=10'
                       .format(subreddit), headers=user_agent).json()
    try:
        for post in url.get('data').get('children'):
            print(post.get('data').get('title'))
    except Exception:
        print(None)


if __name__ == "__main__":
    top_ten(argv[1])

