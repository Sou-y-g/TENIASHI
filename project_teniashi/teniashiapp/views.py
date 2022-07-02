from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, DeleteView, ListView, DetailView

from .forms import ProjectFrom
from .models import project

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
    model = project
    context_object_name = 'project_list'

# class result():
#     def kekak(self):
#         print("a")

class delete(DeleteView):
    template_name = 'teniashiapp/delete.html'

class createproject(CreateView):
    template_name = 'teniashiapp/createproject.html'
    model = project
    form_class = ProjectFrom
    success_url = reverse_lazy('list')

    def get_form(self):
        form = super(createproject, self).get_form()
        form.fields['project_num'].label = '課題No.'
        form.fields['wall_name'].label = 'WallName'
        form.fields['setter_name'].label = 'セッター名'
        form.fields['project_num'].required = True
        form.fields['wall_name'].required = True
        form.fields['setter_name'].required = True
        form.fields['image'].required = True
        return form

class detailproject(DetailView):
    template_name = 'teniashiapp/detailproject.html'
