from datetime import datetime, timedelta
import json
import logging
from os import getenv

from google.cloud import tasks_v2
from google.protobuf import timestamp_pb2


def create_task_for_api(message):

	project = getenv("PROJECT")
	location = getenv("LOCATION")
	url_app_engine = getenv("URL_APP_ENGINE")
	queue_name = 'api'
	url = f"https://{project}.{url_app_engine}/api/"
	in_seconds = None

	create_task(project, location, queue_name, url, message, in_seconds)


def create_task(project, location, queue_name, url, message, in_seconds): #pylint: disable=too-many-arguments

	logging.info(f"project={project}, location={location}, queue_name={queue_name}, url={url}, message={message}, in_seconds={in_seconds} - created task") #pylint: disable=line-too-long
	task = prepare_task(url, message, in_seconds)

	is_testing = 'unittest.util' in __import__('sys').modules
	if not is_testing:
		client = tasks_v2.CloudTasksClient()
		queue = client.queue_path(project, location, queue_name)
		client.create_task(request={"parent": queue, "task": task})


def prepare_task(url, message, in_seconds):

	service_account_email = getenv("SERVICE_ACCOUNT_EMAIL")
	payload = json.dumps(message)
	converted_payload = payload.encode()
	task = {
		"http_request": {
			"http_method": tasks_v2.HttpMethod.POST,
			"url": url,
			"headers": {
				"Content-type": "application/json",
				'accept': 'application/json'
			},
			"oidc_token": {
				"service_account_email": service_account_email,
			},
			"body": converted_payload,
		}
	}

	if in_seconds:
		date = datetime.utcnow() + timedelta(seconds=in_seconds)

		timestamp = timestamp_pb2.Timestamp()
		timestamp.FromDatetime(date) #pylint: disable=no-member
		task['schedule_time'] = timestamp

	return task
