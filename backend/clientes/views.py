from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from clientes.models import CadastroClientes
from clientes.serializers import CadastroClientesSerializer
from rest_framework import generics


class CadastroClientesLista(generics.ListCreateAPIView):
    queryset = CadastroClientes.objects.filter(status=True)
    serializer_class = CadastroClientesSerializer

class CadastroClientesDetalhes(generics.RetrieveUpdateDestroyAPIView):
    queryset = CadastroClientes.objects.filter(status=True)
    serializer_class = CadastroClientesSerializer


            
        
                
        
        