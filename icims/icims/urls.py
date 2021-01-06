from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from jobApp import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('jobApp.urls')),
    path('register/', v.registration, name='register')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)