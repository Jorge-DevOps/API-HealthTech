from django.conf.urls import url
from django.urls import path
from Apps.share.medico import views as viewsMedico

urlpatterns = [
    path('api/medico/traerAgendaMedico',viewsMedico.traerAgendaMedico),
]