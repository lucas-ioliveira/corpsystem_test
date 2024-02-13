<template>
  <div class="table-responsive">
    <div class="mb-3">
      <input type="text" v-model="termoBusca" class="" placeholder="Buscar produto por ID" @input="filtrarCliente">
    </div>
    <table class="table table-bordered table-striped">
      <thead class="thead-dark">
        <tr>
          <th>ID</th>
          <th>Nome</th>
          <th>Descricão</th>
          <th>Status</th>
          <th>Preço</th>
          <th>Estoque</th>
          <th>Data de Criação</th>
          <th>Data de Atualização</th>
          <th>Grupo</th>
          <th>Ação</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="produto in produtos" :key="produto.id">
          <td>{{ produto.id }}</td>
          <td>{{ produto.nome }}</td>
          <td>{{ produto.descricao }}</td>
          <td>{{ produto.status }}</td>
          <td>{{ produto.preco }}</td>
          <td>{{ produto.estoque }}</td>
          <td>{{ produto.dt_criacao }}</td>
          <td>{{ produto.dt_atualizacao }}</td>
          <td>{{ produto.grupo }}</td>
          <td>
            <button @click="editarCliente(cliente)">Editar</button>
          </td>
        </tr>
      </tbody>
    </table>
    <div v-if="!produtos.length && errorMessage">{{ errorMessage }}</div>

    <div class="modal" v-if="clienteSelecionado">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">Editar Cliente</h5>
            <button type="button" class="close" @click="fecharModal">&times;</button>
          </div>
          <div class="modal-body">
            <!-- Formulário de edição do cliente -->
            <label for="nome">Nome:</label>
            <input type="text" v-model="clienteSelecionado.nome" id="nome">
            <!-- Adicione mais campos conforme necessário para editar os dados do cliente -->
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" @click="fecharModal">Fechar</button>
            <button type="button" class="btn btn-primary" @click="salvarEdicao">Salvar</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'TableProdutos',
  data() {
    return {
      termoBusca: '',
      produtos: [],
      clienteSelecionado: null,
      errorMessage: null
    }
  },
  methods: {
    fetchClientes() {
      axios.get('http://127.0.0.1:8000/api/v1/produto/')
        .then((response) => {
          this.produtos = response.data;
          this.errorMessage = null;
        })
        .catch(() => {
          this.produtos = [];
          this.errorMessage = 'Erro ao buscar os clientes';
        });
    },
    filtrarCliente() {
      this.termoBusca = parseInt(this.termoBusca);
      if (!this.termoBusca) {
        this.fetchClientes();
        return;
      }
      axios.get(`http://127.0.0.1:8000/api/v1/produto/detalhes/${this.termoBusca}`)
        .then((response) => {
          this.produtos = response.data ? [response.data] : [];
          this.errorMessage = response.data ? null : 'Nenhum cliente encontrado com o ID fornecido.';
        })
        .catch(() => {
          this.produtos = [];
          this.errorMessage = 'Erro ao buscar o cliente';
        });
    },
    editarCliente(produto) {
      this.clienteSelecionado = { ...produto }; // Copia o objeto cliente para evitar a modificação direta dos dados na tabela
    },
    fecharModal() {
      this.clienteSelecionado = null;
    },
    salvarEdicao() {
      // Aqui você pode enviar os dados editados do cliente de volta para o servidor
      // Por exemplo, usando axios.put() ou axios.patch()
      // Não se esqueça de fechar a modal após a conclusão da operação
      this.fecharModal();
    }
  },
  mounted() {
    this.fetchClientes();
  }
}
</script>

<style>
.table-responsive {
  overflow-x: auto;
}

/* Estilos para a modal */
.modal {
  display: block;
  position: fixed;
  z-index: 1000;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  overflow: auto;
  background-color: rgba(0, 0, 0, 0.4);
}

.modal-dialog {
  margin: 30px auto;
  width: 50%;
}

.modal-content {
  background-color: #fefefe;
  margin: 5% auto;
  padding: 20px;
  border: 1px solid #888;
  width: 80%;
}

.modal-header,
.modal-footer {
  padding: 10px 16px;
  background-color: #5bc0de;
  color: white;
}

.modal-header button.close {
  color: white;
  font-size: 26px;
}

.modal-body {
  padding: 20px;
}
</style>
