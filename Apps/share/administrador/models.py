from django.db import models

from Apps.usuario.models import usuario

# Create your models here.
class Administrador(usuario):

    class Meta:
        managed = False
        db_table = 'administrador'