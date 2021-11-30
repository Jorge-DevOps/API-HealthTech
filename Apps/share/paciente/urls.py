from django.conf.urls import url
from django.urls import path
from Apps.share.paciente import views as viewsPaciente

urlpatterns = [
    path('api/paciente/generarCertificadoPaciente',viewsPaciente.generarCertificadoPaciente),
]