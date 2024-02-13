from django.http import HttpResponse, FileResponse
from rest_framework.response import Response
from rest_framework.views import APIView
import os
import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime
from vendas.models import Vendas
from relatorios.serializers import RelatorioVendasSerializer

class ExportarRelatorioView(APIView):
    def post(self, request, *args, **kwargs):
        pdf_filename = None
        excel_filename = None
        try:
            data = request.data.get('data')
            vendedor = request.data.get('vendedor')
            cliente = request.data.get('cliente')
            opcao = request.data.get('opcao')

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
                pdf_filename = 'relatorio_vendas.pdf'
                self.exportar_para_pdf(data, pdf_filename)

                # Construir a resposta PDF
                response = FileResponse(open(pdf_filename, 'rb'), content_type='application/pdf')
                response['Content-Disposition'] = 'attachment; filename="relatorio_vendas.pdf"'
            
            elif opcao == 'excel':
                excel_filename = 'relatorio_vendas.xlsx'
                self.exportar_para_excel(data, excel_filename)

                # Construir a resposta Excel
                response = FileResponse(open(excel_filename, 'rb'), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
                response['Content-Disposition'] = 'attachment; filename="relatorio_vendas.xlsx"'
            else:
                return Response({'detail': 'Opção inválida. Escolha entre "pdf" ou "excel".'})
            
            if excel_filename:
                os.remove(excel_filename)

            if pdf_filename:
                os.remove(pdf_filename)

            return response

        except Exception as e:
            return Response({'detail': str(e)})

    def exportar_para_excel(self, data, filename):
        df = pd.DataFrame(data)
        df.to_excel(filename, index=False)

    def exportar_para_pdf(self, data, filename):
        doc = SimpleDocTemplate(filename, pagesize=letter)
        styles = getSampleStyleSheet()
        header_style = styles['Heading1']
        conteudo = [Paragraph("Relatório de Vendas", header_style)]
        table_data = [["Data da Venda", "Nome do Vendedor", "Nome do Cliente"]]
        for item in data:
            table_data.append([item['data_venda'], item['vendedor_nome'], item['cliente_nome']])
        table = Table(table_data)
        doc.build(conteudo + [table])
