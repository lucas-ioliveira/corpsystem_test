<template>
  <div>
    <div v-if="clienteSelecionado">
      <h2>Editar Cliente</h2>
      <div class="form-group">
        <label for="nomeInput">Nome:</label>
        <input type="text" v-model="clienteSelecionado.nome" class="form-control" id="nomeInput">
      </div>
      <div class="form-group">
        <label for="sobrenomeInput">Sobrenome:</label>
        <input type="text" v-model="clienteSelecionado.sobrenome" class="form-control" id="sobrenomeInput">
      </div>
      <!-- Outros campos de edição aqui -->
      
      <button class="btn btn-primary" @click="salvarEdicao">Salvar</button>
      <button class="btn btn-secondary" @click="fecharModal">Cancelar</button>
    </div>

    <div v-if="errorMessage" class="alert alert-danger">{{ errorMessage }}</div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'EditarCliente',
  props: {
    clienteId: {
      type: Number,
      required: true
    }
  },
  data() {
    return {
      clienteSelecionado: null,
      errorMessage: ''
    };
  },
  methods: {
    fetchCliente() {
      axios.get(`http://127.0.0.1:8000/api/v1/clientes/detalhes/${this.clienteId}`)
        .then((response) => {
          this.clienteSelecionado = response.data;
          this.errorMessage = '';
        })
        .catch(() => {
          this.clienteSelecionado = null;
          this.errorMessage = 'Erro ao buscar o cliente.';
        });
    },
    salvarEdicao() {
      // Lógica para salvar a edição do cliente
    },
    fecharModal() {
      this.$emit('fechar');
    }
  },
  mounted() {
    this.fetchCliente();
  }
};
</script>

<style>
</style>
