from operator import index
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index.as_view(), name='index'), 
    path('honsen', views.honsen.as_view(), name='honsen'),
    path('yosen', views.yosen.as_view(), name='yosen'),
    path('yosen/rule', views.rule.as_view(), name='rule'),
    path('yosen/projectlist', views.projectlist.as_view(), name='list'),
    path('yosen/createproject', views.createproject.as_view(), name='create'),
    path('yosen/<int:pk>/projectdetail', views.detailproject.as_view(), name='detail'),
    path('yosen/<int:pk>/delete', views.DeleteProject.as_view(), name='delete'),
    path('yosen/<int:pk>/update', views.Update_project.as_view(), name='update'),

]
