from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'anchovy.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^user/', include('users.urls')),
    url(r'^item/', include('wish.urls')),
    url(r'^social/', include('social.apps.django_app.urls', namespace='social')),
    url(r'^account/', include('django.contrib.auth.urls', namespace='auth')),

)
