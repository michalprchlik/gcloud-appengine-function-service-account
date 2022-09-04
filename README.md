# README.md

A testing project to test how to use gcloud service account as an authentication method in functions and in Django REST API

It consists of one page in Django framework with a button

Clicking the button will create an event in queue `queue` which will trigger a function `function`

`funcion` will send REST API back to backend `/api`

The communication is secured and all network traffic is protected