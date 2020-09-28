from django.shortcuts import render
from django.http import HttpResponse
import requests
from .models import Greeting
import os
import tweepy

APP_KEY = 'V4mkmenWVWeZimYcK9jzWBS0F'
APP_SECRET = 'RUyMKeZzonXUWY9PdfytLBBVI4LqgAYiSUGSRLYW0xQMsh3RmP'
BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAAd5IAEAAAAABg3CZmaU1d01gnBfLwgBaqazPvc%3D5WcoGYXGLD3uJKMoWDpt3rczZYw9a0eYLtvG1pYM0QOXXm9sVo'
ACCESS_TOKEN = '39713422-4zTBRtTp1WvwxtvsBdaeb2xsPaVOhW5Fzx12woBts'
ACCESS_TOKEN_SECRET = 'yNUQeakiGq33istzn4RZAHG7Y6QvQtvC21rfxqGJX53mE'

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    # return render(request, "index.html")
    # r = requests.get('http://httpbin.org/status/418')
    # print(r.text)
    # return HttpResponse('<pre>' + r.text + '</pre>')
    # times = int(os.environ.get('TIMES',3))
    # return HttpResponse('Hello! ' * times)
    
    auth = tweepy.OAuthHandler(APP_KEY, APP_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth)
    status = api.update_status('Welcome1234 !!!')
    return HttpResponse(str(status.created_at))

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
