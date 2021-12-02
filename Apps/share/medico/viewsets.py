from rest_framework import  viewsets
from Apps.LoginUsuarios.views import LoginAPI
from . import models
from . import  serializers
from Apps.LoginUsuarios import views as viewsLogin

class MedicoViewset(viewsets.ModelViewSet):
    queryset = models.Medico.objects.all()
    #Estamos indicando el serializador para la conversion a json, para nuestro conjunto de vistas
    serializer_class = serializers.MedicoSerializer
"""Con esta clase estamos creando por defecto los metedos de abajo para 
los metodos GET = list(), Post= create(), PUT= update(), DELETE = destroy()"""
# list(), retrive(), create(), update(), destroy()