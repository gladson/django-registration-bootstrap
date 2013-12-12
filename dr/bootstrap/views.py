# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import redirect
from django.conf import settings

from django.views.generic.base import TemplateView

if settings.LOGIN_URL_BOOTSTRAP:
	url = settings.LOGIN_URL_BOOTSTRAP
else:
	url = settings.LOGIN_URL

class Index_Bootstrap(TemplateView):
	def get(self, request, **kwargs):
		if not request.user.is_authenticated():
			return redirect('%s?next=%s' % (url, request.path))
	
	template_name = "bootstrap/capa.html"