#!/usr/bin/python3
'''
    This script contains a function to retrieve the number of subscribers for a specified subreddit.
'''
import requests
from sys import argv


def number_of_subscribers(subreddit):
    '''
        Retrieves the number of subscribers for a given subreddit.
    '''
    user_agent = {'User-Agent': 'Lizzie'}
    url = requests.get('https://www.reddit.com/r/{}/about.json'
                       .format(subreddit), headers=user_agent).json()
    try:
        return url.get('data').get('subscribers')
    except Exception:
        return 0


if __name__ == "__main__":
    number_of_subscribers(argv[1])

