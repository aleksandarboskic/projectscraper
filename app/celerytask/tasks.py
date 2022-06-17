import requests
from bs4 import BeautifulSoup
from djangorest import models
import dateutil.parser as pars
from .celery import cel
import os

@cel.task
def get_feed_items(provider):
    urltemplate = os.environ.get("URLTEMPLATE").format(provider)
    try:
        response = requests.get(urltemplate, headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(response.content, features='xml')
        myitems = soup.findAll('item')
        article = models.Article()
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

@cel.task
def scrap_one(provider):
    get_feed_items(provider)

@cel.task
def scrap_all():
    listofitems = os.environ.get("FEEDITEMS").split(",")
    for itm in listofitems:
        get_feed_items(itm)
    