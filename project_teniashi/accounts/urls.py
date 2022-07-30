from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('create/', views.UserCreate.as_view(), name='create'),
    path('user_top/', views.UserTopView.as_view(), name='user_top'),
    path('login/', views.UserLogin.as_view(), name='login'),
    path('logout/', views.UserLogout.as_view(), name='logout'),
    path('passwordchange/', views.MyPasswordChange.as_view(), name='passwordchange'),
    path('passwordchangedone/', views.UserPasswordChangeDone.as_view(), name='passwordchangedone'),

]