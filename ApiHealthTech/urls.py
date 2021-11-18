from django.contrib import admin
from django.urls import path, re_path, include
from django.urls import path, include
from .router import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('',include('login.urls')),
]
