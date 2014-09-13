from django.shortcuts import render
from django.views.generic import TemplateView
from instagram import client
from portfolio.views import LayoutView

CONFIG = {
	'client_id': 'af80dd4c67de439fba77ac4c4743ead0',
	'client_secret': '1f661d6538c44c9a83ff279bc350bb75',
	'redirect_uri': 'http://127.0.0.1:8000/social'
}

unauthenticated_api = client.InstagramAPI(**CONFIG)

'''
Pull personal instagram feed and allow visitors the option 
to connect via the API to perform authenticated actions
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

			context['test']          = check_session
			context['popular_media'] = api.user_recent_media(count=20)

		return context

'''
Personal Instagram feed for view consumption. Not tied
to auhtenticated API 
'''		
class InstagramFeed(LayoutView, TemplateView):
	template_name = 'social/instagram.html'

	def get_context_data(self, **kwargs):
		context = super(InstagramFeed, self).get_context_data(**kwargs)
		context['page_title'] = 'Instagram'

		try:
			url = unauthenticated_api.get_authorize_url(scope=["likes","comments"])
			context['link'] = url
		except Exception, e:
			print e

		return context

'''
For testing purposes... authenticate user, set session,
and perform an authenticated action
'''
# class AuthorizeView(LayoutView, TemplateView):
# 	template_name = 'social/authorize.html'

# 	def get_context_data(self, **kwargs):
# 		context = super(AuthorizeView, self).get_context_data(**kwargs)
# 		context['page_title'] = 'Instagram'

# 		# Grabecode from instagram authentication api
# 		code = self.request.GET.get('code')
# 		if not code:
# 			return 'Missing code'
# 		try:
# 			access_token, user_info = unauthenticated_api.exchange_code_for_access_token(code)
# 			if not access_token:
# 				return 'Could not get access token'
# 			api = client.InstagramAPI(access_token=access_token)
# 			self.request.session['access_token'] = access_token
# 			# context['test'] = self.request.session.get('access_token')
# 		except Exception, e:
# 			print e

# 		# Was code grabbed successfully? Open a new session and pull media
# 		check_session = self.request.session.get('access_token')
# 		if check_session:
# 			context['test'] = check_session

# 			instagram_api = client.InstagramAPI(access_token=check_session)

# 			popular_media = api.user_recent_media(count=20)
# 			context['popular_media'] = popular_media

# 		return context








