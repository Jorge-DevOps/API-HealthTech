from io import BytesIO
from reportlab.pdfgen import canvas
from django.http import HttpResponse

def generarCertificadoPaciente(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="mypdf.pdf"'
    #response['Content-Disposition'] = 'attachment; filename=' + \
    #    str('certificadoAfiliado')+'.pdf'

    buffer = BytesIO()
    p = canvas.Canvas(buffer)

    # Start writing the PDF here
    p.drawString(148, 700, 'CERTIFICADO DE AFILIACIÓN AL PBS DE EPS SURA')
    p.drawString(30, 660, 'EPS Y MEDICINA PREPAGADA SURAMERICANA S.A en desarrollo de su programa especial para')
    p.drawString(30, 640, 'la garantía del Plan de Beneficios en Salud denominado EPS SURA')
    p.drawString(268, 595, 'CERTIFICA')
    p.drawString(150, 500, 'CERTIFICADO DE AFILIACIÓN AL PBS DE EPS SURA')
    p.drawString(150, 400, 'CERTIFICADO DE AFILIACIÓN AL PBS DE EPS SURA')
    p.drawString(100, 300, 'Hello world.')
    # End writing

    p.showPage()
    p.save()

    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)

    return response