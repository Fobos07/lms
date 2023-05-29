from django.contrib.auth.views import LoginView
from django.urls import path

from user_auth.views import login_view, get_coockie_view, set_coockie_view, set_session_view, get_session_view, \
    logout_view, AboutMeView, RegisterView

app_name = 'user_auth'

urlpatterns = [
    path('login/',
         LoginView.as_view(
             template_name='auth/login.html',
             redirect_authenticated_user=True,
         ),
         name='login'),
    path('coockie/get/', get_coockie_view, name='get-coockie'),
    path('coockie/set/', set_coockie_view, name='set-coockie'),
    path('session/set/', set_session_view, name='set-session'),
    path('session/get/', get_session_view, name='get-session'),
    path('logout/', logout_view, name='logout'),
    path('about/', AboutMeView.as_view(), name='about'),
    path('register/', RegisterView.as_view(), name='register'),

]
