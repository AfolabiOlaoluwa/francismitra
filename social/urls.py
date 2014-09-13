from django.conf.urls import patterns, url
from social import views

urlpatterns = patterns('',
	url(r'^$', 
		views.SocialView.as_view(), 
		name='social_home'
	),
	url(r'^instagram',
		views.InstagramFeed.as_view(),
		name='instagram'
	),
)

