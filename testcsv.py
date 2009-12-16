#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
import sys
import urllib2

#f = open(sys.argv[1], 'rt')
f = urllib2.urlopen('http://mis.tse.com.tw/data/%s.csv' % '2456')

try:
 reader = csv.reader(f)
 for row in reader:
   print row
finally:
 f.close()
