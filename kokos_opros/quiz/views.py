from django.contrib.auth.decorators import login_required
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


@login_required
def answer(request, id, id_q):
    """
    Отображение формы ответа, вопроса и вариантов ответа.
    """
    quiz = get_object_or_404(Quiz, pk=id)
    question = quiz.questions.get(id=id_q)
    answers = question.answers.all()
    last_question = quiz.questions.last()
    right_answer = question.num_of_right_answer

    form = QuestionForm
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            answer = int(form.cleaned_data['num_of_answer'])
            if answer == right_answer:
                user = request.user
                user.right_answers += 1
                user.save()

            if question.id == last_question.id:
                if user.right_answers == quiz.min_right_answers:
                    user.golden_coins += quiz.difficult
                    DoneQuiz.objects.create(user=request.user,
                                            quiz=quiz,
                                            done=True)
                else:
                    DoneQuiz.objects.create(user=request.user,
                                            quiz=quiz,
                                            done=False)
                user.right_answers = 0
                user.save()
                return redirect('quiz:index')
            return redirect('quiz:answer', id=id, id_q=id_q+1)

    context = {
        'question': question,
        'answers': answers,
        'form': form,
    }
    return render(request, 'quiz/answer.html', context)


@login_required
def start_quiz(request, id):
    """
    Запускает тест.
    """
    quiz = get_object_or_404(Quiz, pk=id)
    question = quiz.questions.first()
    return redirect('quiz:answer', id, question.id)


@login_required
def quizs(request, id):
    """
    Для отображения всех вопросов.
    """
    quiz = get_object_or_404(Quiz, pk=id)
    questions = quiz.questions.all()
    count = len(questions)
    context = {
        'count': count,
        'page_obj': pagina(request, questions),
        'id': id,
    }
    return render(request, 'quiz/quizs.html', context)


@login_required
def done_quizs(request):
    """
    Страница выполненных тестов. И итога - пройден или нет.
    """
    quizs = request.user.userdonequizs.all()
    print(quizs)
    context = {
        'page_obj': pagina(request, quizs),
    }
    return render(request, 'quiz/done_quizs.html', context)


@login_required
def index(request):
    """
    Главная страница. Отображение всех непройденных Quiz.
    """
    donequizs = DoneQuiz.objects.filter(user=request.user).values('quiz_id')
    quizs = Quiz.objects.exclude(id__in=donequizs)
    context = {
        'page_obj': pagina(request, quizs),
    }
    return render(request, 'quiz/index.html', context)
