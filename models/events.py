from google.appengine.ext import ndb

from google.appengine.ext import db
from google.appengine.api import urlfetch
import urllib2
import xml.dom.minidom as mdom


class Events(ndb.Model):
    title = ndb.StringProperty()
    date = ndb.DateProperty()
    host = ndb.UserProperty(required=True)
    attendees = ndb.UserProperty(repeated=True)
    games = ndb.StringProperty(repeated=True)

    def _pre_put_hook(self):
        #update game list
        self.update_gamelist()

    def update_gamelist(self):

        host_bggUsername = "abishek_sm"

        requestURL = "http://www.boardgamegeek.com/xmlapi/collection/" \
                             + host_bggUsername + "?own=1"

        data = urlfetch.fetch(requestURL).content
        dom = mdom.parseString(data)

        #loop through dom and get all games

        items = dom.getElementsByTagName("item")

        game_titles = []
        for item in items:
            item_name = item.getElementsByTagName('name')
            for i in item_name:
                game_titles.append(i.firstChild.data)

        self.games = game_titles

