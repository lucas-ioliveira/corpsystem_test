from django.urls import path
from relatorios.views import ExportarRelatorioView

urlpatterns = [
    path('exportar/', ExportarRelatorioView.as_view(), name='exportar_relatorio'),
]