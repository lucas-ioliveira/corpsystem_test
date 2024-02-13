<template>
  <div class="table-responsive">
    <div class="mb-3">
      <input type="text" v-model="termoBusca" class="" placeholder="Buscar vendedor por ID" @input="filtrarCliente">
    </div>
    <table class="table table-bordered table-striped">
      <thead class="thead-dark">
        <tr>
          <th>ID</th>
          <th>Nome</th>
          <th>Sobrenome</th>
          <th>Email</th>
          <th>Data de Nascimento</th>
          <th>Telefone</th>
          <th>Status</th>
          <th>CEP</th>
          <th>Logradouro</th>
          <th>Bairro</th>
          <th>Cidade</th>
          <th>Complemento</th>
          <th>UF</th>
          <th>Data de Criação</th>
          <th>Data de Atualização</th>
          <th>Ação</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="vendedor in vendedores" :key="vendedor.id">
          <td>{{ vendedor.id }}</td>
          <td>{{ vendedor.nome }}</td>
          <td>{{ vendedor.sobrenome }}</td>
          <td>{{ vendedor.email }}</td>
          <td>{{ vendedor.dt_nascimento }}</td>
          <td>{{ vendedor.telefone }}</td>
          <td>{{ vendedor.status }}</td>
          <td>{{ vendedor.cep }}</td>
          <td>{{ vendedor.logradouro }}</td>
          <td>{{ vendedor.bairro }}</td>
          <td>{{ vendedor.cidade }}</td>
          <td>{{ vendedor.complemento }}</td>
          <td>{{ vendedor.uf }}</td>
          <td>{{ vendedor.dt_criacao }}</td>
          <td>{{ vendedor.dt_atualizacao }}</td>
          <td>
            <button @click="editarCliente(cliente)">Editar</button>
          </td>
        </tr>
      </tbody>
    </table>
    <div v-if="!vendedores.length && errorMessage">{{ errorMessage }}</div>

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
      vendedores: [],
      clienteSelecionado: null,
      errorMessage: null
    }
  },
  methods: {
    fetchClientes() {
      axios.get('http://127.0.0.1:8000/api/v1/vendedor/')
        .then((response) => {
          this.vendedores = response.data;
          this.errorMessage = null;
        })
        .catch(() => {
          this.vendedores = [];
          this.errorMessage = 'Erro ao buscar os clientes';
        });
    },
    filtrarCliente() {
      this.termoBusca = parseInt(this.termoBusca);
      if (!this.termoBusca) {
        this.fetchClientes();
        return;
      }
      axios.get(`http://127.0.0.1:8000/api/v1/vendedor/detalhes/${this.termoBusca}`)
        .then((response) => {
          this.vendedores = response.data ? [response.data] : [];
          this.errorMessage = response.data ? null : 'Nenhum cliente encontrado com o ID fornecido.';
        })
        .catch(() => {
          this.vendedores = [];
          this.errorMessage = 'Erro ao buscar o cliente';
        });
    },
    editarCliente(vendedor) {
      this.clienteSelecionado = { ...vendedor }; 
    },
    fecharModal() {
      this.clienteSelecionado = null;
    },
    salvarEdicao() {

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
