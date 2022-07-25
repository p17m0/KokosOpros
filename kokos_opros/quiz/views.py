from django.shortcuts import get_object_or_404, render
from .models import *
from .forms import *


def quizs(request, id):
    quiz = get_object_or_404(Quiz, id=id)
    questions = quiz.questions.all()
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.cleaned_data['answer']
            
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
