from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from .models import *
from .forms import *


def pagina(request, qui):
    """
    Пагинация.
    """
    paginator = Paginator(qui, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj


def answer(request, id, id_q):
    """
    Отображение формы ответа, вопроса и вариантов ответа.
    """
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


# def start_quiz(request, id, count):
#     for i in range(1, count+1):
#         answer(request, id, i)


def quizs(request, id):
    """
    Для отображения всех вопросов.
    """
    quiz = get_object_or_404(Quiz, pk=id)
    questions = quiz.questions.all()
    count = len(questions)
    # start = start_quiz(request, id, count)
    context = {
        'count': count,
        'page_obj': pagina(request, questions),
        'id': id,
    }
    return render(request, 'quiz/quizs.html', context)


def index(request):
    """
    Главнаця страница. Отображение всех Quiz.
    """
    quizs = Quiz.objects.all()
    context = {
        'page_obj': pagina(request, quizs),
    }
    return render(request, 'quiz/index.html', context)
