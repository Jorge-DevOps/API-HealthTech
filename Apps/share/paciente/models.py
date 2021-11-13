from django.db import models
from Apps.usuario.models import usuario

# Create your models here.
class Paciente(usuario):
    
    contrato = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'paciente'

