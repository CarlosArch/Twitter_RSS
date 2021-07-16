import csv
from django.shortcuts import render
from django.http import HttpResponse
from twitter_parser import connect_to_twitter, get_user_timeline, format_to_rss

def home(request):
    return render(request, 'templates/home.html')

def feed(request):
    screen_name = request.GET.get('screen_name')
    no_replies = request.GET.get('no_replies')
    media_only = request.GET.get('media_only')
    limit = request.GET.get('limit')

    _, api = connect_to_twitter('.twitter.json')
    timeline = get_user_timeline(api=api
                                ,screen_name=screen_name
                                ,no_replies=no_replies
                                ,media_only=media_only
                                ,limit=limit)

    RSS = format_to_rss(timeline, screen_name)
    return HttpResponse(RSS, content_type='text/xml')

