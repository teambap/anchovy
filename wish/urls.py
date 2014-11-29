from django.conf.urls import patterns, url, include
from wish import views

urlpatterns = patterns('',
    url(r'^list$', views.list, name='list'),
    url(r'^add$', views.add, name='add'),

)