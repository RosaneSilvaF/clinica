from django.shortcuts import render
from django.http import HttpResponse
from endereco.models import Endereco

# Create your views here.
def teste(request):
    endereco = Endereco()
    endereco.cep = '12345678'
    endereco.bairro = 'Teste'
    endereco.cidade = 'Teste'
    endereco.estado = 'Teste'
    endereco.save()
    return HttpResponse(list(Endereco.objects.all()))