from django.conf import settings
from django.urls import re_path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from api.views import ListView


urlpatterns = [
	re_path(
		r'^$',
		ListView.as_view(),
		name='api_view'
	),
]
