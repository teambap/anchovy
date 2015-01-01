from django.conf.urls import patterns, url, include
from users import views

urlpatterns = patterns('',
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    url(r'^home$', views.home, name='home'),
    url(r'^info.json$', views.info),
    url(r'^logout.json$', views.logout),
)