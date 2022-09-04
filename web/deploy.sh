#!/bin/bash

source ../config/config.sh

export GOOGLE_CLOUD_PROJECT=${PROJECT}
export USE_CLOUD_SQL_AUTH_PROXY=true

python3.9 manage.py makemigrations
python3.9 manage.py test

if [ $? -eq 0 ]; then 
	rm -rf static
	python3.9 manage.py collectstatic --noinput
	
	gcloud app deploy  --quiet
	
	python3.9 manage.py migrate
	
else
	echo "FIX THE TESTS!!!"
fi