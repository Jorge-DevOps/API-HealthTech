from django.db.models import fields
from rest_framework import serializers
from.models import JoinTablesmodel

class Jointableserializer(serializers.ModelSerializer):
    class Meta:
        model=JoinTablesmodel
        fields=['tipo_documento','numero_documento','nombre_usuario','contrasena','correo','telefono','sexo','fecha_nacimiento','grupo_sanguineo','estrato','estado_civil','id_perfil']