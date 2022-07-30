from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from .models import User


User = get_user_model()

class UserCreateForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='ユーザー名')
    password = forms.CharField(label='パスワード', widget=forms.PasswordInput())

class UserPasswordChange(PasswordChangeForm):
    pass
