#!/usr/bin/env python
# -*- coding: utf-8 -*-

from apps import twsk
from datamodel import TSEStocks
import logging

print '123'
a = TSEStocks.gql('where name = null limit 5')
print a.count()
for i in a:
  tk = twsk(i.key().id_or_name())
  if tk.oktimes == 0:
    name = tk.sread['name']
    data = TSEStocks.get_by_key_name(i.key().id_or_name())
    data.name = name
    data.put()
    logging.info('Add stock name: %s %s' % (i.key().id_or_name(),name))
