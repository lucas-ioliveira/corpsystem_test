from rest_framework import serializers
from clientes.models import CadastroClientes

class CadastroClientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CadastroClientes
        fields = ('id', 'usuario', 'user_firstname', 'user_lastname', 'dt_aniversario', 'telefone', 'status', 'cep', 'logradouro',
                  'bairro', 'cidade', 'complemento', 'uf', 'dt_criacao', 'dt_atualizacao')
    
    user_firstname = serializers.SerializerMethodField()
    user_lastname = serializers.SerializerMethodField()

    def get_user_firstname(self, obj):
        return obj.usuario.first_name
    
    def get_user_lastname(self, obj):
        return obj.usuario.last_name
    
    