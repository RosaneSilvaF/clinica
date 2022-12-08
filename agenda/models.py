from django.db import models
from usuario.models import Paciente
from usuario.models import Medico

# Create your models here.
class Agenda(models.Model):
    data = models.DateTimeField(blank = False, null = False)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)