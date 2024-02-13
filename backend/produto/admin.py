from django.contrib import admin
from produto.models import GrupoProduto, Produto

@admin.register(GrupoProduto)
class GrupoProdutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'descricao', 'status', 'dt_criacao', 'dt_atualizacao')
    list_filter = ('id', 'nome', 'status',)
    list_display_links = ('nome', 'dt_criacao',)
    search_fields = ('nome', 'dt_criacao',)

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'status', 'preco', 'estoque', 'grupo', 'dt_criacao', 'dt_atualizacao')
    list_filter = ('id', 'nome', 'status',)
    list_display_links = ('nome', 'dt_criacao',)
    search_fields = ('nome', 'dt_criacao',)
