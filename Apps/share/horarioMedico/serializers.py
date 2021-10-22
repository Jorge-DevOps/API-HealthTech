from rest_framework import serializers
from.models import horarioMedico

class HorarioMedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = horarioMedico
        fields = '__all__'