import json
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.detail import BaseDetailView
from django import http
from instagram import client
from social.models import PersonalInstagram
from portfolio.views import LayoutView

INSTAGRAM_CONFIG = {
	'client_id': 'af80dd4c67de439fba77ac4c4743ead0',
	'client_secret': '1f661d6538c44c9a83ff279bc350bb75',
	'redirect_uri': 'http://127.0.0.1:8000/social'
}

unauthenticated_api = client.InstagramAPI(**INSTAGRAM_CONFIG)

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
Personal Instagram feed for view consumption.
Not tied to the authenticated API 
'''		
class InstagramFeed(JSONResponseMixin, BaseDetailView):
	def get(self, request, *args, **kwargs):
	    my_user_id        = '2968231'
	    my_client_id      = 'af80dd4c67de439fba77ac4c4743ead0'
	    my_instagram      = PersonalInstagram(my_user_id, my_client_id)
	    
	    try: 
	    	json_response = my_instagram.find_feed()
	    except Exception, e:
	    	json_response = {'failed':'Unable to find feed'}
	    
	    context = json_response
	    return self.render_to_response(context)

'''
Allow visitors the option to connect via
the API to perform authenticated actions
'''
class SocialView(LayoutView, TemplateView):
	template_name = 'social/social.html'

	def get_context_data(self, **kwargs):
		context = super(SocialView, self).get_context_data(**kwargs)
		context['page_title'] = 'Social'

		# Create button to authenticate users
		try:
			url = unauthenticated_api.get_authorize_url(scope=["likes","comments"])
			context['link'] = url
		except Exception, e:
			context['link'] = '#'
			print e  

		# Code parameter is available when attempting to authenticate user
		try:
			code = self.request.GET.get('code')
			access_token, user_info = unauthenticated_api.exchange_code_for_access_token(code)
			if not access_token:
				return 'No access token available'
			self.request.session['access_token'] = access_token
		except Exception, e:
			print e

		# If session has been created, enable authenticated features
		if self.request.session.get('access_token'):
			check_session = self.request.session.get('access_token')
			api = client.InstagramAPI(access_token=check_session)

			# Results for testing...
			# context['test']          = check_session
			# context['popular_media'] = api.user_recent_media(count=20)

		return context








