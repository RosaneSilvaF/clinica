from django.shortcuts import render
from rest_framework.views import APIView, Response, status
from usuario.models import *
from agenda.models import Agenda
from api.serializers import *
from datetime import datetime as date_time
import datetime

class UserAPI(APIView):
    def get(self,request):
        PACIENTE = "1"
        FUNCIONARIO = "2"
        usuario_tipo = request.query_params['tipo']
        try: 
            usuario_id = request.query_params['usuario_id'] or None
        except:
            usuario_id = None
        
        try:
            if usuario_tipo == PACIENTE:
                if usuario_id:
                    pacientes = Paciente.objects.all().get(id=usuario_id)
                    pacientes_response = PacienteSerializer(pacientes, many = False).data
                else:
                    pacientes = Paciente.objects.all()
                    pacientes_response = PacienteSerializer(pacientes, many = True).data
                return Response(pacientes_response)
            elif usuario_tipo == FUNCIONARIO:
                if usuario_id:
                    funcionarios = Funcionario.objects.all().get(id=usuario_id)
                    funcionario_response = FuncionarioSerializer(funcionarios, many = False).data
                else:
                    funcionarios = Funcionario.objects.all()
                    funcionario_response = FuncionarioSerializer(funcionarios, many = True).data
                return Response(funcionario_response)
            else:
                if usuario_id:
                    medicos = Medico.objects.all().get(id=usuario_id)
                    medico_response = MedicoSerializer(medicos, many = False).data
                else:
                    medicos = Medico.objects.all()
                    medico_response = MedicoSerializer(medicos, many = True).data
                return Response(medico_response)
        except Exception as e:
            return Response("Erro ao obter usuário, verifique se o tipo e o id do usuário estão de acordo", status=status.HTTP_400_BAD_REQUEST)

    def post(self,request):
        PACIENTE = 1
        FUNCIONARIO = 2
        usuario_tipo = request.data.get('tipo')
        data_contrato = request.data.get('data_contrato') or None
        if data_contrato:
            date = datetime.date(int(data_contrato.split('-')[0]),int(data_contrato.split('-')[1]),int(data_contrato.split('-')[2]))


        email = request.data.get('email')
        try:
            if Usuario.objects.all().get(email=email):
                return Response(u'Email ja cadastrado', status=status.HTTP_400_BAD_REQUEST)
        except Usuario.DoesNotExist:
            pass
        
        try:
            endereco = Endereco()
            endereco.bairro = request.data.get('bairro')
            endereco.cep = request.data.get('cep')
            endereco.cidade = request.data.get('cidade')
            endereco.estado = request.data.get('estado')
            endereco.save()
        except Exception:
            return Response(u'Deu ruim pra criar Endereço, passa a porra dos dados certos', status=status.HTTP_400_BAD_REQUEST)

        if usuario_tipo == PACIENTE:
            try:
                paciente = Paciente()
                paciente.nome = request.data.get('nome')
                paciente.email = request.data.get('email')
                paciente.telefone = request.data.get('telefone')
                paciente.endereco = endereco
                paciente.peso = request.data.get('peso')
                paciente.altura = request.data.get('altura')
                paciente.tipo_sanguineo = request.data.get('tipo_sanguineo')
                paciente.save()
            except Exception as e :
                return Response(u'Deu ruim pra criar Paciente, passa a porra dos dados certos', status=status.HTTP_400_BAD_REQUEST)
            return Response('OK')

        elif usuario_tipo == FUNCIONARIO:
            try:
                funcionario = Funcionario()
                funcionario.nome = request.data.get('nome')
                funcionario.email = request.data.get('email')
                funcionario.telefone = request.data.get('telefone')
                funcionario.endereco = endereco
                funcionario.password = request.data.get('password')
                funcionario.salario = request.data.get('salario')
                funcionario.data_contrato = date
                funcionario.save()
            except Exception as e :
                return Response(u'Deu ruim pra criar Funcionario, passa a porra dos dados certos', status=status.HTTP_400_BAD_REQUEST)
            return Response('OK')
        else:
            try:
                medico = Medico()
                medico.nome = request.data.get('nome')
                medico.email = request.data.get('email')
                medico.telefone = request.data.get('telefone')
                medico.endereco = endereco
                medico.password = request.data.get('password')
                medico.salario = request.data.get('salario')
                medico.data_contrato = date
                medico.especialidade = request.data.get('especialidade')
                medico.crm = request.data.get('crm')
                medico.save()
            except Exception as e :
                return Response(u'Deu ruim pra criar Medico, passa a porra dos dados certos')
            return Response('OK')

class EnderecoAPI(APIView):
    def get(self,request):
        try:
            usuario = request.query_params['usuario']
        except:
            usuario = None
        
        if usuario:
            usuario_endereco = Usuario.objects.all().get(id=int(usuario)).endereco
            print(usuario_endereco)
            endereco_response = EnderecoSerializer(usuario_endereco, many = False).data
            return Response(endereco_response)
            
        enderecos = Endereco.objects.all()
        enderecos_response = EnderecoSerializer(enderecos, many = True).data
        return Response(enderecos_response)


class LoginAPI(APIView):
    def post(self,request):
        password = request.data.get('password') or None
        email = request.data.get('email') or None
        usuario = ''
        if not password or not email:
            return Response('Sem email ou senha', status=status.HTTP_400_BAD_REQUEST)

        try:
            usuario = Funcionario.objects.all().get(email=email,password=password)
        except Usuario.DoesNotExist:
            return Response('Não encontrado', status=status.HTTP_404_NOT_FOUND)
        finally:
            usuario_response = UsuarioSerializer(usuario,many=False).data
        return Response(usuario_response)


class AgendaAPI(APIView):
    def post(self,request):
        data = request.data.get('data') or None
        paciente_id = request.data.get('paciente_id') or None
        medico_id = request.data.get('medico_id') or None

        if not data or not paciente_id or not medico_id:
            return Response('Faltam dados na requisição', status=status.HTTP_400_BAD_REQUEST)
        
       
        agendamento = Agenda()
        agendamento.data = date_time.strptime(data, '%d/%m/%y %H:%M:%S')
        try:
            agendamento.medico = Medico.objects.all().get(id=medico_id)
        except Medico.DoesNotExist:
            return Response('Medico não existe', status=status.HTTP_404_NOT_FOUND)

        try:
            agendamento.paciente = Paciente.objects.all().get(id=paciente_id)
        except Paciente.DoesNotExist:
            return Response('Paciente não existe', status=status.HTTP_404_NOT_FOUND)

        agendamento.save()
        return Response('OK', status=status.HTTP_200_OK)

    def get(self,request):
        try:
            medico_id = request.query_params['medico_id'] 
        except : 
            medico_id = None

        if not medico_id:
            agendamentos = Agenda.objects.all().order_by('id')
            agendamentos_serializer = AgendaSerializer(agendamentos,many=True).data

            return Response(agendamentos_serializer,status=status.HTTP_200_OK)

        agendamentos = Agenda.objects.all().filter(medico_id=int(medico_id))
        if not agendamentos:
            return Response('Não foram encontrados agendamentos para esse médico', status=status.HTTP_404_NOT_FOUND)

        agendamentos_serializer = AgendaSerializer(agendamentos,many=True).data
        return Response(agendamentos_serializer,status=status.HTTP_200_OK)
        


            