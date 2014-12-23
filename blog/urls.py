from django.conf.urls import patterns, url
from blog import views

urlpatterns = patterns('',
	url(r'^tutorials/$', 
		views.TutorialView.as_view(), 
		name='tutorials'
	),
	url(r'^api/$', 
		views.ApiBlogView.as_view(),
	),
	url(r'^(?P<slug>[-_\w]+)/$', 
		views.SingleView.as_view(), 
		name='blog_single'
	),
	url(r'^$', 
		views.ApiView.as_view(), 
		# views.BlogView.as_view(), 
		name='blog_home'
	),
)