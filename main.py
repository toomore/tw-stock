#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
import urllib2
import apps

page = urllib2.urlopen('http://mis.tse.com.tw/data/%s.csv' % '2456')
#page = urllib2.urlopen('http://mis.tse.com.tw/data/TSEIndex.csv')
#page = response.read()

print '123'
#print page

reader = csv.reader(page)

for i in reader:
  print i
  a = apps.sread(i)
  print a
