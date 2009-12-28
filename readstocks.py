#!/usr/bin/env python
# -*- coding: utf-8 -*-

from google.appengine.api import memcache
from google.appengine.api import urlfetch
from datamodel import *
from random import randrange
import logging,csv

def getTSEkey():
  TE = TSEList()
  count = memcache.get('count','TSEkey')
  if count is None:
    count = TE.all().count()
    memcache.add('count', count, namespace = 'TSEkey')
    logging.info('Add cache: TSEkey')

  TEall = memcache.get('TEall','TSEkey')
  if TEall is None:
    TEall = TE.all()
    memcache.add('TEall', TEall, namespace = 'TSEkey')
    logging.info('Add cache: TEall')

  for a in TEall.fetch(1,randrange(0,count)):
    return a.key().id_or_name(),a.key()

#print '123'
a,b = getTSEkey()
#print a,b

page = urlfetch.fetch('http://mis.tse.com.tw/data/TC%s.csv?r=%s' % (a,randrange(1,10000)))
reader = csv.reader(page.content)

for s in reader:
  if len(s):
    TSEStocks(key_name = s[0], TSELRef = b).put()
    logging.info('Add data: %s-%s' % (a,s[0]))
