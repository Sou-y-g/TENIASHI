from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, CreateView, DeleteView, ListView, DetailView, UpdateView

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

# class result():
#     def kekak(self):
#         print("a")

class DeleteProject(DeleteView):
    template_name = 'teniashiapp/delete.html'
    model = project
    success_url = reverse_lazy('list')

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
        return form

class detailproject(DetailView):
    template_name = 'teniashiapp/detailproject.html'
    model = project

class Update_project(UpdateView):
    template_name = 'teniashiapp/update.html'
    model = project
    fields = '__all__'

    def get_success_url(self):
        return reverse('detail', kwargs={'pk':self.object.id})