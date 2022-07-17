from django.urls import path

from . import views

from django.contrib.auth import views as auth_view

urlpatterns = [
    path('users-sign-up', views.sign_up, name='users-sign-up'),
    # ===> class based views below
    # ! [NOTE] specify your login redirect url in your settings.py file
    path('login/', auth_view.LoginView.as_view(template_name = 'authentication/login.html'), name='users-login'),
    path('logout/', auth_view.LogoutView.as_view(template_name = 'authentication/logout.html'), name='users-logout'),
]