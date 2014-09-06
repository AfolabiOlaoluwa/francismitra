from django.shortcuts import render
from django.views.generic import TemplateView
from instagram import client
from portfolio.views import LayoutView

CONFIG = {
	'client_id': 'af80dd4c67de439fba77ac4c4743ead0',
	'client_secret': '1f661d6538c44c9a83ff279bc350bb75',
	# 'access_token': 
	'redirect_uri': 'http://127.0.0.1:8000/social/authorize'
}

unauthenticated_api = client.InstagramAPI(**CONFIG)
# instagram_api = client.InstagramAPI(**CONFIG)

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

class AuthorizeView(LayoutView, TemplateView):
	template_name = 'social/authorize.html'

	def get_context_data(self, **kwargs):
		context = super(AuthorizeView, self).get_context_data(**kwargs)
		context['page_title'] = 'Instagram'

		code = self.request.GET.get('code')
		# code = request.GET.get("code")
		if not code:
			return 'Missing code'
		try:
			access_token, user_info = unauthenticated_api.exchange_code_for_access_token(code)
			context['access_token'] = access_token
			if not access_token:
				return 'Could not get access token'
			api = client.InstagramAPI(access_token=access_token)
			context['access_token'] = access_token
		except Exception, e:
			print e

		# popular_media = unauthenticated_api.user_recent_media(count=20)
		# context['popular_media'] = popular_media
		# for media in popular_media:
		    # print media.images['standard_resolution'].url

		return context

class SocialView(LayoutView, TemplateView):
	template_name = 'social/social.html'

	def get_context_data(self, **kwargs):
		context = super(SocialView, self).get_context_data(**kwargs)
		context['page_title'] = 'Social'
		return context







