from rest_framework import serializers
from clientes.models import CadastroClientes

class CadastroClientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CadastroClientes
        fields = '__all__'
    
