from django.db import models

# Create your models here.
class Endereco(models.Model):
    cep = models.CharField(max_length=8,null=False,blank=False)
    bairro = models.CharField(max_length=50,null=False,blank=False)
    cidade = models.CharField(max_length=50,null=False,blank=False)
    estado = models.CharField(max_length=50,null=False,blank=False)
    