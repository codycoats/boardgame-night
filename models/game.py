from google.appengine.ext import ndb

class Game(ndb.Model):
    title = ndb.StringProperty()
    minPlayers = ndb.StringProperty()
    maxPlayers = ndb.StringProperty()
    votes = ndb.IntegerProperty(default=0)
    voters = ndb.UserProperty(repeated=True)