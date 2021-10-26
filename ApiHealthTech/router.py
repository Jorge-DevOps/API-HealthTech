from Apps.share.medico.viewsets import MedicoViewset
from Apps.share.especialidad.viewsets import EspecialidadViewset
from Apps.share.consultorio.viewsets import ConsultorioViewset

from rest_framework import routers

router = routers.DefaultRouter()

#Registrar las rutas
router.register('medico', MedicoViewset)
#router.register('especialidad', EspecialidadViewset)
#router.register('consultorio', ConsultorioViewset)

# Localhost:p/api/medico/5
# GET, POST, UPDATE , DELETE