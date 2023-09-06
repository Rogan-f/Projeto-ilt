from pathlib import Path
from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    # path("", views.index, name="index"),
    # # ex: /polls/5/
    # path("<int:question_id>/", views.detail, name="detail"),
    # # ex: /polls/5/results/
    # path("<int:question_id>/results/", views.results, name="results"),
    # # ex: /polls/5/vote/
    # path("<int:question_id>/vote/", views.vote, name="vote"),

    # class based views
    path('listar', views.QuestionListView.as_view(), name = "question-list"),
    path('cadastrar', views.QuestionCreateView.as_view(), name = "question-create"), 
    path('<int:pk>', views.QuestionDetailView.as_view(), name="question-detail"),
    path('<int:pk>/deletar', views.QuestionDeleteView.as_view(),name='question-delete'),
    path('<int:pk>/atualizar', views.QuestionUpdateView.as_view(), name="question-update")
]