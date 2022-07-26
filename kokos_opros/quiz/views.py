from django.shortcuts import get_object_or_404, redirect, render
from .models import *
from .forms import *


def answer(request, id, id_q):
    quiz = get_object_or_404(Quiz, pk=id)
    question = quiz.questions.get(id=id_q)
    answers = question.answers.all()
    right_answer = question.num_of_right_answer
    form = QuestionForm
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            answer = int(form.cleaned_data['num_of_answer'])
            print(answer == right_answer)
            if answer == right_answer:
                user = request.user
                user.golden_coins += 1
                user.save()
                return redirect('quiz:quizs', id=id)
            return redirect('quiz:quizs', id=id)
       
    context = {
        'question': question,
        'answers': answers,
        'form': form,
    }
    return render(request, 'quiz/answer.html', context)


def quizs(request, id):
    quiz = get_object_or_404(Quiz, pk=id)
    questions = quiz.questions.all()
    count = len(questions)
    context = {
        'count': count,
        'questions': questions,
        'id': id,
    }
    return render(request, 'quiz/quizs.html', context)


def index(request):
    quizs = Quiz.objects.all()
    context = {
        'quizs': quizs,
    }
    return render(request, 'quiz/index.html', context)
