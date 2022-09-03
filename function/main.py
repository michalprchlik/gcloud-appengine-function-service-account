#!/usr/bin/env python3

import logging

from functions_framework import http

from modules.run import run, get_is_request_valid, get_is_request_json_valid

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logging.basicConfig(
	format='[%(levelname)s %(filename)s, %(lineno)d] %(message)s',
)

@http
def main(request):

	try:
		is_request_valid = get_is_request_valid(request)
		if is_request_valid:

			request_json = request.get_json(silent=True)
			logging.info(f"request_json={request_json}")

			is_request_json_valid = get_is_request_json_valid(request_json)
			if is_request_json_valid:

				run(request_json)

			else:
				message = f"ERROR: Request is valid but json data is invalid. request_json={request_json}"
				logging.error(message)
				return message, 400

		else:
			message = "ERROR: Request is invalid"
			logging.error(message)
			return message, 401

		return 'OK', 200

	except Exception: #pylint: disable=broad-except
		logging.exception('Got an exception')
		return 'Exception', 500
