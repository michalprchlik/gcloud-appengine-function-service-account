from django.test import TestCase


from api.run import validate_api_data, run_api


class RunApi(TestCase):

	def test(self):

		data = {}

		result = run_api(data)
		expected_result = True

		self.assertEqual(result, expected_result)


class ValidateApiDataValid(TestCase):

	def test(self):

		data = {}

		result = validate_api_data(data)
		expected_result = "OK"

		self.assertEqual(result, expected_result)
