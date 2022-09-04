from django.urls import re_path, include
from django.views.generic import RedirectView
from django.conf import settings

from gui import views as general_view


urlpatterns = [
	re_path(
		'^$',
		general_view.index,
		name='index'
	),
	re_path(
		r'action/',
		include('gui.action.urls'),
		name='gui_action_view'
	),
	re_path(r'^favicon\.ico$',RedirectView.as_view(url='/static/images/favicon.ico')),
]
