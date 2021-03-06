# Generated by Django 3.2.8 on 2021-11-19 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('id_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_documento', models.CharField(max_length=10)),
                ('numero_documento', models.CharField(max_length=50)),
                ('nombre_usuario', models.CharField(max_length=100)),
                ('contrasena', models.CharField(max_length=100)),
                ('correo', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=20)),
                ('sexo', models.CharField(max_length=30)),
                ('fecha_nacimiento', models.DateField()),
                ('grupo_sanguineo', models.CharField(max_length=50)),
                ('estrato', models.IntegerField()),
                ('estado_civil', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'administrador',
                'managed': False,
            },
        ),
    ]
