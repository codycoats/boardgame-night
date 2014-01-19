from google.appengine.ext import ndb

class Events(ndb.Model):
    title = ndb.StringProperty()
    date = ndb.DateProperty()