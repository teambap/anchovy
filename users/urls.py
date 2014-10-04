from django.conf.urls import patterns, url
from users import views

urlpatterns = patterns('',
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    url(r'^add$', views.add, name='add'),
    url(r'^info$', views.info, name='info'),
)