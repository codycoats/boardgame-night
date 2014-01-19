#!/usr/bin/env python
# -*- coding: utf-8 -*-

from handlers import *

#This is the place where all of your URL mapping goes
route_list = [
	(r'^/events', EventsHandler),
           (r'^/new-event', NewEventHandler),
	(r'^/', DefaultHandler)
]
