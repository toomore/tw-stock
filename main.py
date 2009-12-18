#!/usr/bin/env python
# -*- coding: utf-8 -*-

from apps import twsk

#page = urllib2.urlopen('http://mis.tse.com.tw/data/TSEIndex.csv')
#page = response.read()

print '123'
#print page

a = twsk().sread
for w in a:
  print w,a[w]
