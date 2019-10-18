from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^new$', views.newShow),
    url(r'^newShowPass$', views.newShowPass),
    url(r'^shows/(?P<show_id>\d+)$', views.infoShow),
    url(r'^shows/(?P<show_id>\d+)/update$', views.updateShow),
    url(r'^shows/(?P<show_id>\d+)/update/pass$', views.updateShowPass),
    url(r'^shows/(?P<show_id>\d+)/delete$', views.deleteShow),
    url(r'^shows$', views.shows),
    url(r'^$', views.index),
]