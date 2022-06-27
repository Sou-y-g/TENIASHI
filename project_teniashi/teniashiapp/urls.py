from operator import index
from unicodedata import name
from unittest import result
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index.as_view(), name='index'), 
    path('/honsen', views.honsen.as_view(), name='honsen'),
    path('/yosen', views.yosen.as_view(), name='yosen'),
    path('/rule', views.rule.as_view(), name='rule'),
    path('/projectlist', views.projectlist.as_view(), name='projectlist'),
    # path('/yosen/result', views.result, name='result')
]
