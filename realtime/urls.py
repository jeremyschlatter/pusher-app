from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'realtime.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^chat/', include('chat.urls', namespace='chat')),
    url(r'^$', include('chat.urls', namespace='chat')),
    url(r'^admin/', include(admin.site.urls)),
)
