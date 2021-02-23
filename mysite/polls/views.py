from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
import json


def index(request):
   return HttpResponse('Hello')