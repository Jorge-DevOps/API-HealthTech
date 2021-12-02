from django.http import response
from django.shortcuts import render
from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer
from django.http import HttpResponse

# Register-- API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })
#---------Part Login in the api------------
from django.contrib.auth import login
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
import json
from django import http
from Apps.share.paciente.models import Paciente
from Apps.share.medico.models import Medico
from Apps.share.administrador.models import Administrador
class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)
    def traerPerfil(consulta):
            for p in consulta:
                print("valor de P: ",p.id_perfil.id_perfil)
                return int(p.id_perfil.id_perfil)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
       
        #Validación
        dataRequestPerfil=request.data.get('perfil')
        dataRequestUsername=request.data.get('username')

        if dataRequestPerfil=="1":
            queryAdministrador=f"SELECT id_usuario, id_perfil FROM administrador WHERE email = '{dataRequestUsername}'"
            consulta=Administrador.objects.raw(queryAdministrador)
            
        elif dataRequestPerfil=="2":
            
            queryPaciente=f"SELECT id_usuario, id_perfil FROM paciente WHERE email = '{dataRequestUsername}'"
            consulta=Paciente.objects.raw(queryPaciente)

        elif dataRequestPerfil=="3":
            queryMedico=f"SELECT id_usuario, id_perfil FROM medico WHERE email = '{dataRequestUsername}'"
            consulta=Medico.objects.raw(queryMedico)
        #queryPaciente2= Paciente.objects.raw(f'SELECT id_perfil FROM paciente WHERE email = '{dataRequestUsername}'')

        if LoginAPI.traerPerfil(consulta)==int(dataRequestPerfil):
            login(request, user)
            response=super(LoginAPI, self).post(request, format=None)
            print("si es un paciente")
        else:
            response=HttpResponse("Credenciales invalidas")
        
         #Parte del codigo que se usa para el Login
        return response