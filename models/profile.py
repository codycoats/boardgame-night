from google.appengine.ext import ndb

class Profile(ndb.Model):
    user = ndb.UserProperty()
    info = ndb.StringProperty()
    bggProfile = ndb.StringProperty()