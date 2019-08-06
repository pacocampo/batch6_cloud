# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import JsonResponse

#python logger
import logging as pylogger

# GCP Logging
from google.cloud import logging as logging_gcp

# Instantiates a client
client = logging_gcp.Client()

handler = client.get_default_handler()
py_logger = pylogger.getLogger("cloudLogger")
py_logger.setLevel(pylogger.INFO)
py_logger.addHandler(handler)

# The name of the log to write to
log_name = 'django-app-logging'
# Selects the log to write to
logger = client.logger(log_name)


def health(request):
    print("request")
    py_logger.critical("critical")
    py_logger.error("bad news from python")
    py_logger.info("info from python")
    py_logger.warning("warning from python")
    py_logger.debug("debugeando")
    logger.log_struct({
        'message': 'hello logging',
        'status_code': 200,
        'request': 'health'
    })
    return JsonResponse({"result":"ok"})
 