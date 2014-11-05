import urllib2
import json
from django.db import models
from instagram import client

class PersonalInstagram(object):
	def __init__(self, user_id, client_id):
		self.user_id   = user_id
		self.client_id = client_id

	def find_feed(self, max_id=''):

		"""
		max_id is an empty string by default in order to
		to pull the most recent instagram items and paginate later
		"""

		# Consume feed without authorization
		url      = 'https://api.instagram.com/v1/users/%s/media/recent/?max_id=%s&client_id=%s' % (self.user_id, max_id, self.client_id)
		response = urllib2.urlopen(url)
		data     = json.load(response)

		return data

class AuthenticateInstagram(object):
	def __init__(self, client_id, client_secret, redirect_uri):
		self.client_id     = client_id
		self.client_secret = client_secret
		self.redirect_uri  = redirect_uri

		CONFIG = {
			'client_id': self.client_id,
			'client_secret': self.client_secret,
			'redirect_uri': self.redirect_uri
		}

		self.unauthenticated_api = client.InstagramAPI(**CONFIG)

	def get_authorization_url(self):
		try:
			url = self.unauthenticated_api.get_authorize_url(scope=["likes","comments"])
			return url
		except Exception:
			url = '#'
			return url

	def find_access_token(self, code):
		try:
			access_token, user_info = self.unauthenticated_api.exchange_code_for_access_token(code)
			return access_token
		except Exception, e:
			print e

	def like_instagram_photo(self, token, id):
		api = client.InstagramAPI(access_token=token)
		api.like_media(media_id=id)



