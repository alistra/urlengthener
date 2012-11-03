from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$',               'urls.views.index'),
    url(r'^p/(?P<url>.*)/$', 'urls.views.posted'),
    url(r'^r/(?P<url>.*)/$', 'urls.views.redirect'),
    url(r'^admin/', include(admin.site.urls)),
)
