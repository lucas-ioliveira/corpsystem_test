from django.contrib import admin
from vendedor.models import Vendedor

@admin.register(Vendedor)
class VendedorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'email', 'dt_aniversario', 'telefone', 'status', 'dt_criacao', 'dt_atualizacao')
    list_filter = ('status', 'nome',)
    list_display_links = ('nome', 'telefone',)
    search_fields = ('nome', 'sobrenome',)
    fieldsets = (
        ('Informações Pessoais', {
            'fields': (
                'nome', 'sobrenome', 'email', 'dt_aniversario', 'telefone', 'status',)
                }),
        ('Informações de Endereço', {
            'fields': ('cep', 'logradouro', 'bairro', 'cidade', 'complemento', 'uf',)
        })
    )
