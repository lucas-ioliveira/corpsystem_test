from django.urls import path
from clientes.views import CadastroClientesLista, CadastroClientesDetalhes

urlpatterns = [
    path('', CadastroClientesLista.as_view(), name='cadastro_clientes_lista'),
    path('detalhes/<int:pk>/', CadastroClientesDetalhes.as_view(), name='cadastro_clientes_detalhes')
]