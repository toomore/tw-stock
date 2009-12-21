#!/usr/bin/env python
# -*- coding: utf-8 -*-

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template

from apps import twsk,twsew
import datetime

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
          'test': twsew().weight,
          'twse': twsk(self.request.get('q')).sread
        }
    self.response.out.write(template.render('./template/h_index.htm',{'tv':tv}))

class weightpage(webapp.RequestHandler):
  def get(self):
    tv = {'login': str(datetime.datetime.now() + datetime.timedelta(hours=8))[:-7],
          'twsew': twsew().weight,
        }
    self.response.out.write(template.render('./template/h_weight.htm',{'tv':tv}))

def main():
  """ Start up. """
  application = webapp.WSGIApplication([
                                        ('/', index),
                                        ('/weight', weightpage)
                                      ],debug=True)
  run_wsgi_app(application)

if __name__ == '__main__':
  main()
