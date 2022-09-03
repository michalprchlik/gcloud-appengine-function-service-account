from datetime import datetime, timezone
import logging

from modules.tasks import create_task_for_api

if 'unittest.util' in __import__('sys').modules:
	logging.disable(logging.CRITICAL)


def run(request_json):

	message = {
		'message': 'message',
	}

	create_task_for_api(message)

	return message


def get_is_request_valid(request):

	valid = bool(request.headers['content-type'] == 'application/json')

	return valid


def get_is_request_json_valid(request_json):

	valid = True

	return valid
