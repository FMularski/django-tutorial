from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Question, Choice

def index(request):
   questions = Question.objects.all()
   return render(request, 'polls/index.html', {'questions': questions})

def question(request, question_id):
   question = get_object_or_404(Question, id=question_id)
   choices = question.choice_set.all()
   return render(request, 'polls/question.html', {'question': question, 'choices': choices})

def vote(request, choice_id):
   choice = Choice.objects.get(id=choice_id)
   choice.votes += 1
   choice.save()

   return redirect('/polls/thanks')

def thanks(request):
   return render(request, 'polls/thanks.html')