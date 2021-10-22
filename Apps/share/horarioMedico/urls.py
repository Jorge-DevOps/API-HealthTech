from django.urls import path, re_path

from . import views

app_name="horarioMedico_app"

urlpatterns = [
    path('postHorarioMedico', views.post, name="postHorarioMedico"),
    path('postHorarioMedico2', views.Post_ApiView, name="postHorarioMedico2"),
]