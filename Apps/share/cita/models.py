from django.db import models
from Apps.agenda.models import Agenda
#from Apps.share.medico.models import Medico
from Apps.share.paciente.models import Paciente
from Apps.horario.models import horario
from django.db.models import Q, query
from django.db import connection
from django.http import HttpResponse
# Create your models here.
#Horario= horario.objects.filter(Q(hora_inicio=query)|Q())

def traerMedicos(request):
    
    with connection.cursor() as cursor:
            cursor.execute("SELECT  username, id_agenda FROM  medico ")
            rawData = cursor.fetchall()
            result = []
            for r in rawData:
                result.append(list(r))
                rows = result        
    response = HttpResponse(content_type='application/json')
    return result

class Cita(models.Model):
    id_cita = models.AutoField(primary_key=True)
    id_agenda = models.ForeignKey(
        Agenda, models.DO_NOTHING, db_column='id_agenda')
    id_usuario = models.ForeignKey(
        Paciente, models.DO_NOTHING, db_column='id_usuario')
    fecha = models.DateField()
    id_horario = models.ForeignKey(
        horario, models.DO_NOTHING, db_column='id_horario')
    Medico=traerMedicos
    #medicos = models.ManyToManyField(Medico)
    class Meta:
        managed = False
        db_table = 'cita'