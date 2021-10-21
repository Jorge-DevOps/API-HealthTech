from django.urls import path, re_path

from .views import  usuarioListView, usuarioDetailView

urlpatterns = [
    path('usuario/', usuarioListView.as_view(), name="usuario_list"),
    path('usuario/<int:pk>/', usuarioDetailView.as_view(), name='usuario'),
]