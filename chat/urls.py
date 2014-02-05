from django.conf.urls import patterns, url

from chat import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<room_id>\d+)/$', views.room, name='room'),
    url(r'^(?P<room_id>\d+)/submit/$', views.submit, name='submit'),
)
