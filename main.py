#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
import urllib2

page = urllib2.urlopen('http://mis.tse.com.tw/data/%s.csv' % '2456')
#page = urllib2.urlopen('http://mis.tse.com.tw/data/TSEIndex.csv')
#page = response.read()

print '123'
#print page

reader = csv.reader(page)
print reader

for i in reader:
  print i
