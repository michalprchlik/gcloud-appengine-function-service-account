# README.md

A testing project to test how to use gcloud service account as an authentication method in functions and in Django REST API

It consists of one page in Django framework with a button

Clicking the button will create an event in queue `queue` which will trigger a function `function`

`funcion` will create an event in queue `queue` which will send REST request to backend's API `/api`

The communication is secured and all network traffic is protected