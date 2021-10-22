from rest_framework import serializers
from . import models

class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.horarioMedico  
        exclude = ['is_removed', 'created', 'modified']