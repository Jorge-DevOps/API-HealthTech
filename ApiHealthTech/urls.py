from django.contrib import admin
from django.urls import path, re_path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^', include('Apps.share.horarioMedico.urls')),
    re_path(r'^', include('Apps.usuario.urls')),
    
]