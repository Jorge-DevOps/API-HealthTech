from io import BytesIO

from django.db.models.fields import EmailField
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from json import loads
from.models import Paciente
from datetime import datetime

def generarCertificadoPaciente(request):

    dic = loads(request.body)

    dataRequestUsername=dic['username']

    response = HttpResponse(content_type='application/pdf')
    #response['Content-Disposition'] = 'inline; filename="mypdf.pdf"'
    response['Content-Disposition'] = 'attachment; filename=' + \
        str('certificadoAfiliado')+'.pdf'

    afiliado = consultarDatosAfiliado(dataRequestUsername)
    nombreAfiliado = afiliado.username
    tipoDocAfiliado = afiliado.tipo_documento
    documentoAfiliado = afiliado.numero_documento
    contrato = afiliado.contrato

    buffer = BytesIO()
    p = canvas.Canvas(buffer)

    # Start writing the PDF here
    p.setFont("Helvetica", 20)
    p.setStrokeColorRGB(0.2,0.5,0.3)
    p.setFillColorRGB(0,0,1)
    p.drawString(30, 760, 'PREPAGADA')
    p.setFont("Times-Bold", 20)
    p.drawString(420, 760, 'HEALTH TECH')

    p.setFont("Helvetica-Bold", 13)
    p.setStrokeColorRGB(0.2,0.5,0.3)
    p.setFillColorRGB(0,0,1)
    p.drawString(105, 700, 'CERTIFICADO DE AFILIACIÓN AL PBS DE EPS HEALTH TECH')
    p.setFont("Helvetica", 10)
    p.setFillColorRGB(0,0,0)
    p.drawString(30, 660, 'EPS Y MEDICINA PREPAGADA HEALTH TECH S.A en desarrollo de su programa especial para')
    p.drawString(30, 645, 'la garantía del Plan de Beneficios en Salud denominado EPS HEALTH TECH')
    p.setFont("Helvetica", 13)
    p.drawString(260, 595, 'CERTIFICA')
    p.setFont("Helvetica", 10)
    p.drawString(30, 560, 'Que ' + nombreAfiliado + ' identificado(a) con ' + tipoDocAfiliado + ' número ' + documentoAfiliado + ' está registrado(a) en el PBS EPS ')
    p.drawString(30, 545, 'HEALTH TECH con la siguiente información:')
    p.drawString(30, 510, 'TIPO Y NÚMERO DE IDENTIFICACIÓN')
    p.drawString(300, 510, tipoDocAfiliado + ' ' + documentoAfiliado)
    p.drawString(30, 495, 'NOMBRES Y APELLIDOS')
    p.drawString(300, 495, nombreAfiliado)
    p.drawString(30, 480, 'TIPO DE AFILIADO')
    p.drawString(300, 480, 'TITULAR')
    p.drawString(30, 465, 'PARENTESCO')
    p.drawString(300, 465, 'TITULAR')
    p.drawString(30, 450, 'ESTADO DE AFILIACIÓN')
    p.drawString(300, 450, 'TIENE DERECHO A COBERTURA INTEGRAL')
    p.drawString(30, 435, 'CAUSA ESTADO DE LA AFILIACIÓN')
    p.drawString(300, 435, 'COBERTURA INTEGRAL')
    p.drawString(30, 420, 'N° CONTRATO')
    p.drawString(300, 420, contrato)

    p.drawString(30, 230, 'DIRECCIÓN DE AFILIACIONES')
    p.setFont("Helvetica-Bold", 9)
    p.drawString(30, 210, 'Fecha de generación: ' + datetime.today().strftime('%Y-%m-%d %H:%M'))
    p.setFont("Helvetica-Bold", 12)
    p.drawString(130, 180, 'ESTE DOCUMENTO NO ES VÁLIDO PARA LA PRESTACIÓN')
    p.drawString(190, 160, 'DEL SERVICIO, NI PARA TRASLADOS')

    p.setFont("Courier", 10)
    p.drawString(40, 100, 'EPS Y MEDICINA PREPAGADA HEALTH TECH S.A.')
    p.drawString(40, 80, 'Bogotá D.C., Colombia. Línea de atención Bogotá 477 7777, Medellin 277 77777')
    p.drawString(40, 60, 'Línea Nacional 018000 177 7777')
    p.drawString(40, 40, 'www.healthtech.com')
    # End writing

    p.showPage()
    p.save()

    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)

    return response

def consultarDatosAfiliado(correo):
    return Paciente.objects.get(email=correo)