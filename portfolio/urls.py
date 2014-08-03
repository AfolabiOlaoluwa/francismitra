from django.conf.urls import patterns, url
from portfolio import views

urlpatterns = patterns('',
	# Functional views
	# url(r'^$', views.index, name='index'),
	# url(r'^(?P<title>\w+)/$', views.categories, name='categories'),

	# Class based views
	url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^(?P<slug>\w+)/$', views.CategoryView.as_view(), name='categories'),
)
