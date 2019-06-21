# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import logging as pylogger
from django.shortcuts import render
from django.http import JsonResponse


#GCP Imports
from google.cloud import error_reporting
from google.cloud import logging as logging_gcp

#Error setup
error_client = error_reporting.Client()

#Logging setup
client = logging_gcp.Client()

handler = client.get_default_handler()
py_logger = pylogger.getLogger("cloudLogger")
py_logger.setLevel(pylogger.INFO)
py_logger.addHandler(handler)

# The name of the log to write to
log_name = 'django-app-logging'
# Selects the log to write to
logger = client.logger(log_name)


# Create your views here.
def hello(request):
    py_logger.info("say hi")
    return JsonResponse({"message": "hello world"})


def hello_error(request):
    try:
        user = User.objects.all()

        return JsonResponse({"message": user})
    except Exception as e:
        py_logger.critical(e)
        error_client.report_exception()

        return JsonResponse({"message": "somethin wrong"})
