"""
File with database configuration
File is used in settings.production  and settings.dev files
It will set up database engine based on env variables provided
If no variable is provided, it will start sqllite database
"""

import os

#from django.conf import settings

engines = {
	'sqlite': 'django.db.backends.sqlite3',
	'postgresql': 'django.db.backends.postgresql_psycopg2',
	'mysql': 'django.db.backends.mysql',
}


def config(basedir):
	"""
	Function to get configuration for database
	env variables are defined in openshift/template.yml file
	"""

	service_name = os.getenv('DATABASE_SERVICE_NAME', '').upper().replace('-', '_')

	if service_name:
		engine = engines.get(os.getenv('DATABASE_ENGINE'), engines['sqlite'])
	else:
		engine = engines['sqlite']

	name = os.getenv('DATABASE_NAME')

	if not name and engine == engines['sqlite']:
		name = os.path.join(basedir, 'db.sqlite3')
	return {
		'ENGINE': engine,
		'NAME': name,
		'USER': os.getenv('DATABASE_USER'),
		'PASSWORD': os.getenv('DATABASE_PASSWORD'),
		'HOST': os.getenv(f'{service_name}_SERVICE_HOST'),
		'PORT': os.getenv(f'{service_name}_SERVICE_PORT'),
	}
