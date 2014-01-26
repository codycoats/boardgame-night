from google.appengine.ext import ndb

class Profile(ndb.Model):
    user = ndb.UserProperty()
    info = ndb.StringProperty(default="Lorem ipsum dolor semit...")
    bggProfile = ndb.StringProperty(default="")