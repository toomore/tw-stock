#!/usr/bin/env python
# -*- coding: utf-8 -*-

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template
from google.appengine.api import memcache
from google.appengine.api import urlfetch

from apps import twsk,twsew,tsealllists
from datamodel import TSEList
import datetime,csv,urllib2,random,logging

#page = urllib2.urlopen('http://mis.tse.com.tw/data/TSEIndex.csv')
#page = response.read()

#print '123'
#print page

#a = twsk()
#for w in a.sread:
  #print w,a.sread[w]

class index(webapp.RequestHandler):
  """ index page.
  """
  def get(self):
    tv = {'login': str(datetime.datetime.now() + datetime.timedelta(hours=8))[:-7],
          'twse': twsk(self.request.get('q')).sread
        }
    self.response.out.write(template.render('./template/h_index.htm',{'tv':tv}))

class weightpage(webapp.RequestHandler):
  def get(self):
    tv = {'login': str(datetime.datetime.now() + datetime.timedelta(hours=8))[:-7],
          'twsew': twsew().weight,
        }
    self.response.out.write(template.render('./template/h_weight.htm',{'tv':tv}))

class news(webapp.RequestHandler):
  def get(self):
    tv = {'login': str(datetime.datetime.now() + datetime.timedelta(hours=8))[:-7],
          'q': self.request.get('q'),
          'twseno': self.request.get('twseno')
        }
    self.response.out.write(template.render('./template/h_news.htm',{'tv':tv}))

class TseAllList(webapp.RequestHandler):
  def get(self):

    if self.request.get('w'):
      for i in tsealllists().list:
        c,d = i
        TSEList(key_name = c, name = d.decode('utf-8')).put()

    ll = memcache.get('ll')
    if not ll:
      ll = TSEList().all()
      memcache.add('ll',ll,60*5)

    q = []
    for i in ll:
      q.append({'no':(i.key().id_or_name()).encode('utf-8'), 'name':(i.name).encode('utf-8')})

    tv = {'login': str(datetime.datetime.now() + datetime.timedelta(hours=8))[:-7],
          'q': q
        }

    self.response.out.write(template.render('./template/h_twselist.htm',{'tv':tv}))

class TseListPage(webapp.RequestHandler):
  def get(self,twseno):
    '''
    try:
      page = urllib2.urlopen('http://mis.tse.com.tw/data/TC%s.csv?r=%s' % (twseno,random.randrange(1,10000)))

      reader = csv.reader(page)
      e = []
      for i in reader:
        e.append(twsk(i[0]).sread)
    '''
    page = urlfetch.fetch('http://mis.tse.com.tw/data/TC%s.csv?r=%s' % (twseno,random.randrange(1,10000)))
    #reader = csv.reader((page.content).split('\r\n'))
    reader = csv.reader(page.content)

    e = []
    logging.info('s: %s, c:%s' % (page.status_code,page.headers))

    if page.status_code == 404:
      self.redirect('/TseList')
    else:
      try:
        for i in reader:
          if len(i):
            e.append(twsk(i[0]).sread)
        classname = memcache.get(twseno,'classname')
        if classname is None:
          classname = TSEList().get_by_key_name(twseno).name
          memcache.add(twseno,classname,60*3,namespace = 'classname')
          logging.info('Add memcache: %s' % twseno)

        tv = {'login': str(datetime.datetime.now() + datetime.timedelta(hours=8))[:-7],
              'e': e,
              'classname': classname
            }

        self.response.out.write(template.render('./template/h_twselistpage.htm',{'tv':tv}))
      except:
        self.redirect('/TseList')

def main():
  """ Start up. """
  application = webapp.WSGIApplication([
                                        ('/', index),
                                        ('/weight', weightpage),
                                        ('/news', news),
                                        ('/TseList', TseAllList),
                                        ('/TseList/([\w]+)', TseListPage)
                                      ],debug=True)
  run_wsgi_app(application)

if __name__ == '__main__':
  main()
