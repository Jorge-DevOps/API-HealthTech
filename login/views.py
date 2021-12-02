from.serializers import SerializerLogin
from.models import LoginModel, FormLogin
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import serializers, viewsets
from django.http import  JsonResponse
from django.views import View
from django.views.decorators.http import require_POST
# Create your views here.
from django.contrib.auth import authenticate, login

@require_POST
def my_view(request):
    print('POST', request.POST)
    username = request.POST.get('username')
    print('usuario', username)
    password = request.POST.get('password')
    print('contraseña', password)
    user = authenticate(request, username=username, password=password)
    print('user', user)
    if user is not None:
        login(request, user)
        return HttpResponse('bien papu')
    else:
        return HttpResponse('cagaste')