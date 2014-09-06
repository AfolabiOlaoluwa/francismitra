from django.conf.urls import patterns, url
from portfolio import views

urlpatterns = patterns('',
	url(r'^$', 
		views.IndexView.as_view(), 
		name='index'
	),
	url(r'^(?P<slug>\w+)/$', 
		views.CategoryView.as_view(), 
		name='categories'
	),
	url(r'^resume', 
		views.ResumeView.as_view(), 
		name='resume'
	),
	url(r'^info', 
		views.InfoView.as_view(), 
		name='info'
	),
)
