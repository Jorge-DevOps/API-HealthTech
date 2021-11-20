from django.db import connection
from xlwt.Formatting import Font
from.serializers import Jointableserializer
from.models import JoinTablesmodel
from rest_framework import serializers, viewsets
from django.http import HttpResponse
import xlwt 

# Create your views here.
class Jointableapi(viewsets.ModelViewSet):
    queryset=JoinTablesmodel.objects.raw('SELECT id_usuario, tipo_documento, numero_documento, nombre_usuario, contrasena, correo, telefono, sexo, fecha_nacimiento, grupo_sanguineo, estrato, estado_civil, id_perfil FROM  administrador UNION SELECT  id_usuario, tipo_documento, numero_documento, nombre_usuario, contrasena, correo, telefono, sexo, fecha_nacimiento, grupo_sanguineo, estrato, estado_civil, id_perfil FROM medico UNION SELECT  id_usuario, tipo_documento, numero_documento, nombre_usuario, contrasena, correo, telefono, sexo, fecha_nacimiento, grupo_sanguineo, estrato, estado_civil, id_perfil FROM paciente')
    serializer_class = Jointableserializer



def export_excel(request):
      response = HttpResponse(content_type='application/ms-excel')
      #nesecitamos enviarle el contenido
      response['Content-Disposition'] = 'attachment; filename=Expenses' + \
        str('informeDeUsuarios')+'.xls'
      wb = xlwt.Workbook(encoding='utf-8')
      ws=wb.add_sheet('Usuarios')
      row_num = 0
      font_style=xlwt.XFStyle()
      font_style.font.bold =True

      columns = ['id_usuario','tipo_documento','numero_documento','nombre_usuario','contrasena','correo','telefono','sexo','fecha_nacimiento','grupo_sanguineo','estrato','estado_civil','id_perfil']

      for col_num in range(len(columns)):
        ws.write(row_num,col_num,columns[col_num], font_style)
      font_style=xlwt.XFStyle()

      with connection.cursor() as cursor:
        cursor.execute("SELECT id_usuario, tipo_documento, numero_documento, nombre_usuario, contrasena, correo, telefono, sexo, fecha_nacimiento, grupo_sanguineo, estrato, estado_civil, id_perfil FROM  administrador UNION SELECT  id_usuario, tipo_documento, numero_documento, nombre_usuario, contrasena, correo, telefono, sexo, fecha_nacimiento, grupo_sanguineo, estrato, estado_civil, id_perfil FROM medico UNION SELECT  id_usuario, tipo_documento, numero_documento, nombre_usuario, contrasena, correo, telefono, sexo, fecha_nacimiento, grupo_sanguineo, estrato, estado_civil, id_perfil FROM paciente")
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
