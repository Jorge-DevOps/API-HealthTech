from django import urls
from django.contrib import admin
from django.urls import path, re_path, include
from django.urls import path, include
from Apps.share import cita
from login import views
from django.contrib.auth.views import LoginView
from .router import router
from Apps.JoinUsuarios import views as viewsExcel



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('login/', views.my_view,  name="login"),
    path('api/Excel', viewsExcel.export_excel),
    path('',include('Apps.LoginUsuarios.urls')),
    path('',include('Apps.share.cita.urls')),
    path('',include('Apps.share.medico.urls')),
    path('',include('Apps.share.paciente.urls')),
]
