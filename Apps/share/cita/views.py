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
from django.views import View

from rest_framework import permissions
from django.views.generic.edit import UpdateView
#from knox.views import LoginView as KnoxLoginView
# Create your views here.

def traerMedicos(request):
    queryMedicos="SELECT  id_usuario, username, id_agenda FROM medico "
    consulta=Medico.objects.raw(queryMedicos)
    result = []
    for p in consulta:
        result.append(p.username)
    response = HttpResponse(json.dumps(result, indent=4),content_type='application/json')
    return response
  
from knox.views import LoginView as KnoxLoginView
class HorariosDisponibles(UpdateView):
  
  permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )
  permission_classes = (permissions.AllowAny,)
  def post(self, request, format=None):
    
    self.http_method_names.append("post")
    form = self.form_class(request.POST)
    if form.is_valid():
      dataRequestUsername=request.data.get('username')
      dataRequestFecha=request.data.get('fecha')
      print(dataRequestFecha)
      queryAgenda=f"SELECT agenda.id_agenda FROM agenda, medico, usuario WHERE usuario.nombre_usuario = '{dataRequestUsername}' AND usuario.id_usuario = medico.id_usuario AND medico.id_agenda = agenda.id_agenda"
      consultaAgenda=Agenda.objects.raw(queryAgenda)
      
      for p in consultaAgenda:
            print("id_agenda: ",p.id_agenda)
      
      queryHorariosDisponibles=f"SELECT * FROM horario WHERE horario.id_horario NOT IN ( SELECT cita.id_horario FROM cita WHERE cita.fecha ={dataRequestFecha} AND cita.id_agenda ={p.id_agenda}"
      response = HttpResponse(p,content_type='application/json')
      #json.dumps(result, indent=4)    
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
