from django.contrib import admin
from django.urls import path, include
from jobApp import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('jobApp.urls')),
    path('register/', v.registration, name='register')
]
