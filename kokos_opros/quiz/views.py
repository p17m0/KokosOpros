from django.shortcuts import get_object_or_404, render
from .models import *


def quizs(request, id):
    quiz = get_object_or_404(Quiz, id=id)
    questions = quiz.questions.all()
    if request.method == 'POST':
        print(request.POST)

    context = {
        'quizs': questions,
    }
    return render(request, 'quiz/quizs.html', context)


def index(request):
    quizs = Quiz.objects.all()
    context = {
        'quizs': quizs,
    }
    return render(request, 'quiz/index.html', context)
