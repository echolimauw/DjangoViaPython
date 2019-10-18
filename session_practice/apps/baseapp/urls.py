from django.conf.urls import url
from . import views      

urlpatterns = [
    url(r'^$', views.index),
    url(r'^success$', views.success),
    url(r'^error$', views.error),
    url(r'^process$', views.process),
    url(r'^(?P<animal>\w+)$', views.process),
]