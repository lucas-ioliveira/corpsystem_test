from rest_framework import serializers
from vendas.models import Vendas

class VendasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendas
        fields = '__all__'

    cliente_nome = serializers.CharField(
        source='cliente',
        read_only=True
    )

    vendedor_nome = serializers.CharField(
        source='vendedor',
        read_only=True
    )

    item_vendido_nome = serializers.CharField(
        source='item_vendido',
        read_only=True
    )

    tipo_pagamento_nome = serializers.CharField(
        source='get_tipo_pagamento_display',
        read_only=True
    )

    status_venda_nome = serializers.CharField(
        source='get_status_venda_display',
        read_only=True
    )
    



   
