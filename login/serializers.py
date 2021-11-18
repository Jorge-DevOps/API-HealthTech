from rest_framework import serializers
from Apps.share.medico.models import medico

class LoginMedico(serializers.ModelSerializer):
    class Meta:
        model = medico
        fields = '__all__'