from django.urls import re_path

from gui.action.create_event.views import create_event


urlpatterns = [
	re_path(
		'create_event?$',
		create_event,
		name='create_event'
	),
]
