# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import JsonResponse

#python logger
import logging as pylogger



def health(request):
    print("request")
    py_logger.critical("critical")
    py_logger.error("bad news from python")
    py_logger.info("info from python")
    py_logger.warning("warning from python")
    py_logger.debug("debugeando")

    return JsonResponse({"result":"ok"})
 