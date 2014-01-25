from models import events

import logging
from datetime import datetime

log = logging.getLogger(__name__)

from base import BaseHandler

class EventsHandler(BaseHandler):
    def get(self):
        config = self.app.config

        #Get all events
        events_query = events.Events.query()
        e = events_query.fetch()

        print (type(e))

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

class EventHandler(BaseHandler):
    def get(self, eventKey):

        #get event
        event = events.Events.get(eventKey)

        print(event)

        template_values ={
            'event' : event
        }

        config = self.app.config
        self.render_response('event.html')

class DefaultHandler(BaseHandler):
    def get(self):
	config = self.app.config
	self.render_response('default.html')