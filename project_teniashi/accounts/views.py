from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.views.generic import CreateView, ListView, View
from .models import User
from accounts.forms import UserCreateForm, UserLoginForm, UserPasswordChange

from django.contrib.auth import (
    get_user_model, logout as auth_logout
)

User = get_user_model()

class UserTopView(ListView):
    template_name = 'registration/user_top.html'
    model = User

class UserCreate(CreateView):
    model = User
    form_class = UserCreateForm
    template_name = 'registration/create.html'
    success_url = reverse_lazy('index')    

class UserLogin(LoginView):
    template_name = 'registration/login.html'
    authentication_form = UserLoginForm

    # def post(self, request, *args, **kwargs):

class UserLogout(LogoutView):
    pass

class MyPasswordChange(PasswordChangeView):
    form_class =  UserPasswordChange #あえてUserPasswordChangeにする必要はない、importが面倒だっただけ
    success_url = reverse_lazy('registration/passwordchangedone.html')
    template_name = 'registration/passwordchange.html'

class UserPasswordChangeDone(PasswordChangeDoneView):
    template_name = 'registration/passwordchangedone.html'

