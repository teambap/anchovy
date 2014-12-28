from django.conf.urls import patterns, url, include
from wish import views

urlpatterns = patterns('',
    url(r'^list$', views.list, name='list'),
    url(r'^list.json$', views.list_json),
    url(r'^add$', views.add_form),
    url(r'^add.json$', views.add),
    url(r'^remove.json$', views.remove),
)