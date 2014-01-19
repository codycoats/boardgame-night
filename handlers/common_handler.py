
from models import events

import logging

log = logging.getLogger(__name__)

from base import BaseHandler

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
        event = Event()

        #update new model with submitted information from form
        event.title = self.request.get('title')
        event.date = self.request.get('date')

        #save new event to db
        event.put()

class DefaultHandler(BaseHandler):
    def get(self):
	config = self.app.config
	self.render_response('default.html')