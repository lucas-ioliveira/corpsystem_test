from django.contrib import admin
from vendas.models import Vendas

@admin.register(Vendas)
class VendasAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'vendedor','tipo_pagamento', 'item_vendido', 'status_venda', 'venda_ativa','dt_criacao')
    list_filter = ('id', 'cliente', 'vendedor', 'dt_criacao')
    list_display_links = ('id', 'dt_criacao')
    search_fields = list_filter