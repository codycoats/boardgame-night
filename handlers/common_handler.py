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

        template_values = {
            'warnings' : []
        }

        user = users.get_current_user()
        user_profile = profile.Profile.query(profile.Profile.user == user).get()

        if not user_profile:
            template_values['warnings'].append("You have not completed your profile. Go to your <a href='/profile'>profile</a> to ensure full functionality.")

        config = self.app.config
        self.render_response('new-event.html', **template_values)

    def post(self):

        #create new Event
        event = events.Events()

        #update new model with submitted information from form
        event.title = self.request.get('title')
        event.date = datetime.strptime(self.request.get('event-date'), '%m/%d/%y')
        event.host = users.get_current_user()

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

class SignupEventHandler(BaseHandler):
    def post(self, eventUrlString):

        #get event
        event_key = ndb.Key(urlsafe=eventUrlString)
        event = event_key.get()

        #add user to attendees list
        user = users.get_current_user()
        event.attendees.append(user)

        #update event
        event.put()

        self.redirect('/events/'+eventUrlString)

class EventHandler(BaseHandler):
    def get(self, eventUrlString):

        #get event
        event_key = ndb.Key(urlsafe=eventUrlString)
        event = event_key.get()

        template_values ={
            'event' : event
        }

        print(event.attendees)

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

class EditProfileHandler(BaseHandler):
    def get(self):

        #get user and profile
        current_user = users.get_current_user()

        print(current_user)

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

        print(current_user)
        print(template_values)

        self.render_response('edit-profile.html', **template_values)

    def post(self):

        #get user and profile
        current_user = users.get_current_user()

        profile_query = profile.Profile.query( profile.Profile.user == current_user)
        current_profile = profile_query.get()


        #update fields
        current_profile.info = self.request.get('info')
        current_profile.bggProfile = self.request.get('bggProfile')

        current_profile.put()

        self.redirect('/profile')


class DefaultHandler(BaseHandler):
    def get(self):
	config = self.app.config
	self.render_response('default.html')