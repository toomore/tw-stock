#!/usr/bin/env python
# -*- coding: utf-8 -*-
# http://chart.apis.google.com/chart?chs=20x50&cht=lc&chd=t1:0,0,0|0,55,0|0,50,0|0,40,0|0,35,0&chds=35,55&chm=F,,1,1:4,20
# about big5 http://hoamon.blogspot.com/2008/05/python-big5.html

import urllib2,csv,random,logging
from google.appengine.api import memcache
from google.appengine.api import urlfetch

class twsk:
  def __init__(self,no = None):
    self.stock = ''
    if no is None:
      no = random.randrange(1000,8000)

    ok = 1
    ok_times = 0

    while ok:
      ok = 0
      try:
        page = urllib2.urlopen('http://mis.tse.com.tw/data/%s.csv?r=%s' % (no,random.randrange(1,10000)))
        ok = 0
      except:
        no = random.randrange(1000,8000)
        ok = 1
        ok_times += 1

    logging.info('%s: %s' % (ok_times,no))

    self.oktimes = ok_times

    reader = csv.reader(page)
    for i in reader:
      self.stock = i

  @property
  def sread(self):
    re = {'name': unicode(self.stock[-1], 'cp950'),
          'no': self.stock[0],
          'range': self.stock[1],
          'time': self.stock[2],
          'top': self.stock[3],
          'down': self.stock[4],
          'open': self.stock[5],
          'h': self.stock[6],
          'l': self.stock[7],
          'c': self.stock[8],
          'value': self.stock[9],
          'pvalue': self.stock[10],
          'top5buy': [
            (self.stock[11], self.stock[12]),
            (self.stock[13], self.stock[14]),
            (self.stock[15], self.stock[16]),
            (self.stock[17], self.stock[18]),
            (self.stock[19], self.stock[20])
            ],
          'top5sell': [
            (self.stock[21], self.stock[22]),
            (self.stock[23], self.stock[24]),
            (self.stock[25], self.stock[26]),
            (self.stock[27], self.stock[28]),
            (self.stock[29], self.stock[30])
            ]
          }
    if '-' in self.stock[1]:
      re['ranges'] = False
    else:
      re['ranges'] = True

    re['crosspic'] = "http://chart.apis.google.com/chart?chs=20x40&cht=lc&chd=t1:0,0,0|0,%s,0|0,%s,0|0,%s,0|0,%s,0&chds=%s,%s&chm=F,,1,1:4,20" % (re['h'],re['c'],re['open'],re['l'],re['l'],re['h'])

    re['top5buy'].sort()
    re['top5sell'].sort()
    return re

class twsew:
  def __init__(self):
    self.weight = {}
    page = urlfetch.fetch('http://mis.tse.com.tw/data/TSEIndex.csv?r=%s' % random.randrange(1,10000))
    reader = csv.reader((page.content).split('\r\n'))

    for i in reader:
      if len(i):
        if '-' in i[3]:
          ud = False
        else:
          ud = True
        self.weight[i[0]] = {'no':i[0], 'time':i[1], 'value':i[2], 'range':i[3], 'ud': ud}

    self.weight['200']['v2'] = int(self.weight['200']['value'].replace(',','')) / 100000000

class tsealllists:
  def __init__(self):
    self.list = [
                ('01','水泥工業'),
                ('02','食品工業'),
                ('03','塑膠工業'),
                ('04','紡織纖維'),
                ('05','電機機械'),
                ('06','電器電纜'),
                ('21','化學工業'),
                ('22','生技醫療業'),
                ('08','玻璃陶瓷'),
                ('09','造紙工業'),
                ('10','鋼鐵工業'),
                ('11','橡膠工業'),
                ('12','汽車工業'),
                ('24','半導體業'),
                ('90','封閉式基金'),
                ('99','ETF'),
                ('92','受益證券'),
                ('25','電腦及週邊設備業'),
                ('26','光電業'),
                ('27','通信網路業'),
                ('28','電子零組件業'),
                ('29','電子通路業'),
                ('30','資訊服務業'),
                ('31','其他電子業'),
                ('14','建材營造'),
                ('15','航運業'),
                ('16','觀光事業'),
                ('17','金融保險'),
                ('18','貿易百貨'),
                ('19','綜合'),
                ('23','油電燃氣業'),
                ('20','其他'),
                ('91','存託憑證'),
                ('93','權證(03)'),
                ('94','權證(04)'),
                ('95','權證(05)'),
                ('96','權證(06)'),
                ('97','權證(07)'),
                ('98','權證(08)'),
                ('88','中央登錄公債'),
                ('89','外國債券')
                ]
