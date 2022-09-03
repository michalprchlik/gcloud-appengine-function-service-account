from django.contrib.auth.models import User #pylint: disable=imported-auth-user
from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from gui.action.create_event.run import run


class Run(TestCase):

	def test(self):

		result = run()
		expected_result = 'OK'
		
		self.assertEqual(result, expected_result)

