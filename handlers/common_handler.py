from google.appengine.ext import ndb
from google.appengine.api import users

from models import events
from models import profile

import logging
from datetime import datetime

log = logging.getLogger(__name__)

from base import BaseHandler

#Event Handlers
class EventsHandler(BaseHandler):
    def get(self):
        config = self.app.config

        #Get all events
        events_query = events.Events.query()
        e = events_query.fetch()

        #Display all events
        template_values = {
            'events': e
        }

        self.render_response('events.html', **template_values)

class NewEventHandler(BaseHandler):
    def get(self):
        config = self.app.config
        self.render_response('new-event.html')

    def post(self):

        #create new Event
        event = events.Events()

        #update new model with submitted information from form
        event.title = self.request.get('title')
        event.date = datetime.strptime(self.request.get('date'), '%m/%d/%y')

        #save new event to db
        event.put()

        self.redirect('/events')

class EditEventHandler(BaseHandler):
    def get(self, eventUrlString):

        #get event
        event_key = ndb.Key(urlsafe=eventUrlString)
        event = event_key.get()

        template_values ={
            'event' : event
        }

        config = self.app.config
        self.render_response('edit-event.html', **template_values)

    def post(self, eventUrlString):

        #get event
        event_key = ndb.Key(urlsafe=eventUrlString)
        event = event_key.get()

        #modify event values with user input
        event.title = self.request.get('title')
        event.date = datetime.strptime(self.request.get('date'), '%m/%d/%y')

        event.put()

        self.redirect('/events/'+event.key.urlsafe())

class DeleteEventHandler(BaseHandler):
    def post(self, eventUrlString):

        #get event key
        event_key = ndb.Key(urlsafe=eventUrlString)

        #delete from datastore
        event_key.delete()

        self.redirect('/events')

class EventHandler(BaseHandler):
    def get(self, eventUrlString):

        #get event
        event_key = ndb.Key(urlsafe=eventUrlString)
        event = event_key.get()

        template_values ={
            'event' : event
        }

        config = self.app.config
        self.render_response('event.html', **template_values)

#User Handlers
class ProfileHandler(BaseHandler):
    def get(self):

        #get user and profile
        current_user = users.get_current_user()

        profile_query = profile.Profile.query( profile.Profile.user == current_user)
        current_profile = profile_query.get()

        #first time user
        if not current_profile:
            #create new profile
            current_profile = profile.Profile()

            current_profile.user = current_user

            current_profile.put()

        template_values = {
            'user' : current_user,
            'profile' : current_profile
        }

        self.render_response('profile.html', **template_values)


class DefaultHandler(BaseHandler):
    def get(self):
	config = self.app.config
	self.render_response('default.html')