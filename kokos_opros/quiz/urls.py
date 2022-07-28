from django.urls import path
from . import views

app_name = 'quiz'

urlpatterns = [
    path('', views.index, name='index'),
    path('donequiz/', views.done_quizs, name='done_quizs'),
    path('quiz/<int:id>/', views.quizs, name='quizs'),
    path('quiz/<int:id>/answer/<int:id_q>/', views.answer, name='answer'),
    path('quiz/start/<int:id>/', views.start_quiz, name='start'),
]
