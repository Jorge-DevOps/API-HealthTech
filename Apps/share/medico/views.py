from django.shortcuts import render
from django.db import connection
from django.http import HttpResponse
import json

from json import loads

def traerAgendaMedico(request):

    dic = loads(request.body)

    dataRequestUsername=dic['username']

    with connection.cursor() as cursor:
        cursor.execute("""SELECT paciente.username, cita.fecha, horario.hora_inicio, horario.hora_fin
                        FROM paciente
                        JOIN cita ON (paciente.id_usuario = cita.id_usuario)
                        JOIN horario ON (cita.id_horario = horario.id_horario)
                        JOIN agenda ON (cita.id_agenda = agenda.id_agenda)
                        JOIN medico ON (medico.id_agenda = agenda.id_agenda)
                        WHERE medico.email = %s""", [dataRequestUsername]
                    )
                    
        result = dictfetchall(cursor)

    response = HttpResponse(json.dumps(result, indent=4, default=str),content_type='application/json')
    
    return response

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]