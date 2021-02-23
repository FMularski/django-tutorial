from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

def index(request):
   return HttpResponse('Index of polls.')

def detail(request, question_id):
   return HttpResponse(f'You are looking at question {question_id}')

def results(request, question_id):
   response = f'You are looking at question {question_id}'
   return HttpResponse(response)

def vote(request, question_id):
   return HttpResponse(f'You are voting on question {question_id}')

def get_question(request, question_id):
   question = Question.objects.get(id=question_id)
   return HttpResponse(question)
