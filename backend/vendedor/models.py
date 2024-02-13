from clientes.models import CadastroClientes

class Vendedor(CadastroClientes):
    class Meta:
        db_table = "vendedores"
        verbose_name = "vendedor"
        verbose_name_plural = "vendedores"
    
    def __str__(self):
        return self.nome
