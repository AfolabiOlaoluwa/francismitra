from django.conf.urls import patterns, include, url
from django.http import HttpResponseRedirect
import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	# url(r'^$', include('portfolio.urls', namespace='portfolio')),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    # url(r'^portfolio/', include('portfolio.urls', namespace='portfolio')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('portfolio.urls', namespace='portfolio')),
)
