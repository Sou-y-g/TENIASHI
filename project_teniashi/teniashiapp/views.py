from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, DeleteView, ListView, DetailView
from . import models

class index(TemplateView):
    template_name = 'teniashiapp/index.html'

class honsen(TemplateView):
    template_name = 'teniashiapp/honesen.html'

class yosen(TemplateView):
    template_name = 'teniashiapp/yosen.html'

class rule(TemplateView):
    template_name = 'teniashiapp/rule.html'

class projectlist(ListView):
    template_name = 'teniashiapp/projectlist.html'
    model = models.project
    context_object_name = 'project_list'

# class result():
#     def kekak(self):
#         print("a")

class delete(DeleteView):
    template_name = 'teniashiapp/delete.html'

class createproject(CreateView):
    template_name = 'teniashiapp/createproject.html'

class detailproject(DetailView):
    template_name = 'teniashiapp/detailproject.html'
