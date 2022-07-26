from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from .models import *
from .forms import *


def pagina(request, qui):
    paginator = Paginator(qui, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj


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
        'answers': pagina(request, answers),
        'form': form,
    }
    return render(request, 'quiz/answer.html', context)


def quizs(request, id):
    quiz = get_object_or_404(Quiz, pk=id)
    questions = quiz.questions.all()
    count = len(questions)
    context = {
        'count': count,
        'page_obj': pagina(request, questions),
        'id': id,
    }
    return render(request, 'quiz/quizs.html', context)


def index(request):
    quizs = Quiz.objects.all()
    context = {
        'page_obj': quizs,
    }
    return render(request, 'quiz/index.html', context)
