# variable used for deployment of the project
export PROJECT_NAME := rododendron-361414
export REGION := europe-west6

export SERVICE_ACCOUNT_EMAIL := service-account@$(PROJECT_NAME).iam.gserviceaccount.com

export DJANGO_SECRET_KEY := $(shell cat /dev/urandom | LC_ALL=C tr -dc '[:alpha:]'| fold -w 50 | head -n1)
export DJANGO_SECRET_NAME := django-settings

export DATABASE_INSTANCE_NAME := $(PROJECT_NAME)-postgresql
export DATABASE_NAME := $(PROJECT_NAME)-sql-database
export DATABASE_PASSWORD := $(shell cat /dev/urandom | LC_ALL=C tr -dc '[:alpha:]'| fold -w 50 | head -n1)
export DATABASE_USER := user




enable-api:
	gcloud services enable \
	sqladmin.googleapis.com \
	secretmanager.googleapis.com \
	cloudtasks.googleapis.com \
	cloudresourcemanager.googleapis.com \
	cloudbuild.googleapis.com \
	cloudfunctions.googleapis.com 


create-app:
	gcloud app create


create-queue:
	gcloud tasks queues create queue --quiet --location=$(REGION)

# You do not need to delete whole database instance in order to wipe out database's schema
create-database:
	gcloud sql instances create $(DATABASE_INSTANCE_NAME) \
	    --project $(PROJECT_NAME) \
	    --database-version POSTGRES_14 \
	    --tier db-f1-micro \
	    --region $(REGION)


# https://cloud.google.com/iam/docs/creating-managing-service-accounts#iam-service-accounts-create-gcloud
# https://cloud.google.com/tasks/docs/creating-http-target-tasks#token
create-serivice-account:
	gcloud iam service-accounts create service-account \
	    --description="description" \
	    --display-name="service-account"

	gcloud projects add-iam-policy-binding $(PROJECT_NAME) \
	    --member="serviceAccount:${SERVICE_ACCOUNT_EMAIL}" \
	    --role="roles/cloudfunctions.invoker"


configure-database:
	# clean up the project
	-gcloud sql databases delete $(DATABASE_NAME) --instance $(DATABASE_INSTANCE_NAME) --quiet
	-gcloud sql users delete $(DATABASE_USER) --instance $(DATABASE_INSTANCE_NAME) --quiet
	-gcloud secrets delete $(DJANGO_SECRET_NAME) --quiet

	# Within the created instance, create a database
	gcloud sql databases create $(DATABASE_NAME) --instance $(DATABASE_INSTANCE_NAME)

	# Create a database user
	gcloud sql users create $(DATABASE_USER) --instance $(DATABASE_INSTANCE_NAME) --password $(DATABASE_PASSWORD)

	# Create a file called .env, defining the database connection string, the media bucket name, and a new SECRET_KEY value
	echo DATABASE_URL=postgres://$(DATABASE_USER):${DATABASE_PASSWORD}@//cloudsql/$(PROJECT_NAME):$(REGION):$(DATABASE_INSTANCE_NAME)/$(DATABASE_NAME) > web/.env
	echo GS_BUCKET_NAME=$(PROJECT_NAME)-django-bucket >> web/.env
	echo SECRET_KEY=$(DJANGO_SECRET_KEY) >> web/.env

	# Create a new secret, django-settings, with the value of the .env file
	gcloud secrets create $(DJANGO_SECRET_NAME) --data-file web/.env

	# Grant access to the secret to the App Engine standard service account
	gcloud secrets add-iam-policy-binding $(DJANGO_SECRET_NAME) \
	   --member serviceAccount:${PROJECT_NAME}@appspot.gserviceaccount.com \
	    --role roles/secretmanager.secretAccessor

install-proxy:
	wget https://dl.google.com/cloudsql/cloud_sql_proxy.linux.amd64 -O cloud_sql_proxy
	chmod +x cloud_sql_proxy
	sudo cp cloud_sql_proxy /usr/bin


run-proxy:
	export GOOGLE_CLOUD_PROJECT=$(PROJECT_NAME)
	export USE_CLOUD_SQL_AUTH_PROXY=true
	./cloud_sql_proxy -instances=$(PROJECT_NAME):$(REGION):$(DATABASE_INSTANCE_NAME)=tcp:5432
