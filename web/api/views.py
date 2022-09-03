import logging
import traceback

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.run import validate_api_data, run_api


class ListView(APIView):

	def post(self, request):

		data = request.data.copy()
		logging.info(data)

		try:
			message = validate_api_data(data)
			if message == 'OK':

				run_api(data)

				response = Response({'message': message}, status=status.HTTP_200_OK)

			else:
				logging.error(message)
				response = Response({'message': message}, status=status.HTTP_400_BAD_REQUEST)

		except Exception as exception: #pylint: disable=broad-except
			logging.exception('Got an exception')
			response = Response({'exception': str(exception)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

			if 'unittest.util' in __import__('sys').modules:
				print(str(traceback.format_exc()))

		return response
