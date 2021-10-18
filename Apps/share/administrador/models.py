from django.db import models

# Create your models here.
class Administrador(models.Model):
    id_usuario = models.OneToOneField(
        'Usuario', models.DO_NOTHING, db_column='id_usuario', primary_key=True)

    class Meta:
        managed = False
        db_table = 'administrador'