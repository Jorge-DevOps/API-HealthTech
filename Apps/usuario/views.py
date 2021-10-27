from django.shortcuts import render
from django.views import View
from .models import  usuario
from django.http import  JsonResponse
from django.forms.models import  model_to_dict

class usuarioListView(View):
    def get(self, request):
        """Consultar usuarios"""
        listUsers = usuario.objects.all()
        return JsonResponse(list(listUsers.values()), safe=False)
        # get....
    def post(self, request):
        """Crear usuarios"""
        # post ...
    def put(self, request):
        """Actualizar usuarios"""
        # put
    def delete(self, request):
        """Eliminar usuarios"""
        # delete...

class usuarioDetailView(View):
    """Le pasamos la pk como parametro para identificar al usuario"""
    def get(self, request, pk):
        """Consultar usuario"""
        user = usuario.objects.get(pk=pk)
        return JsonResponse(model_to_dict(user))
        # get....
    def post(self, request):
        """Crear usuario"""
        # post ...
    def put(self, request):
        """Actualizar usuario"""
        # put
    def delete(self, request):
        """Eliminar usuario"""
        # delete...
