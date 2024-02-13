from rest_framework import generics
from vendedor.models import Vendedor
from vendedor.serializers import VendedorSerializer

class VendedorLista(generics.ListCreateAPIView):
    queryset = Vendedor.objects.filter(status=True)
    serializer_class = VendedorSerializer

class VendedorDetalhes(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendedor.objects.filter(status=True)
    serializer_class = VendedorSerializer
