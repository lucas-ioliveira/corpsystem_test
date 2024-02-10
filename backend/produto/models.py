from django.db import models

class GrupoProduto(models.Model):
    nome = models.CharField(verbose_name='nome', max_length=15, blank=True, null=True)
    descricao = models.TextField(verbose_name='descricao', blank=True, null=True)
    status = models.BooleanField(verbose_name='status', default=True, blank=True, null=True)
    dt_criacao = models.DateField(verbose_name='data de criacao', auto_now_add=True, blank=True, null=True)
    dt_atualizacao = models.DateField(verbose_name='data de atualizacao', auto_now=True, blank=True, null=True)

    class Meta:
        db_table = 'grupo_produtos'
        verbose_name = 'Grupo de produtos'
        verbose_name_plural = 'Grupos de produtos'

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(verbose_name='nome', max_length=100)
    descricao = models.TextField(verbose_name='descricao', blank=True, null=True)
    status = models.BooleanField(verbose_name='status', default=True, blank=True, null=True)
    preco = models.DecimalField(verbose_name='preco', max_digits=10, decimal_places=2, blank=True, null=True)
    estoque = models.PositiveIntegerField(verbose_name='estoque', default=0, blank=True, null=True)
    grupo = models.ForeignKey('GrupoProduto', on_delete=models.CASCADE)
    dt_criacao = models.DateField(verbose_name='data de criacao', auto_now_add=True, blank=True, null=True)
    dt_atualizacao = models.DateField(verbose_name='data de atualizacao', auto_now=True, blank=True, null=True)

    class Meta:
        db_table = 'produtos'
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return self.nome