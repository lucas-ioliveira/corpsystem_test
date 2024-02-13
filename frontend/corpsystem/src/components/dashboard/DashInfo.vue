<template>
  <div class="container-fluid d-flex">
    <!-- Menu lateral -->
    <div class="sidebar">
      <!-- Título centralizado -->
      <h3 class="text-center mt-3 mb-3">CORPSYSTEM</h3>
      <!-- Links do menu -->
      <ul class="list-group mt-3">
        <li class="list-group-item mb-3"><router-link to="/clientes">Clientes</router-link></li>
        <li class="list-group-item mb-3"><router-link to="/produtos">Produtos</router-link></li>
        <li class="list-group-item mb-3"><router-link to="/vendas">Vendas</router-link></li>
        <li class="list-group-item mb-3"><router-link to="/vendedores">Vendedores</router-link></li>
       <li class="list-group-item mb-3"><router-link to="/relatorios">Relatórios</router-link></li>
      </ul>
    </div>

    <!-- Conteúdo principal -->
    <div class="content">
      <!-- Título centralizado -->
      <h1 class="text-center mt-5 mb-4">CORPSYSTEM ERP</h1>
      
      <!-- Conteúdo da página -->
      <div class="row">
        <div class="col-md-4 mb-4"> 
          <div class="card h-100"> 
            <div class="card-body">
              <h5 class="card-title">Clientes</h5>
              <router-link to="/clientes" class="btn btn-primary">Visualizar</router-link>
            </div>
          </div>
        </div>
        <div class="col-md-4 mb-4"> 
          <div class="card h-100"> 
            <div class="card-body">
              <h5 class="card-title">Produtos</h5>
              <router-link to="/produtos" class="btn btn-primary">Visualizar</router-link>
            </div>
          </div>
        </div>
        <div class="col-md-4 mb-4"> 
          <div class="card h-100"> 
            <div class="card-body">
              <h5 class="card-title">Vendas</h5>
             <router-link to="/vendas" class="btn btn-primary">Visualizar</router-link>
            </div>
          </div>
        </div>
        <div class="col-md-4 mb-4"> 
          <div class="card h-100"> 
            <div class="card-body">
              <h5 class="card-title">Vendedores</h5>
              <router-link to="/vendedores" class="btn btn-primary">Visualizar</router-link>
            </div>
          </div>
        </div>
        <div class="col-md-4 mb-4"> 
          <div class="card h-100"> 
            <div class="card-body">
              <h5 class="card-title">Relatórios</h5>
             <router-link to="/relatorios" class="btn btn-primary">Visualizar</router-link>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  
}
</script>

<style scoped>
/* Remover margem padrão do body */
body {
  margin: 0;
}

/* Estilização do menu lateral */
.sidebar {
  height: 100vh;
  width: 250px;
  background-color: #333;
  color: #fff;
  padding: 20px;
  border-radius: 10px ;
}

/* Estilização do título centralizado */
.sidebar h1 {
  margin-bottom: 20px;
}

/* Estilização dos links do menu */
.sidebar h3 {
  border-block-end: 1px solid #fff;
}

/* Estilização dos links do menu */
.sidebar ul {
  list-style-type: none;
  padding: 0;
  border-radius: 10px;
}

.sidebar a {
  color: #333;
  text-decoration: none;
}

/* Estilização do conteúdo */
.content {
  flex-grow: 1;
  padding: 20px;
  margin-top: 0; /* Removendo a margem superior */
}

a {
  color: #fff;
  text-decoration: none;

}

.card {
  height: 100%; /* Mantém a altura dos cards */
}


</style>
