#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
import sys

f = open(sys.argv[1], 'rt')

try:
 reader = csv.reader(f)
 for row in reader:
   print row
finally:
 f.close()
