import json, csv
from os import write
from time import time
import tweepy

import RSS_format

def connect_to_twitter(key_file_name):
    with open(key_file_name, 'r') as key_file:
        key_data = json.load(key_file)
        consumer_key = key_data[0]['consumer_key']
        consumer_secret = key_data[0]['consumer_secret']

    auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
    api = tweepy.API(auth)
    return auth, api

def get_user_timeline(api, screen_name, no_replies=True, media_only=True, limit=500):
    timeline = list(tweepy.Cursor(api.user_timeline, screen_name=screen_name).items(limit))

    if no_replies:
        timeline = [tweet for tweet in timeline if not tweet.in_reply_to_user_id]

    if media_only:
        timeline = [tweet for tweet in timeline if hasattr(tweet, 'extended_entities')]

    return timeline

def format_to_rss(timeline, screen_name):
    items = []
    for tweet in timeline:
        tweet_url = f'https://twitter.com/twitter/statuses/{tweet.id}'
        if not hasattr(tweet, 'extended_entities'):
            items += [RSS_format.text_only_item_format.format(tweet_text=tweet.text
                                                             ,tweet_link=tweet_url)]
        else:
            items += [RSS_format.media_item_format.format(image_url=tweet.extended_entities['media'][0]['media_url']
                                                         ,tweet_text=tweet.text
                                                         ,tweet_link=tweet_url)]

    user_url = f'https://twitter.com/{screen_name}'
    RSS = RSS_format.document_format.format(screen_name=screen_name
                                           ,user_link=user_url
                                           ,items='\r\n'.join(items))
    return RSS

if __name__ == '__main__':
    _, api = connect_to_twitter('.twitter.json')
    with open('user_list.csv') as user_list:
        user_list = csv.DictReader(user_list, fieldnames = ['screen_name','media_only','no_replies'])
        user_list.__next__()
        for user in user_list:
            screen_name = user['screen_name']
            media_only = user['media_only']
            no_replies = user['no_replies']
            media_only = True if media_only == 'yes' else False
            no_replies = True if no_replies == 'yes' else False

            timeline = get_user_timeline(api=api
                                        ,screen_name=screen_name
                                        ,no_replies=no_replies
                                        ,media_only=media_only)

            RSS = format_to_rss(timeline, screen_name)

            with open(f'RSS_Output_{screen_name}.xml', 'w+', encoding='utf8') as output:
                output.write(RSS)
