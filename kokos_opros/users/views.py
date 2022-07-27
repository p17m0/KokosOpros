from multiprocessing import context
from django.views.generic import CreateView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model

from quiz.models import DoneQuiz

from .forms import CreationForm
from .service import hex_code_colors


User = get_user_model()


class SignUp(CreateView):
    form_class = CreationForm
    # После успешной регистрации перенаправляем пользователя на главную.
    success_url = reverse_lazy('quiz:index')
    template_name = 'users/signup.html'


def profile(request):
    user = request.user
    context = {'user': user}
    return render(request, 'users/profile.html', context)


def buycolor(request):
    user = request.user
    if user.golden_coins > 0 or user.golden_coins <= 5:
        color = hex_code_colors()
        user.color = color
        user.golden_coins -= 5
        user.save()
    return redirect('users:profile')


def list_of_users(request):
    users = User.objects.all()
    DoneQuiz
    context = {'users': users,}
    return render(request, 'users/list_users.html', context)
