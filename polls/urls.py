from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    # ex: /<language_code/polls/
    path('', views.IndexView.as_view(), name = 'index'),
    # ex: /<language_code/polls/5/
    path('<int:pk>/', views.DetailView.as_view(), name = 'detail'),
    # ex: /<language_code/polls/5/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name = 'results'),
    #ex: /<language_code/polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name = 'vote'),
    #ex: /<language_code/polls/mytranslate/
    path('mytranslate/', views.mytranslateview, name = 'mytranslate'),
    #ex: /<language_code/polls/essaitraduc/
    path('essaitraduc/', views.matraduc, name = 'matraduc'),
]
