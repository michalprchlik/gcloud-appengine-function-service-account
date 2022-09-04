import json

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from os import environ


class Api1(TestCase):

	def test(self):

		data = {}
		data = json.dumps(data)

		response = self.client.post(
			reverse(
				'api_view',
			),
			data,
			content_type='application/json'
		)

		self.assertEqual(response.data, {'message': 'OK'})
		self.assertEqual(response.status_code, status.HTTP_200_OK)


class Api2(TestCase):

	def test(self):

		data = {}
		data = json.dumps(data)

		environ['GOOGLE_CLOUD_PROJECT'] = "GOOGLE_CLOUD_PROJECT"
		response = self.client.post(
			reverse(
				'api_view',
			),
			data,
			content_type='application/json'
		)

		self.assertEqual(response.data, {'message': 'Unauthorized'})
		self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

		environ['GOOGLE_CLOUD_PROJECT'] = ""