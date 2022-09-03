#!/bin/bash

FUNCTION_NAME=buy-sell
MEMORY=128MB

make run-tests

if [ $? -eq 0 ]; then 

	source ../../config/config.sh

	gcloud functions deploy ${FUNCTION_NAME} \
	--memory ${MEMORY} \
	--entry-point main \
	--runtime python39 \
	--trigger-http \
	--region ${LOCATION} \
	--ingress-settings all \
	--no-allow-unauthenticated \
	--set-env-vars PROJECT=${PROJECT},LOCATION=${LOCATION},URL_APP_ENGINE=${URL_APP_ENGINE},SERVICE_ACCOUNT_EMAIL=${SERVICE_ACCOUNT_EMAIL}

else
	echo "FIX THE TESTS!!!"
fi