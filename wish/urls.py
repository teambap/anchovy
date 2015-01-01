from django.conf.urls import patterns, url, include
from wish import views

urlpatterns = patterns('',
    url(r'^list.bap$', views.list, name='list'),
    url(r'^list', views.list_json),
    url(r'^add.bap$', views.add_form),
    url(r'^add', views.add),
    url(r'^(?P<item_id>\d+)/delete', views.delete),
)