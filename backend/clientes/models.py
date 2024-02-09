from django.db import models
from django.contrib.auth.models import User


class CadastroClientes(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    dt_aniversario = models.DateField()
    telefone = models.CharField(max_length=15)
    status = models.BooleanField()
    cep = models.CharField(max_length=8)
    logradouro = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    complemento = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)
    dt_criacao = models.DateField(auto_now_add=True)
    dt_atualizacao = models.DateField(auto_now=True)

class Meta:
    db_table = "cadastro_clientes"
    verbose_name = "cadastro de cliente"
    verbose_name_plural = "cadastros de clientes"

def __str__(self):
    return self.usuario
