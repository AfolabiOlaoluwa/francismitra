import json
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.detail import BaseDetailView
from django import http
from social.models import PersonalInstagram, AuthenticateInstagram
from social.config import INSTAGRAM_CONFIG
from portfolio.views import LayoutView


'''
Begin authentication to allow viewers to 'comment' and 'like' media.
Authentication is completed after user requests access token through
class SocialView and verified through checking session['access_token']
'''
instagram_user = AuthenticateInstagram(INSTAGRAM_CONFIG['client_id'], 
	                                   INSTAGRAM_CONFIG['client_secret'], 
	                                   INSTAGRAM_CONFIG['redirect_uri'])

class JSONResponseMixin(object):
	# Returns a JSON response containing 'context' as payload
	def render_to_response(self, context):
		return self.get_json_response(self.convert_context_to_json(context))

	# Construct an `HttpResponse` object.
	def get_json_response(self, content, **httpresponse_kwargs):
		return http.HttpResponse(content,
                                 content_type='application/json',
                                 **httpresponse_kwargs)

	# Convert the context dictionary into a JSON object
	def convert_context_to_json(self, context):
		return json.dumps(context)

'''
Personal Instagram feed rendered as JSON response.
Does not require authentication and is an instance of
a separate model
'''		
class InstagramFeed(JSONResponseMixin, BaseDetailView):
	def get(self, request, *args, **kwargs):
		my_instagram = PersonalInstagram(INSTAGRAM_CONFIG['user_id'], 
			                             INSTAGRAM_CONFIG['client_id'])
	    
		try: 
			instagram_feed = my_instagram.find_feed()
			json_response  = {'result':'success', 'content':instagram_feed}
		except Exception:
			json_response = {'result':'fail', 'content':'Failure in Django class InstagramFeed'}

		context = json_response
		return self.render_to_response(context)

'''
Allow visitors the option to connect via
the API to perform authenticated actions on model PersonalInstagram
'''
class SocialView(LayoutView, TemplateView):
	template_name = 'social/social.html'

	def get_context_data(self, **kwargs):
		context = super(SocialView, self).get_context_data(**kwargs)
		context['page_title'] = 'Social'

		# Check if code parameter is available and retrieve token
		if self.request.GET.get('code'):
			code = self.request.GET.get('code')	

			try:
				access_token = instagram_user.find_access_token(code)
				self.request.session['access_token'] = access_token
			except Exception:
				print 'Code not available in Django class SocialView'

		# Create visible button to authenticate users
		if not self.request.session.get('access_token'):
			context['link'] = instagram_user.get_authorization_url()

		return context

'''
Allow authenticated users to 'like' personal Instagram feed
'''
class MediaLike(JSONResponseMixin, BaseDetailView):
	def get(self, request, *args, **kwargs):
		if self.request.session.get('access_token'):
			token = self.request.session.get('access_token');

			id = self.request.GET.get('id')

			try: 
				instagram_user.like_instagram_photo(token, id)
				json_response = {'result':'success'}

			except Exception:
				json_response = {'result':'fail', 'message':'Failure in Django class MediaLike'}

		else:
			json_response = {'result':'fail', 'message':'Not logged in'}

		context = json_response

		return self.render_to_response(context)









