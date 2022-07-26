from django.views.generic import CreateView
from django.shortcuts import render
from django.urls import reverse_lazy

from .forms import CreationForm
from .service import hex_code_colors


class SignUp(CreateView):
    form_class = CreationForm
    # После успешной регистрации перенаправляем пользователя на главную.
    success_url = reverse_lazy('quiz:index')
    template_name = 'users/signup.html'


def profile(request):
    user = request.user
    color = hex_code_colors()
    context = {'user': user,
               'color': color}
    return render(request, 'users/profile.html', context)
