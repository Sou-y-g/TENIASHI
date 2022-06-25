from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, DeleteView, ListView, DetailView

class index(TemplateView):
    template_name = 'teniashiapp/index.html'

class honsen(TemplateView):
    template_name = 'teniashiapp/honesen.html'

class yosen(TemplateView):
    template_name = 'teniashiapp/yosen.html'

class projectlist(ListView):
    template_name = 'teniashiapp/projectlist'

class delete(DeleteView):
    template_name = 'teniashiapp/delete.html'

class createproject(CreateView):
    template_name = 'teniashiapp/createproject.html'

class detailproject(DetailView):
    template_name = 'teniashiapp/detailproject.html'
