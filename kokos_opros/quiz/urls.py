from django.urls import path, include
from .views import answer, quizs, start_quiz, index

app_name = 'quiz'

urlpatterns = [
    path('', index, name='index'),
    path('quiz/<int:id>/', quizs, name='quizs'),
    path('quiz/<int:id>/answer/<int:id_q>/', answer, name='answer'),
    path('quiz/start/<int:id>/<int:count>/', start_quiz, name='start')
]
