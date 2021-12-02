from django.shortcuts import render
from django.db import connection
from django.views.generic.base import View
from rest_framework.generics import UpdateAPIView
from xlwt.Formatting import Font
from django.http import HttpResponse
import xlwt 
from Apps.share.medico.models import Medico
from Apps.horario.models import horario
from Apps.agenda.models import Agenda
import json
from json import loads
from django.views import View

from rest_framework import permissions
from django.views.generic.edit import UpdateView
from knox.views import LoginView as KnoxLoginView
#from knox.views import LoginView as KnoxLoginView
# Create your views here.

def traerMedicos(request):
    consulta = list(Medico.objects.values('username', 'id_agenda'))
    response = HttpResponse(json.dumps(consulta, indent=4), content_type='application/json')
    return response


def horariosDisponibles(request):

  dic = loads(request.body)

  idAgenda=dic['id_agenda']
  dataRequestFecha=dic['fecha']

  #with connection.cursor() as cursor:
  #      cursor.execute("""SELECT agenda.id_agenda
  #                        FROM agenda
  #                        JOIN medico ON (agenda.id_agenda = medico.id_agenda)
  #                        WHERE medico.email = %s""", [dataRequestUsername]
  #                    )
  #                  
  #      result = dictfetchall(cursor)
  
  #idAgenda = result[0]['id_agenda']
  
  with connection.cursor() as cursor:
        cursor.execute("""SELECT * 
                          FROM horario 
                          WHERE horario.id_horario NOT IN 
                          ( 
                          SELECT cita.id_horario 
                          FROM cita 
                          WHERE cita.fecha =%s AND 
                          cita.id_agenda =%s
                          )""", [dataRequestFecha, idAgenda]
                      )
                    
        result = dictfetchall(cursor)

  response = HttpResponse(json.dumps(result, indent=4, default=str),content_type='application/json')
  
  return response

def export_informeCitas(request):
      response = HttpResponse(content_type='application/ms-excel')
      #nesecitamos enviarle el contenido
      response['Content-Disposition'] = 'attachment; filename=Ep_' + \
        str('informeCitasMedicas')+'.xls'
      wb = xlwt.Workbook(encoding='utf-8')
      ws=wb.add_sheet('Cita')
      row_num = 0
      font_style=xlwt.XFStyle()
      font_style.font.bold =True

      columns = ['id_cita','id_agenda','id_usuario','fecha','id_horario']

      for col_num in range(len(columns)):
        ws.write(row_num,col_num,columns[col_num], font_style)
      font_style=xlwt.XFStyle()

      with connection.cursor() as cursor:
        cursor.execute("SELECT id_cita, id_agenda, id_usuario, fecha, id_horario FROM  cita ")
        rawData = cursor.fetchall()
        result = []
        for r in rawData:
          result.append(list(r))
        rows = result

      for row in rows:
        row_num+=1
        
        for col_num in range(len(row)):
          ws.write(row_num,col_num,str(row[col_num]), font_style)
      wb.save(response)
      return response
from json import loads

def lista_citas(request):

    dic = loads(request.body)

    dataRequestUsername=dic['username']

    with connection.cursor() as cursor:
        cursor.execute("""SELECT medico.username, cita.fecha, horario.hora_inicio, horario.hora_fin, consultorio.nombre
                          FROM medico
                          JOIN agenda ON (medico.id_agenda = agenda.id_agenda)
                          JOIN consultorio ON(agenda.id_consultorio = consultorio.id_consultorio)
                          JOIN cita ON (agenda.id_agenda = cita.id_agenda)
                          JOIN horario ON (cita.id_horario = horario.id_horario)
                          JOIN paciente ON (cita.id_usuario = paciente.id_usuario)
                          WHERE paciente.email = %s""", [dataRequestUsername])
                    
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