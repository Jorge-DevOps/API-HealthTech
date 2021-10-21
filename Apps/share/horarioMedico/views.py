from django.shortcuts import render
from django.http import HttpResponse
from . import forms
from django.views.decorators.http import require_POST

@require_POST
def post(request):
    form = forms.HorarioMedico(request.POST) 
    if form.is_valid():
        return HttpResponse('/thanks/')
    return HttpResponse(request, 'name.html')
