from django.urls import path
from .views import (answer,
                    quizs,
                    start_quiz,
                    done_quizs,
                    index)

app_name = 'quiz'

urlpatterns = [
    path('', index, name='index'),
    path('donequiz/', done_quizs, name='done_quizs'),
    path('quiz/<int:id>/', quizs, name='quizs'),
    path('quiz/<int:id>/answer/<int:id_q>/', answer, name='answer'),
    path('quiz/start/<int:id>/', start_quiz, name='start'),
]
