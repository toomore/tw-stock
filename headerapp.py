#!/usr/bin/env python
# -*- coding: utf-8 -*-
from google.appengine.ext.webapp import template
import datetime

class Renderer:
  def render(self,header,tempfile,orgvalue):
    tv = {
      'login': str(datetime.datetime.now() + datetime.timedelta(hours=8))[:-7]
    }
    tv.update(orgvalue)
    header.response.out.write(template.render(tempfile,tv))
