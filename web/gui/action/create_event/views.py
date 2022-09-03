import logging

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from gui.action.config.profile.delete.run import run


@login_required(login_url='login')
def create_event(request):

	try:

		message = run()

		response = redirect(f'/message_ok={message}')

	except Exception as exception: #pylint: disable=broad-except

		logging.exception('Got an exception')
		message = f"Something went wrong: {exception}"
		response = redirect(f'/?message_error={message}')

	return response
