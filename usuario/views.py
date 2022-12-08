from django.shortcuts import render
from usuario.models import * 
from endereco.models import *
from datetime import *

def teste(request):
    endereco = Endereco()
    endereco.cep = '1231231'
    endereco.logadouro = 'cu'
    endereco.bairro = 'cu'
    endereco.cidade = 'cu'
    endereco.estado = 'CU'
    endereco.save()
     
    pessoa = Medico()
    pessoa.especialidade = 'Cu'
    pessoa.crm = '123'
    pessoa.nome = 'Doutor cu'
    pessoa.email = 'cu@cu.cu'
    pessoa.telefone = '123'
    pessoa.password = 'cu123'
    pessoa.salario = 6785.00
    pessoa.data_contrato = date(2022, 12, 31)
    pessoa.endereco = Endereco.objects.all().last()

    pessoa.save()


    print(Usuario.objects.all())
