# aspi <-> web app  json
from rest_framework import serializers
from django.contrib.auth.models import User
from.models import Medico

class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = '__all__'
        extra_kwargs = {'password':{'write_only': True}}
    def create(self, validated_data):
        user = User(
            username=validated_data['email']
        )
        medico = Medico(
            tipo_documento=validated_data['tipo_documento'],
            numero_documento=validated_data['numero_documento'],
            password=validated_data['password'],
            username=validated_data['username'],
            email=validated_data['email'],
            telefono=validated_data['telefono'],
            sexo=validated_data['sexo'],
            fecha_nacimiento=validated_data['fecha_nacimiento'],
            grupo_sanguineo=validated_data['grupo_sanguineo'],
            estrato=validated_data['estrato'],
            estado_civil=validated_data['estado_civil'],
            id_perfil=validated_data['id_perfil'],
            id_agenda=validated_data['id_agenda'],
            id_especialidad=validated_data['id_especialidad'],
            
        )
        medico.save()
        user.set_password(validated_data['password'])
        user.save()
        return medico 