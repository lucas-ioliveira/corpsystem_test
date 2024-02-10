from rest_framework import serializers
from produto.models import GrupoProduto, Produto

class GrupoProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrupoProduto
        fields = '__all__'

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'