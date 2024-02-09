from django.contrib import admin
from clientes.models import CadastroClientes

@admin.register(CadastroClientes)
class CadastroClientesAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'dt_aniversario', 'telefone', 'status', 'dt_criacao', 'dt_atualizacao')
    list_filter = ('status', 'usuario',)
    list_display_links = ('usuario', 'telefone',)
    search_fields = ('usuario', 'usuario__username',)
    fieldsets = (
        ('Informações Pessoais', {
            'fields': (
                'usuario', 'dt_aniversario', 'telefone', 'status',)
                }),
        ('Informações de Endereço', {
            'fields': ('cep', 'logradouro', 'bairro', 'cidade', 'complemento', 'uf',)
        })
    )
