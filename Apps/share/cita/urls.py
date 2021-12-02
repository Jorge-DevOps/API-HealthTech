from django.conf.urls import url
from django.urls import path
from Apps.share.cita import views as viewsCitaMedicos
from Apps.share.cita import views as viewsCitas
from Apps.share.cita import views as viewsInformeCitas

urlpatterns = [
    path('api/cita/traerMedicos',viewsCitaMedicos.traerMedicos),
    path('api/cita/traerHorarios',viewsCitas.horariosDisponibles),
    path('api/informeCita',viewsInformeCitas.export_informeCitas),
    path('api/traerCita',viewsCitas.lista_citas),
    path('api/cita/consultarIdPaciente',viewsCitas.consultarIdPaciente),
    #url(r'^api/cita/traerHorarios/(?P<pk>\d+)/$', HorariosDisponibles),
]