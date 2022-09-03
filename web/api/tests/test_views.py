import json

from django.test import TestCase
from django.urls import reverse
from rest_framework import status


class Api(TestCase):

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
