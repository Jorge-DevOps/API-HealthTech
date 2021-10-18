from django.db import models
from share.paciente.models import medico
from share.medico.models import paciente
from share.administrador.models import administrador

# USUARIO
class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    tipo_documento = models.CharField(max_length=10)
    numero_documento = models.CharField(max_length=50)
    nombre_usuario = models.CharField(max_length=100)
    contrasena = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    sexo = models.CharField(max_length=30)
    fecha_nacimiento = models.DateField()
    grupo_sanguineo = models.CharField(max_length=50)
    estrato = models.IntegerField()
    estado_civil = models.CharField(max_length=50)
    id_perfil = models.ForeignKey(
        Perfil, models.DO_NOTHING, db_column='id_perfil')

    class Meta:
        managed = False
        db_table = 'usuario'
