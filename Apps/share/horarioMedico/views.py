from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from . import forms
from . import models
from . import serializers
from django.views.decorators.http import require_POST
from rest_framework.views import APIView
from rest_framework import status

@require_POST
def post(request):
    models.horarioMedico = forms.HorarioMedico(request.POST) 
    form = forms.HorarioMedico(request.POST) 
    if form.is_valid():
        return HttpResponseNotFound('Ocurrio un Error')
    return HttpResponse('Creado Exitosamente')

 

class Post_ApiView(APIView):

    def post(self, request, format=None):
        serializer = serializers.PostSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(serializer.data, status=status.HTTP_201_CREATED)
        return HttpResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

