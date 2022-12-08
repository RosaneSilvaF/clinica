
from usuario.models import *
from endereco.models import *
from agenda.models import Agenda
from rest_framework import serializers

class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = ('id','nome', 'email', 'telefone','endereco','password','salario','data_contrato','especialidade','crm')

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = ('id','nome', 'email', 'telefone','endereco','peso','altura','tipo_sanguineo')

class FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionario
        fields = ('id','nome', 'email', 'telefone','endereco','password','salario','data_contrato')

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id','nome', 'email', 'telefone','endereco')

class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = ('id','cep','bairro','cidade','estado')

class AgendaSerializer(serializers.ModelSerializer):
    class Meta :
        model = Agenda
        fields = ('id','data','paciente','medico')