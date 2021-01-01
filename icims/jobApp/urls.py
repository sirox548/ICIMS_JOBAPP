from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('company', views.company, name='company'),
    path('login', views.login, name='login'),
]