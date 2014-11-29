from django.conf.urls import patterns, url, include
from wish import views

urlpatterns = patterns('',
    # ex: /polls/
    url(r'^list$', views.list, name='list'),
)