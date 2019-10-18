from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^addBook$', views.addBook),
    url(r'^addlBook/(?P<id>\d+)$', views.addlBook),
    url(r'^authors$', views.authors),
    url(r'^addAuthor$', views.addAuthor),
    url(r'^books/(?P<id>\d+)$', views.viewBook),
    url(r'^authors/(?P<id>\d+)$', views.viewAuth),
]