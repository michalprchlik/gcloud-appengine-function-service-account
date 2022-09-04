from gui.action.tasks import create_task


def run():

	project = 'rododendron-361414'
	location = 'europe-west6'
	queue_name = 'queue'
	url = f"https://{location}-{project}.cloudfunctions.net/function"
	message = '{}'
	in_seconds = None

	create_task(project, location, queue_name, url, message, in_seconds)

	message = "OK"

	return message
