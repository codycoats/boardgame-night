import webapp2
from google.appengine.api import users
import json
from mako.template import Template
from mako.lookup import TemplateLookup
from webapp2_extras import mako

from models import profile

import logging

log = logging.getLogger(__name__)

mako.default_config.update(dict(
	    input_encoding='utf-8',
	    output_encoding = 'utf-8',
	    default_filters=['decode.utf8']
    ))

class BaseHandler(webapp2.RequestHandler):
    """BaseHandler which will be inherited all other handlers
    it should implement the most common functionality
    required by all handlers
    """

    def __init__(self, request, response):
	self.initialize(request, response)

    @webapp2.cached_property
    def mako(self):
	return mako.get_mako(app=self.app)

    def render_response(self, _template, **context):
        #Get current user
        user = users.get_current_user()
        user_profile = profile.Profile.query(profile.Profile.user == user).get()

        context['user'] = user
        context['profile'] = user_profile

        if user:
            context['log_inout_url'] = users.create_logout_url('/')
        else:
            context['log_inout_url'] = users.create_login_url('/')
        rv = self.mako.render_template(_template, **context)
        self.response.write(rv)

    def render_json(self, obj):
	rv = json.dumps(obj)
	self.response.headers.content_type = 'application/json'
	self.response.write(rv)

