from google.appengine.ext import ndb

class Game(ndb.Model):
    title = ndb.StringProperty()
    minPlayers = ndb.IntegerProperty()
    maxPlayers = ndb.IntegerProperty()
    votes = ndb.IntegerProperty()
    voters = ndb.UserProperty(repeated=True)