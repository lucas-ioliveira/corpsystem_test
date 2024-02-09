from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from clientes.models import CadastroClientes
from clientes.serializers import CadastroClientesSerializer


class CadastroClientesLista(APIView):
    def get(self, request):
        try:
            cadastro_clientes = CadastroClientes.objects.filter(status=True)
            serializer = CadastroClientesSerializer(cadastro_clientes, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except CadastroClientes.DoesNotExist:
             return Response({'detail':'Cliente não encontrado ou inexistente',
                             'status':'HTTP 404 Not Found'}, status=status.HTTP_404_NOT_FOUND)

    
    # def post(self, request):
    #     serializer = CadastroClientesSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CadastroClientesDetalhes(APIView):
    def get(self, request, pk):
        try:
            cliete = CadastroClientes.objects.get(pk=pk)
            serializer = CadastroClientesSerializer(cliete)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except CadastroClientes.DoesNotExist:
            return Response({'detail':'Cliente não encontrado ou inexistente',
                             'status':'HTTP 404 Not Found'}, status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, pk):
        try:
            cliente = CadastroClientes.objects.get(pk=pk)
            cliente.status = False
            cliente.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        except CadastroClientes.DoesNotExist:
            return Response({'detail':'Cliente não encontrado ou inexistente',
                             'status':'HTTP 404 Not Found'}, status=status.HTTP_404_NOT_FOUND)
    
    def patch(self, request, pk):
        try:
            cliente = CadastroClientes.objects.get(pk=pk)
            serializer = CadastroClientesSerializer(cliente, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        except CadastroClientes.DoesNotExist:
            return Response({'detail':'Cliente não encontrado ou inexistente',
                             'status':'HTTP 404 Not Found'}, status=status.HTTP_400_BAD_REQUEST)

            
        
                
        
        