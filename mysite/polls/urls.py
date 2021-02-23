from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('questions/<int:question_id>', views.question, name='question'),
    path('vote/<int:choice_id>', views.vote, name='vote'),
    path('thanks', views.thanks, name='thanks')
]  
