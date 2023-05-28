from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


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


def set_coockie_view(request: HttpRequest) -> HttpResponse:
    response = HttpResponse('Cookie set')
    response.set_cookie('fizz', 'buzz', max_age=3600)
    return response


def get_coockie_view(request: HttpRequest) -> HttpResponse:
    value = request.COOKIES.get('fizz')
    return HttpResponse(f'Coockie: {value!r}')