
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('endereco/', include('endereco.urls')),
    path('usuario/', include('usuario.urls')),
    path('api/', include('api.urls')),
]
