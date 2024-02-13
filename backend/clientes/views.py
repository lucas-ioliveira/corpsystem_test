from rest_framework import generics
from clientes.models import CadastroClientes
from clientes.serializers import CadastroClientesSerializer


class CadastroClientesLista(generics.ListCreateAPIView):
    queryset = CadastroClientes.objects.filter(status=True)
    serializer_class = CadastroClientesSerializer

class CadastroClientesDetalhes(generics.RetrieveUpdateDestroyAPIView):
    queryset = CadastroClientes.objects.filter(status=True)
    serializer_class = CadastroClientesSerializer


            
        
                
        
        