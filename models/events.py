from google.appengine.ext import ndb

from google.appengine.ext import db
from google.appengine.api import urlfetch
import urllib2
import logging
import xml.dom.minidom as mdom

from models import profile
from models import game

class Events(ndb.Model):
    title = ndb.StringProperty()
    date = ndb.DateProperty()
    host = ndb.UserProperty(required=True)
    attendees = ndb.UserProperty(repeated=True)
    games = ndb.KeyProperty(repeated=True)

    def _pre_put_hook(self):
        #update game list
        self.update_gamelist()

    def update_gamelist(self):
        print("updating game list")

        host_user = self.host
        host_profile_query = profile.Profile.query( profile.Profile.user == host_user)
        host_profile = host_profile_query.get()

        #if host has completed BGG Profile
        if host_profile:

            #if games is complete
            #recreate entire list
            if not self.games:
                requestURL = "http://www.boardgamegeek.com/xmlapi/collection/" \
                                     + host_profile.bggProfile + "?own=1"

                data = urlfetch.fetch(requestURL).content
                dom = mdom.parseString(data)

                #loop through dom and get all games

                items = dom.getElementsByTagName("item")

                games = []
                for item in items:
                    item_name = item.getElementsByTagName('name').item(0).firstChild.data

                    item_stats = item.getElementsByTagName('stats').item(0)
                    item_maxPlayers = item_stats.getAttribute("maxplayers")
                    item_minPlayers = item_stats.getAttribute("minplayers")

                    #create new game
                    g = game.Game()
                    g.title = item_name
                    g.maxPlayers = item_maxPlayers
                    g.minPlayers = item_minPlayers


                    gKey = g.put()
                    games.append(gKey)

                self.games = games


