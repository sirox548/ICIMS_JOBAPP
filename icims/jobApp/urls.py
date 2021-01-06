from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('company', views.company, name='company'),
    path('login', views.loginpage, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('account', views.account, name='account'),
    path('accountupdate', views.updateAccount, name='accountupdate'),
    path('postjob', views.postJob, name='postjob'),
]