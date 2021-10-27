# aspi <-> web app  json
from rest_framework import serializers
from .models import Consultorio

class ConsultorioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultorio
        fields = '__all__'