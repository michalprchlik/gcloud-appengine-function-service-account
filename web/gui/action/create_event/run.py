from gui.action.tasks import create_task


def run():

	project = ''
	location = ''
	queue_name = ''
	url = ''
	message = ''
	in_seconds = None

	create_task(project, location, queue_name, url, message, in_seconds)

	message = "OK"

	return message
