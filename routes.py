#!/usr/bin/env python
# -*- coding: utf-8 -*-

import handlers
from handlers import common_handler

#This is the place where all of your URL mapping goes
route_list = [
           (r'^/events/(.*)', common_handler.EventHandler),
	(r'^/events', common_handler.EventsHandler),
           (r'^/new-event', common_handler.NewEventHandler),
           (r'^/edit-event/(.*)', common_handler.EditEventHandler),
           (r'^/delete-event/(.*)', common_handler.DeleteEventHandler),
	(r'^/', common_handler.DefaultHandler)
]
