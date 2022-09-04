import logging
import traceback
import json

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
import requests

from api.run import validate_api_data, run_api
from google.auth import crypt
from google.auth import jwt
from os import getenv


def get_is_authorized(headers):

	is_cloud_deployment = getenv('GOOGLE_CLOUD_PROJECT', None)

	if is_cloud_deployment:
		is_authorized = validate_headers(headers)
	else:
		is_authorized = True

	return is_authorized


def validate_headers(headers):

	is_authorized = False

	data_jwt = get_data_jwt_from_headers(headers)

	if data_jwt:

		kid = get_kid_from_jwt(data_jwt)
		certificate = get_certificate(kid)

		try:
			payload = jwt.decode(data_jwt, certs=certificate)
			logging.info(payload)
			service_account_email = service_account_email = getenv("SERVICE_ACCOUNT_EMAIL")

			if 'email' in payload and payload['email'] == service_account_email:
				is_authorized = True

		except ValueError as exception:
			logging.exception(exception)

	return is_authorized


def get_data_jwt_from_headers(headers):

	data_jwt = None
	if 'HTTP_AUTHORIZATION' in headers:

		auth_type, data_jwt = headers['HTTP_AUTHORIZATION'].split(" ", 1)
		if auth_type.lower() != "bearer":
			data_jwt = None

	return data_jwt


def get_kid_from_jwt(data_jwt):

	header, payload, signed_section, signature = jwt._unverified_decode(data_jwt)
	kid = header['kid']

	return kid


def get_certificate(kid):

	url = "https://www.googleapis.com/oauth2/v1/certs"

	response = requests.get(url)
	content = response.content.decode("utf-8")
	json_data = json.loads(content)

	try:
		certificate = json_data[kid]
	except KeyError:
		logging.error(f"kid={kid} not found in google certificates")
		certificate = ""

	return certificate
