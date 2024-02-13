from django.urls import path
from produto.views import GrupoProdutoList, GrupoProdutoDetalhes, ProdutoList, ProdutoDetalhes

urlpatterns = [
    path('', ProdutoList.as_view(), name='produtos_lista'),
    path('detalhes/<int:pk>/', ProdutoDetalhes.as_view(), name='produtos_detalhes'),
    path('grupos', GrupoProdutoList.as_view(), name='produtos_lista'),
    path('grupos/detalhes/<int:pk>/', GrupoProdutoDetalhes.as_view(), name='produtos_detalhes')
]