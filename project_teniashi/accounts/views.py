from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView
from . forms import UserCreateForm

#アカウント作成
class Create_account(CreateView):
    def post(self, request, *args, **kwargs):
        form = UserCreateForm(data = request.POST)
        if form.is_valid():
            form.save()
            #フォームからusernameを読み取る
            username = form.cleaned_data.get('username')
            #フォームからpassword1を読み取る
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        return render(request, 'create.html', {'form': form,})

    def get(self, request, *args, **kawrgs):
        form = UserCreateForm(request.POST)
        return render(request, 'create.html', {'form': form,})

create_account = Create_account.as_view()