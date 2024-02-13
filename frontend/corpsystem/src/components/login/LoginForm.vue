<template>
  <div class="container mt-5">
    <div class="row justify-content-center">
      <div class="col-md-6">
        <div class="card">
          <div class="card-header bg-primary text-white">Login</div>
          <div class="card-body">
            <form @submit.prevent="login">
              <div class="form-group mb-3">
                <input type="text" class="form-control" id="username" aria-describedby="emailHelp" placeholder="Enter username" v-model="username" required>
              </div>
              <div class="form-group mb-3">
                <input type="password" class="form-control" placeholder="Password" v-model="password" required>
              </div>
              <button type="submit" class="btn btn-primary w-100">Entrar</button>
            </form>
            <p class="mt-3" v-if="errorMessage" style="color: red;">{{ errorMessage }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      username: '',
      password: '',
      errorMessage: ''
    };
  },
  methods: {
    async login() {
      try {
        const response = await axios.post('http://127.0.0.1:8000/api/v1/login/', {
          username: this.username,
          password: this.password
        });
        const token = response.data.token;

        // Armazenar o token no localStorage
        localStorage.setItem('token', token);

        // Redirecionar para a tela de dashboard
        this.$router.push('/dashboard');
        
      } catch (error) {
        this.errorMessage = 'Usuário ou senha inválidos.';
        console.error('Erro ao autenticar:', error);
      }
    }
  }
};
</script>


<style scoped>
/* Estilos específicos para este componente, se necessário */
</style>
