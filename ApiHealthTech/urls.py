from django.contrib import admin
from django.urls import path, re_path, include
from django.urls import path, include
from login import views
from django.contrib.auth.views import LoginView
from .router import router
from Apps.JoinUsuarios import views as viewsExcel

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('login/', views.my_view,  name="login"),
    path('api/Excel', viewsExcel.export_excel),
    path('',include('Apps.LoginUsuarios.urls'))
]
