#!/usr/bin/env python
# -*- coding: utf-8 -*-

def sread(stock):
  re = {'name': (stock[-1].decode('big5')).encode('utf-8'),
        'no': stock[0],
        'time': stock[2],
        'top': stock[3],
        'down': stock[4],
        'open': stock[5],
        'h': stock[6],
        'l': stock[7],
        'c': stock[8],
        'value': stock[9],
        'pvalue': stock[10],
        'top5buy': {
                    stock[11]: stock[12],
                    stock[13]: stock[14],
                    stock[15]: stock[16],
                    stock[17]: stock[18],
                    stock[19]: stock[20]
                    },
        'top5sell': {
                    stock[21]: stock[22],
                    stock[23]: stock[24],
                    stock[25]: stock[26],
                    stock[27]: stock[28],
                    stock[29]: stock[30]
                    }
        }

  return re
