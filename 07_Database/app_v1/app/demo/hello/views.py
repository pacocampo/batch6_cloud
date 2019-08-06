# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import logging as pylogger
from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.
def hello(request):
    return JsonResponse({"message": "hello world"})


def hello_error(request):
    try:
        user = User.objects.all()
        return JsonResponse({"message": user})
    except Exception as e:
        return JsonResponse({"message": "something wrong"})
