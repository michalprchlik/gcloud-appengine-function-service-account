"""
Main endpoint for serving HTTP requests to application
"""

from django.conf import settings
from django.contrib import admin
from django.urls import include, re_path, path
from django.views.static import serve
from django.conf.urls.static import static

urlpatterns = [
	re_path(
		r'admin/',
		admin.site.urls
	),
	re_path(
		r'api/?',
		include('api.urls'),
		name='api_view'
	),
	path(
		r'',
		include('gui.urls')
	),
	re_path(
		r'^static/(?P<path>.*)$',
		serve,
		{
			'document_root': settings.STATIC_ROOT,
		}
	)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
