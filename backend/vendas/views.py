from rest_framework import generics
from vendas.models import Vendas
from vendas.serializers import VendasSerializer

class VendasLista(generics.ListCreateAPIView):
    queryset = Vendas.objects.filter(venda_ativa=True)
    serializer_class = VendasSerializer

class VendasDetalhes(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendas.objects.filter(venda_ativa=True)
    serializer_class = VendasSerializer