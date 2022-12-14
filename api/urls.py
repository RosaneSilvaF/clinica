from django.urls import path, include
from api.views import *

urlpatterns = [
    path('usuario/', UserAPI.as_view()),
    path('endereco/', EnderecoAPI.as_view()),
    path('login/', LoginAPI.as_view()),
    path('agenda/', AgendaAPI.as_view()),
    path('especialidades/', get_especialidades),
]
