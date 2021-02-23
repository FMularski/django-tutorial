from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='polls_index'),                                   # polls/
    path('<int:question_id>/', views.detail, name='question_detail'),            # polls/id
    path('<int:question_id>/detail', views.results, name='question_results'),    # polls/id/details
    path('<int:question_id>/vote', views.vote, name='question_vote'),             # polls/id/vote
    path('<int:question_id>/show', views.get_question, name='get_question')
]  
