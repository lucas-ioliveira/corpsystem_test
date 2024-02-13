from django.db import models


class CadastroClientes(models.Model):
    nome = models.CharField(verbose_name="nome", max_length=100, blank=True, null=True)
    sobrenome = models.CharField(verbose_name="sobrenome", max_length=100, blank=True, null=True)
    email = models.EmailField(verbose_name="email", max_length=100, blank=True, null=True)
    dt_aniversario = models.DateField(verbose_name="data de aniversario", blank=True, null=True)
    telefone = models.CharField(verbose_name="telefone", max_length=15, blank=True, null=True)
    status = models.BooleanField(verbose_name="status", default=True, blank=True, null=True)
    cep = models.CharField(verbose_name="cep", max_length=8, blank=True, null=True)
    logradouro = models.CharField(verbose_name="logradouro", max_length=100, blank=True, null=True)
    bairro = models.CharField(verbose_name="bairro", max_length=100, blank=True, null=True)
    cidade = models.CharField(verbose_name="cidade", max_length=100, blank=True, null=True)
    complemento = models.CharField(verbose_name="complemento", max_length=100, blank=True, null=True)
    uf = models.CharField(verbose_name="uf", max_length=2, blank=True, null=True)
    dt_criacao = models.DateField(verbose_name="data de criacao", auto_now_add=True, blank=True, null=True)
    dt_atualizacao = models.DateField(verbose_name="data de atualizacao", auto_now=True, blank=True, null=True)

    class Meta:
        db_table = "cadastro_clientes"
        verbose_name = "cadastro de cliente"
        verbose_name_plural = "cadastros de clientes"

    def __str__(self):
        return self.nome + " " + self.sobrenome
