from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^bootstrap/', include('bootstrap.urls')),
    url(r'^admin/', include(admin.site.urls)),
)