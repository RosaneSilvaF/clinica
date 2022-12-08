from django.urls import path,include
from usuario.views import teste


urlpatterns = [
    path('cu/', teste),
]
