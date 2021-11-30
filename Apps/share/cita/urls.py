from django.conf.urls import url
from django.urls import path
from Apps.share.cita import views as viewsCitaMedicos
from Apps.share.cita.views import HorariosDisponibles
from Apps.share.cita.views import Citas
from Apps.share.cita import views as viewsInformeCitas

urlpatterns = [
    path('api/cita/traerMedicos',viewsCitaMedicos.traerMedicos),
    path('api/cita/traerHorarios',HorariosDisponibles.as_view()),
    path('api/informeCita',viewsInformeCitas.export_informeCitas),
    path('api/traerCita',Citas.lista_citas),
    #url(r'^api/cita/traerHorarios/(?P<pk>\d+)/$', HorariosDisponibles),
]