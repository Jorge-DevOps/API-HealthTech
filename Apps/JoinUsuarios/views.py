from.serializers import Jointableserializer
from.models import JoinTablesmodel
from rest_framework import serializers, viewsets
# Create your views here.
class Jointableapi(viewsets.ModelViewSet):
    queryset=JoinTablesmodel.objects.raw('SELECT id_usuario, tipo_documento, numero_documento, nombre_usuario, contrasena, correo, telefono, sexo, fecha_nacimiento, grupo_sanguineo, estrato, estado_civil, id_perfil FROM  administrador UNION SELECT  id_usuario, tipo_documento, numero_documento, nombre_usuario, contrasena, correo, telefono, sexo, fecha_nacimiento, grupo_sanguineo, estrato, estado_civil, id_perfil FROM medico UNION SELECT  id_usuario, tipo_documento, numero_documento, nombre_usuario, contrasena, correo, telefono, sexo, fecha_nacimiento, grupo_sanguineo, estrato, estado_civil, id_perfil FROM paciente')
    serializer_class = Jointableserializer