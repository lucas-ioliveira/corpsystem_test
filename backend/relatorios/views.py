from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
import os
import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, Paragraph
from django.http import FileResponse
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime
from vendas.models import Vendas
from relatorios.serializers import RelatorioVendasSerializer

class ExportarRelatorioView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            data = self.request.data.get('data')
            vendedor = self.request.data.get('vendedor')
            cliente = self.request.data.get('cliente')
            opcao = request.query_params.get('opcao')

            vendas = Vendas.objects.all()
            if data:
                vendas = vendas.filter(dt_criacao=datetime.strptime(data, '%Y-%m-%d'))
            if vendedor:
                vendas = vendas.filter(vendedor=vendedor)
            if cliente:
                vendas = vendas.filter(cliente=cliente)
            
            serializer = RelatorioVendasSerializer(vendas, many=True)
            data = serializer.data

            if opcao == 'pdf':
                pdf_filename = 'relatorio_vendas.xlsx'
                self.exportar_para_pdf(data, pdf_filename)

                # Remover o arquivo Excel após retornar a resposta
                response = HttpResponse(content_type='application/pdf')
                response['Content-Disposition'] = 'attachment; filename="exemplo.pdf"'
                os.remove(pdf_filename)
            
            elif opcao == 'excel':
                excel_filename = 'relatorio_vendas.xlsx'
                self.exportar_para_excel(data, excel_filename)

                # Remover o arquivo Excel após retornar a resposta
                response = FileResponse(open(excel_filename, 'rb'), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
                response['Content-Disposition'] = 'attachment; filename="relatorio_vendas.xlsx"'
                os.remove(excel_filename)

            return response
        except Exception as e:
            return Response({'detail': str(e)})

    def exportar_para_excel(self, data, filename):
        df = pd.DataFrame(data)
        df.to_excel(filename, index=False)

    def exportar_para_pdf(self, data, filename):
        # Criar um documento PDF
        doc = SimpleDocTemplate(filename, pagesize=letter)

        # Definir estilos
        styles = getSampleStyleSheet()
        header_style = styles['Heading1']

        # Conteúdo do PDF
        conteudo = [
            Paragraph("Relatório de Vendas", header_style),
        ]

        # Criar a tabela com os dados
        table_data = [["Data da Venda", "Nome do Vendedor", "Nome do Cliente"]]
        for item in data:
            table_data.append([item['data_venda'], item['vendedor_nome'], item['cliente_nome']])
        table = Table(table_data)

        # Adicionar conteúdo e tabela ao documento
        doc.build(conteudo + [table])
       