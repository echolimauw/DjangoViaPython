from django.conf.urls import url
from . import views      

urlpatterns = [
    url(r'^shows/newShow$', views.newShow),
    url(r'^shows$', views.shows),
    url(r'^shows/createShow$', views.createShow),
    url(r'^shows/(?P<id>\d+)/delete$', views.deleteShow), 
    url(r'^shows/(?P<id>\d+)/saveEdit$', views.saveEdit), 
    url(r'^shows/(?P<id>\d+)/edit$', views.editShow),
    url(r'^shows/(?P<id>\d+)$', views.viewShow),
    url(r'^$', views.shows),
]