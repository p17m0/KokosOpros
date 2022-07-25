from django.urls import path, include
from .views import quizs, index

app_name = 'quiz'

urlpatterns = [
    path('', index, name='index'),
    path('quiz/<int:id>/', quizs, name='quizs')
]
