from django.db import models
from model_utils.managers import InheritanceManager
from endereco.models import Endereco

# Create your models here.
class Usuario(models.Model):
    nome = models.CharField(max_length=50,  blank=False, null=False)
    email = models.EmailField(blank=False, null=False,unique=True)
    telefone =  models.CharField(max_length=11)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)
    objects = InheritanceManager()

class Funcionario(Usuario):
    password = models.CharField(max_length=50,  blank=False, null=False)
    salario = models.DecimalField(max_digits=7,decimal_places=2, blank=False, null=False)
    data_contrato = models.DateField( blank=False, null=False)
    objects = InheritanceManager()

class Medico(Funcionario):
    especialidade = models.CharField(max_length=100,  blank=False, null=False)
    crm = models.CharField(max_length=20,  blank=False, null=False)

class Paciente(Usuario):
    peso = models.DecimalField(max_digits=4,decimal_places=1,blank=False, null=False)
    altura = models.IntegerField(blank=False, null=False)
    tipo_sanguineo = models.CharField(max_length=3, blank=False, null=False)