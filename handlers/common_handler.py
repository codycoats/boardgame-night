
import logging

log = logging.getLogger(__name__)

from base import BaseHandler

class EventsHandler(BaseHandler):
    def get(self):
	config = self.app.config
	self.render_response('events.html')

class DefaultHandler(BaseHandler):
    def get(self):
	config = self.app.config
	self.render_response('default.html')