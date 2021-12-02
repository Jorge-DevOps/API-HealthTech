from django.db.models import fields
from rest_framework import serializers
from.models import LoginModel

class SerializerLogin(serializers.ModelSerializer):
    class Meta:
        model=LoginModel
        fields=['id_usuario', 'tipo_documento', 'numero_documento', 'contrasena', 'id_perfil']