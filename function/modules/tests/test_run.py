import unittest

from modules.run import run, get_is_request_valid, get_is_request_json_valid


class Run(unittest.TestCase):

	def test(self):

		request_json = {}
		result = run(request_json)
		expected_result = {
			'message': 'message'
		}

		self.assertEqual(result, expected_result)


class GetIsRequestValidValid(unittest.TestCase):

	def test(self):

		request = type('', (), {})()
		request.headers = {}
		request.headers['content-type'] = 'application/json' #pylint: disable=no-member

		result = get_is_request_valid(request)
		expected_result = True

		self.assertEqual(result, expected_result)


class GetIsRequestValidInvalid(unittest.TestCase):

	def test(self):

		request = type('', (), {})()
		request.headers = {}
		request.headers['content-type'] = 'invalid' #pylint: disable=no-member

		result = get_is_request_valid(request)
		expected_result = False

		self.assertEqual(result, expected_result)


class GetIsRequestJsonValidValid(unittest.TestCase):

	def test_is_request_json_valid(self):

		request_json = {}
		result = get_is_request_json_valid(request_json)
		expected_result = True

		self.assertEqual(result, expected_result)
