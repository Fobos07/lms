from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, CreateView

from user_auth.models import NewUserCreationForm


class AboutMeView(LoginRequiredMixin, TemplateView):
    template_name = "auth/about-me.html"


class RegisterView(CreateView):
    form_class = NewUserCreationForm
    template_name = 'auth/register.html'
    success_url = reverse_lazy('user_auth:about')

    def form_valid(self, form):
        response = super().form_valid(form)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        email = form.cleaned_data.get('email')
        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')
        user = authenticate(
            self.request,
            username=username,
            password=password,
            email=email,
            first_name=first_name,
            last_name=last_name,
        )
        user.groups.add(1)
        login(request=self.request, user=user)
        return response


def login_view(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('/admin/')
        return render(request, 'auth/login.html')

    username = request.POST["username"]
    password = request.POST["password"]
    print(request.user)
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('/admin/')

    return render(request, 'auth/login.html', context={'error': 'invalid login credentials'})


def logout_view(request: HttpRequest):
    logout(request)
    return redirect(reverse('user_auth:login'))


def set_coockie_view(request: HttpRequest) -> HttpResponse:
    response = HttpResponse('Cookie set')
    response.set_cookie('fizz', 'buzz', max_age=3600)
    return response


def get_coockie_view(request: HttpRequest) -> HttpResponse:
    value = request.COOKIES.get('fizz')
    return HttpResponse(f'Coockie: {value!r}')


def set_session_view(request: HttpRequest) -> HttpResponse:
    request.session['foobar'] = 'spameggs'
    return HttpResponse('Session set!')


def get_session_view(request: HttpRequest) -> HttpResponse:
    value = request.session.get('foobar', 'default value')
    return HttpResponse(f'Session: {value!r}')
