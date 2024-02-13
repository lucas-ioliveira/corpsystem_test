from django.db import models
from clientes.models import CadastroClientes
from vendedor.models import Vendedor
from produto.models import Produto

class Vendas(models.Model):
    PENDENTE = 1
    PROCESSANDO = 2
    FINALIZADO = 3

    CARTAO_CREDITO = 1
    CARTAO_DEBITO = 2
    DINHEIRO = 3
    PIX = 4
    BOLETO = 5

    TIPO_PAGAMENTO_CHOICES = (
        (CARTAO_CREDITO, 'Cartão de credito'),
        (CARTAO_DEBITO, 'Cartão de debito'),
        (DINHEIRO, 'Dinheiro'),
        (PIX, 'Pix'),
        (BOLETO, 'Boleto'),
    )

    STATUS_VENDA_CHOICES = (
        (PENDENTE, 'Pendente'),
        (PROCESSANDO, 'Processando'),
        (FINALIZADO, 'Finalizado'),
    )

    cliente = models.ForeignKey(CadastroClientes, verbose_name='cliente', related_name='venda_cliente', on_delete=models.CASCADE)
    vendedor = models.ForeignKey(Vendedor,verbose_name='vendedor', related_name='venda_vendedor', on_delete=models.CASCADE)
    item_vendido = models.ForeignKey(Produto, verbose_name='item vendido', related_name='venda_item', on_delete=models.CASCADE)
    tipo_pagamento = models.IntegerField(verbose_name='tipo de pagamento', choices=TIPO_PAGAMENTO_CHOICES, default=PIX)
    status_venda = models.IntegerField(verbose_name='status da venda', choices=STATUS_VENDA_CHOICES, default=PROCESSANDO)
    venda_ativa = models.BooleanField(verbose_name='venda ativa', default=True, blank=True, null=True)
    dt_criacao = models.DateField(verbose_name='data de criacao', auto_now_add=True, blank=True, null=True)
    dt_atualizacao = models.DateField(verbose_name='data de atualizacao', auto_now=True, blank=True, null=True)

    class Meta:
        db_table = 'vendas'
        verbose_name = 'venda'
        verbose_name_plural = 'vendas'
    
    def __str__(self):
        return self.item_vendido.nome