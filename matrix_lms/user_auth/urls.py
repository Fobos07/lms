from django.contrib.auth.views import LoginView
from django.urls import path

from user_auth.views import login_view, get_coockie_view, set_coockie_view

app_name = 'user_auth'


urlpatterns = [
    # path('login/', login_view, name='login'),
    path('login/',
         LoginView.as_view(
             template_name='auth/login.html',
             redirect_authenticated_user=True,
         ),
         name='login'),
    path('coockie/get/', get_coockie_view, name='get-coockie'),
    path('coockie/set/', set_coockie_view, name='set-coockie')
]