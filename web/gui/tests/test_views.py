from django.contrib.auth.models import User #pylint: disable=imported-auth-user
from django.test import TestCase
from django.urls import reverse
from rest_framework import status


class TestIndexView(TestCase):

	def setUp(self):

		self.client.force_login(User.objects.get_or_create(username='testuser')[0])

	def test(self):

		response = self.client.get(
			reverse(
				'index'
			)
		)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
