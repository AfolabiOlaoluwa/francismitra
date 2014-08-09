from django.conf.urls import patterns, include, url
import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^$', 'francismitra.views.home', name='home'),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^portfolio/', include('portfolio.urls', namespace='portfolio')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^admin/', include(admin.site.urls)),
)
