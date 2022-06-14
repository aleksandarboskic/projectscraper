import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

import django
django.setup()

import requests
from celery import Celery
from bs4 import BeautifulSoup
from djangorest import models
import dateutil.parser as pars

app = Celery('app')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

@app.task
def get_feed_items(provider):
    #urltemplate = "https://feeds.finance.yahoo.com/rss/2.0/headline?s={0}&region=US&lang=en-US".format(provider)    
    urltemplate = os.environ.get("URLTEMPLATE").format(provider)
    item_list = []
    try:
        response = requests.get(urltemplate, headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(response.content, features='xml')
        myitems = soup.findAll('item')
        article = models.Article();
        for itm in myitems:
            article.symbol_name = provider
            article.symbol_item_guid = itm.find('guid').text
            article.symbol_item_description = itm.find('description').text
            article.symbol_item_link = itm.find('link').text
            article.symbol_item_pubdate = pars.parse(itm.find('pubDate').text.strip('\"'))
            article.symbol_item_title = itm.find('title').text
            article.save();    
    except Exception as e:
        print('Job failed. Please see exception:')
        print(e)

@app.task
def scrap_one(provider):
    get_feed_items(provider)

@app.task
def scrap_all():
    listofitems = os.environ.get("FEEDITEMS").split(",")
    for itm in listofitems:
        get_feed_items(itm)
    