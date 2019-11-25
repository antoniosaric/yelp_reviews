# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
import sqlite3
import urllib2
import requests
from bs4 import BeautifulSoup
import time



from django.shortcuts import render
 
import paralleldots
 
def home(request):
    user_sent=""
    user_input=""
    fname="na"
    if request.POST:
       user_input=request.POST.get('user_input', '')
       lang_code="en"
       paralleldots.set_api_key("NlxGNPr4VRsjdyORAdKFWWraVX2HNGdBw0JUXCJ9uYg")
       user_response=paralleldots.sentiment(user_input,lang_code)
       user_sent=user_response['sentiment']
 
       if (user_sent == 'neutral'):
             fname=  "emoticon-1634586_640.png"
       elif (user_sent == 'negative'):
             fname = "emoticon-1634515_640.png"
       elif (user_sent == 'positive'):
             fname = "smiley-163510_640.jpg"
       else:
             fname="na"
 
    return render(request, 'jack/home.html', {'resp': user_sent, 'fname':fname, 'user_input':user_input})




# reviews = ['helllllo']

# def home(request):
# 	context = {
# 		'reviews': reviews
# 	}
# 	return render(request, 'jack/home.html', context)




