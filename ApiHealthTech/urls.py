from django.contrib import admin
from django.urls import path, re_path, include
from django.urls import path, include
from login import views
from django.contrib.auth.views import LoginView
from .router import router
from Apps.JoinUsuarios import views as viewsExcel
from Apps.share.cita import views as viewsInformeCitas
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('login/', views.my_view,  name="login"),
    path('api/Excel', viewsExcel.export_excel),
    path('api/informeCita',viewsInformeCitas.export_informeCitas),
    path('',include('Apps.LoginUsuarios.urls'))
]
