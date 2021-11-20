from django.contrib import admin
from django.urls import path, re_path, include
from django.urls import path, include
from .router import router
from Apps.JoinUsuarios import views as viewsExcel

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^', include('Apps.usuario.urls')),
    path('api/', include(router.urls)),
    path('api/Excel', viewsExcel.export_excel),
    path('',include('Apps.LoginUsuarios.urls'))
]
