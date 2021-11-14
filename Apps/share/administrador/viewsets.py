from rest_framework import  viewsets
from . import models
from . import  serializers

class AdministradorViewset(viewsets.ModelViewSet):
    queryset = models.Administrador.objects.all()
    #Estamos indicando el serializador para la conversion a json, para nuestro conjunto de vistas
    serializer_class = serializers.AdministradorSerializer
"""Con esta clase estamos creando por defecto los metedos de abajo para 
los metodos GET = list(), Post= create(), PUT= update(), DELETE = destroy()"""
# list(), retrive(), create(), update(), destroy()