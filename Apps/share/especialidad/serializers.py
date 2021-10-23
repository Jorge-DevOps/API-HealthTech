# aspi <-> web app  json
from rest_framework import serializers
from .models import especialidad

class EspecialidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = especialidad
        fields = '__all__'