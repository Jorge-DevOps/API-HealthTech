from Apps.share.administrador.viewsets import AdministradorViewset
from Apps.share.medico.viewsets import MedicoViewset
from Apps.share.especialidad.viewsets import EspecialidadViewset
from Apps.share.consultorio.viewsets import ConsultorioViewset
from Apps.share.horarioMedico.views import HorarioMedicoView
from Apps.share.paciente.viewsets import PacienteViewset
from Apps.horario.viewsets import HorarioViewset
from Apps.JoinUsuarios.views import Jointableapi
from Apps.agenda.viewsets import AgendaViewset
from Apps.share.cita.viewsets import CitaViewset
from rest_framework import routers




router = routers.DefaultRouter()

#Registrar las rutas
router.register('medico', MedicoViewset)
router.register('especialidad', EspecialidadViewset)
router.register('consultorio', ConsultorioViewset)
router.register('horarioMedico', HorarioMedicoView)
router.register('administrador', AdministradorViewset)
router.register('paciente', PacienteViewset)
router.register('horario', HorarioViewset)
router.register('usuarios',Jointableapi)
router.register('agenda',AgendaViewset)
router.register('cita',CitaViewset)

# Localhost:p/api/medico/5
# GET, POST, UPDATE , DELETE
