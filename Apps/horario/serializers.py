from rest_framework import serializers
from.models import horario

class HorarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = horario
        fields = '__all__'