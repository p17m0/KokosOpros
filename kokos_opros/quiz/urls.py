from django.urls import path, include
from .views import answer, quizs, index

app_name = 'quiz'

urlpatterns = [
    path('', index, name='index'),
    path('quiz/<int:id>/', quizs, name='quizs'),
    path('quizy/<int:id>/answer/<int:id_q>/', answer, name='answer')
]
