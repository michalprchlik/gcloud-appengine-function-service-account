import logging
import traceback
import json

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.run import validate_api_data, run_api
from api.authorize import get_is_authorized

class ListView(APIView):

	def post(self, request):

		data = request.data.copy()
		headers = request.META

		logging.info(data)

		is_authorized = get_is_authorized(headers)

		if is_authorized:
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
		else:
			message = "Unauthorized"
			response = Response({'message': message}, status=status.HTTP_401_UNAUTHORIZED)

		return response
