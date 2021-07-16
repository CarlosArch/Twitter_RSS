# Twitter_RSS
Simple proyect to parse a Twitter timeline and serve a RSS feed.

[twitter_parser.py](twitter_parser.py) contains all the logic to parse through a twitter timeline. You can run the file independently to get an XML file for each user inside [user_list.csv](user_list.csv).

[RSS_Hoster](RSS_Hoster/) contains the django proyect to host the RSS feed, you can run it using:
```
python manage.py runserver
```
I used [nssm](http://nssm.cc/) to permanently run the page as a windows service.

## Requirements
This proyect uses [tweepy](https://www.tweepy.org) to parse timelines and [django](https://www.djangoproject.com) to host the RSS feed, you can install both using:
```
pip install -r requirements.txt
```

You also need access to the Twitter API, you can request access through https://developer.twitter.com.
