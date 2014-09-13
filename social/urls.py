from django.conf.urls import patterns, url
from social import views

urlpatterns = patterns('',
	url(r'^$', 
		views.SocialView.as_view(), 
		name='social_home'
	),
	# url(r'^authorize',
	# 	views.AuthorizeView.as_view(),
	# 	name='authorize'
	# ),
	url(r'^instagram',
		views.InstagramFeed.as_view(),
		name='instagram'
	),
)

