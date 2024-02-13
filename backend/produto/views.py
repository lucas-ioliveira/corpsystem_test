from rest_framework import generics
from produto.models import GrupoProduto, Produto
from produto.serializers import GrupoProdutoSerializer, ProdutoSerializer

class GrupoProdutoList(generics.ListCreateAPIView):
    queryset = GrupoProduto.objects.filter(status=True)
    serializer_class = GrupoProdutoSerializer

class GrupoProdutoDetalhes(generics.RetrieveUpdateDestroyAPIView):
    queryset = GrupoProduto.objects.filter(status=True)
    serializer_class = GrupoProdutoSerializer


class ProdutoList(generics.ListCreateAPIView):
    queryset = Produto.objects.filter(status=True)
    serializer_class = ProdutoSerializer

class ProdutoDetalhes(generics.RetrieveUpdateDestroyAPIView):
    queryset = Produto.objects.filter(status=True)
    serializer_class = ProdutoSerializer
