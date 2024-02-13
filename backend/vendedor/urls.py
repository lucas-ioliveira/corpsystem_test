from django.urls import path
from vendedor.views import VendedorLista, VendedorDetalhes

urlpatterns = [
    path('', VendedorLista.as_view(), name='cadastro_clientes_lista'),
    path('detalhes/<int:pk>/', VendedorDetalhes.as_view(), name='cadastro_clientes_detalhes')
]