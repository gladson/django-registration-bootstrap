# -*- coding: utf-8 -*-
from django.contrib.auth import views as auth_views
from django.conf.urls import patterns, url

from bootstrap.views import (
	Index_Bootstrap,
	)

urlpatterns = patterns('',
    url(r'^$', Index_Bootstrap.as_view(), name='index_bootstrap'),
    url(r'^login/$', auth_views.login, {'template_name': 'bootstrap/registration/login.html'}, name='login_bootstrap'),
    url(r'^password_reset/$', auth_views.password_reset, {'template_name': 'bootstrap/registration/password_reset_form.html'}, name='password_reset_bootstrap'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, {'template_name': 'bootstrap/registration/password_reset_done.html'}, name='password_reset_done'),
    # Support old style base36 password reset links; remove in Django 1.7
    url(r'^reset/(?P<uidb36>[0-9A-Za-z]{1,13})-(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'django.contrib.auth.views.password_reset_confirm_uidb36'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, {'template_name': 'bootstrap/registration/password_reset_confirm.html'},
        name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, {'template_name': 'bootstrap/registration/password_reset_complete.html'}, name='password_reset_complete'),
)