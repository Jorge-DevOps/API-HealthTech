# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


# AGENDA
class Agenda(models.Model):
    id_agenda = models.AutoField(primary_key=True)
    id_horario_medico = models.ForeignKey(
        'HorarioMedico', models.DO_NOTHING, db_column='id_horario_medico')
    id_consultorio = models.ForeignKey(
        'Consultorio', models.DO_NOTHING, db_column='id_consultorio')

    class Meta:
        managed = False
        db_table = 'agenda'


class Medico(models.Model):
    id_usuario = models.OneToOneField(
        'Usuario', models.DO_NOTHING, db_column='id_usuario', primary_key=True)
    id_agenda = models.ForeignKey(
        Agenda, models.DO_NOTHING, db_column='id_agenda')
    id_especialidad = models.ForeignKey(
        Especialidad, models.DO_NOTHING, db_column='id_especialidad')

    class Meta:
        managed = False
        db_table = 'medico'


class Cita(models.Model):
    id_cita = models.AutoField(primary_key=True)
    id_agenda = models.ForeignKey(
        Agenda, models.DO_NOTHING, db_column='id_agenda')
    id_usuario = models.ForeignKey(
        'Paciente', models.DO_NOTHING, db_column='id_usuario')
    fecha = models.DateField()
    id_horario = models.ForeignKey(
        'Horario', models.DO_NOTHING, db_column='id_horario')

    class Meta:
        managed = False
        db_table = 'cita'


class HorarioMedico(models.Model):
    id_horario_medico = models.AutoField(primary_key=True)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

    class Meta:
        managed = False
        db_table = 'horario_medico'


class Consultorio(models.Model):
    id_consultorio = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    codigo = models.CharField(max_length=50)
    piso = models.IntegerField()
    estado = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'consultorio'


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


class Paciente(models.Model):
    id_usuario = models.OneToOneField(
        'Usuario', models.DO_NOTHING, db_column='id_usuario', primary_key=True)
    contrato = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'paciente'


class Administrador(models.Model):
    id_usuario = models.OneToOneField(
        'Usuario', models.DO_NOTHING, db_column='id_usuario', primary_key=True)

    class Meta:
        managed = False
        db_table = 'administrador'


class Horario(models.Model):
    id_horario = models.AutoField(primary_key=True)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

    class Meta:
        managed = False
        db_table = 'horario'


class Perfil(models.Model):
    id_perfil = models.AutoField(primary_key=True)
    rol = models.CharField(max_length=50)
    observacion = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'perfil'


# ORDEN
class OrdenRemision(models.Model):
    id_orden = models.AutoField(primary_key=True)
    id_usuario_paciente = models.ForeignKey(
        'Paciente', models.DO_NOTHING, db_column='id_usuario_paciente')
    id_usuario_medico = models.ForeignKey(
        Medico, models.DO_NOTHING, db_column='id_usuario_medico')
    id_especialidad = models.ForeignKey(
        Especialidad, models.DO_NOTHING, db_column='id_especialidad')

    class Meta:
        managed = False
        db_table = 'orden_remision'


class Paciente(models.Model):
    id_usuario = models.OneToOneField(
        'Usuario', models.DO_NOTHING, db_column='id_usuario', primary_key=True)
    contrato = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'paciente'


class Medico(models.Model):
    id_usuario = models.OneToOneField(
        'Usuario', models.DO_NOTHING, db_column='id_usuario', primary_key=True)
    id_agenda = models.ForeignKey(
        Agenda, models.DO_NOTHING, db_column='id_agenda')
    id_especialidad = models.ForeignKey(
        Especialidad, models.DO_NOTHING, db_column='id_especialidad')

    class Meta:
        managed = False
        db_table = 'medico'


class Especialidad(models.Model):
    id_especialidad = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    estado = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'especialidad'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey(
        'DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
