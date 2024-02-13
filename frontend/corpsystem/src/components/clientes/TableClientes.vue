<template>
  <div class="table-responsive">
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
        <tr v-for="cliente in clientes" :key="cliente.id">
          <td>{{ cliente.id }}</td>
          <td>{{ cliente.nome }}</td>
          <td>{{ cliente.sobrenome }}</td>
          <td>{{ cliente.email }}</td>
          <td>{{ cliente.dt_nascimento }}</td>
          <td>{{ cliente.telefone }}</td>
          <td>{{ cliente.status }}</td>
          <td>{{ cliente.cep }}</td>
          <td>{{ cliente.logradouro }}</td>
          <td>{{ cliente.bairro }}</td>
          <td>{{ cliente.cidade }}</td>
          <td>{{ cliente.complemento }}</td>
          <td>{{ cliente.uf }}</td>
          <td>{{ cliente.dt_criacao }}</td>
          <td>{{ cliente.dt_atualizacao }}</td>
          <td>
            <button @click="editarCliente(cliente.id)">Editar</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'TableClientes',
  data() {
    return {
      clientes: [],
      errorMessage: null
    }
  },
  mounted(){
    this.fetchClientes();
  },
  methods:{
    fetchClientes(){
      axios.get('http://127.0.0.1:8000/api/v1/clientes/')
      .then((response) => {
        this.clientes = response.data;
      }).catch(() => {
        this.errorMessage = 'Erro ao carregar os dados.';
      })
    },
    editarCliente(clienteId) {
    this.$router.push({ name: 'EditarClienteView', params: { id: clienteId } });
  }

  }
}
</script>

<style>
.table-responsive {
  overflow-x: auto;
}
</style>
