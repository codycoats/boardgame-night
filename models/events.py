from google.appengine.ext import ndb

class Events(ndb.Model):
    title = ndb.StringProperty()
    date = ndb.DateProperty()
    host = ndb.UserProperty(required=True)
    attendees = ndb.UserProperty(repeated=True)
    games = ndb.StringProperty(repeated=True)

    def _pre_put_hook(self):
        print("pre put hook")
        print("self is...")
        print(self)
        #update game list
        self.update_gamelist()

    def update_gamelist(self):
        print(self)
