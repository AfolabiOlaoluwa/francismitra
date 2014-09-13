import urllib2
import json
from django.db import models

class PersonalInstagram(object):
	def __init__(self, user_id, client_id):
		self.user_id   = user_id
		self.client_id = client_id

	def find_feed(self):
		url      = 'https://api.instagram.com/v1/users/%s/media/recent/?client_id=%s' % (self.user_id, self.client_id)
		response = urllib2.urlopen(url)
		data     = json.load(response)

		return data


	

