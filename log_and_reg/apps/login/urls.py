from django.conf.urls import url, include
from . import views  

urlpatterns = [
    url(r'^$', views.index),
    url(r'^logout$', views.logout),
    url(r'^success/(?P<id>\d+)$', views.success),
    url(r'^process_reg$', views.process_reg),
    url(r'^process_log$', views.process_log),
]