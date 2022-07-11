from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, CreateView, View

from django.contrib.auth import (
    get_user_model, logout as auth_logout
)
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()

class Top(TemplateView):
    template_name = 'top.html'

class ProfileView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        return render(self.request,'registration/profile.html')

class SignUpView(CreateView):
    from_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class DeleteView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        user = User.objects.get(username=self.request.user.username)
        user.is_active = False
        user.save()
        auth_logout(self.request)
        return render(self.request, 'registration/delete_complete.html')