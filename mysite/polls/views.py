from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.urls import reverse
from django.views import generic


class IndexView(generic.ListView):
   template_name = 'polls/index.html'
   context_object_name = 'questions'

   def get_queryset(self):
      return Question.objects.order_by('pub_date')[:5]


class DetailView(generic.DetailView):
   model = Question
   template_name = 'polls/detail.html'


def vote(request, question_id):
   question = get_object_or_404(Question, id=question_id)   #  get question or 404
   try:
      selected_choice = question.choice_set.get(id=request.POST['choice']) # choice is a radio field with value=1,2,3...
   except (KeyError, Choice.DoesNotExist):   # no choice selected
      return render(request, 'polls/detail.html', {'question': question, 'error_msg': 'You did not select a choice.'})   #rerender tmp with error msg
   else:
      selected_choice.votes += 1 # increment votes count
      selected_choice.save()     # save changes

      return HttpResponseRedirect(reverse('polls:results', args=[question_id]))


class ResultsView(generic.DetailView):
   model = Question
   template_name = 'polls/results.html'