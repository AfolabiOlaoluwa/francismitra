from django.conf.urls import patterns, url
from portfolio import views

urlpatterns = patterns('',
	# Functional views
	# url(r'^$', views.index, name='index'),
	# url(r'^(?P<title>\w+)/$', views.categories, name='categories'),

	# Switching to class based views
	# Comment out the menu url later -- you don't want this accessible
	# url(r'^menu/$', views.Menu.as_view(), name='menu'),
	# url(r'^layout/$', views.LayoutView.as_view()),
	url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^(?P<slug>\w+)/$', views.CategoryView.as_view(), name='categories'),
	# url(r'^(?P<pk>\w+)/$', views.CategoryView.as_view(), name='categories'),
)
