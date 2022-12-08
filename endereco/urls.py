from django.contrib import admin
from django.urls import path
from endereco.views import teste

urlpatterns = [
    path('teste/', teste),
]
