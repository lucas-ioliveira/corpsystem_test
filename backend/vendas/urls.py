from django.urls import path
from vendas.views import VendasLista, VendasDetalhes

urlpatterns = [
    path('', VendasLista.as_view(), name='vendas_lista'),
    path('detalhes/<int:pk>/', VendasDetalhes.as_view(), name='vendas_detalhes')
]