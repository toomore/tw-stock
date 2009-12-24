""" Data property. """
from google.appengine.ext import db

class TSEList(db.Model):
  name = db.StringProperty()
  uindate = db.DateTimeProperty(auto_now_add = True)
