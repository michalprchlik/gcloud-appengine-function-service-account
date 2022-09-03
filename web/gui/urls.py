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
		f'^$',
		general_view.user_login,
		name='user_login'
	),
	re_path(
		'user/logout/?$',
		general_view.user_logout,
		name='user_logout'
	),
	re_path(r'^favicon\.ico$',RedirectView.as_view(url='/static/images/favicon.ico')),
]
