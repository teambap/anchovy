from django.conf.urls import patterns, url, include
from users import views

urlpatterns = patterns('',
    url(r'^home.bap$', views.home, name='home'),
    url(r'^info', views.info),
    url(r'^logout', views.logout),
)