from rest_framework import serializers
from vendas.models import Vendas

class RelatorioVendasSerializer(serializers.ModelSerializer):

    cliente_nome = serializers.CharField(
        source='cliente'
    )

    vendedor_nome = serializers.CharField(
        source='vendedor'
    )

    item_vendido_nome = serializers.CharField(
        source='item_vendido'
    )

    tipo_pagamento_nome = serializers.CharField(
        source='get_tipo_pagamento_display'
    )

    status_venda_nome = serializers.CharField(
        source='get_status_venda_display'
    )

    data_venda = serializers.CharField(
        source='dt_criacao'
    )

    class Meta:
        model = Vendas
        fields = ['cliente_nome', 'vendedor_nome', 'item_vendido_nome', 'tipo_pagamento_nome', 
                  'status_venda_nome', 'data_venda']
    



   
