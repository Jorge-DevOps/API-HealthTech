from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from rest_framework import  viewsets
from . import  serializers
from . import models

# Create your views here.

def index(request):
    queryset = models.horarioMedico.objects.all()
    serializer_class = serializers.HorarioMedicoSerializer
    
    if request.method == 'POST':
        form = models.LoginMedico(request.POST) 
        userMedico = form.cleaned_data['user']
        print('xd', userMedico)
        if(userMedico == 'Medico'):
            return HttpResponse('Es medico')
        else:
            return HttpResponse('No es medico')
    else:
        return HttpResponse('BIEN')


def custom(request):
    return render(request, 'custom.html')


def home(request):
    return render(request, 'home.html')

