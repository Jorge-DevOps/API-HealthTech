from django.shortcuts import render
from django.db import connection
from xlwt.Formatting import Font
from django.http import HttpResponse
import xlwt 
# Create your views here.

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
