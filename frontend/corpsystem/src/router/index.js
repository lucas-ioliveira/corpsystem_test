// router/index.js
import { createRouter, createWebHistory } from 'vue-router';
import LoginFormView from '../views/login/LoginFormView.vue';
import DashInfoView from '../views/dashboard/DashInfoView.vue';
import ClientesAllView from '../views/clientes/ClientesAllView.vue';
import EditarClienteView from '../views/clientes/EditarClienteView.vue';
import RelatorioFormView from '../views/relatorios/RelatorioFormView.vue';
import ProdutosAllView from '../views/produtos/ProdutosAllView.vue';
import VendaAllView from '../views/vendas/VendaAllView.vue';
import VendedoresAllView from '../views/vendedores/VendedoresAllView.vue';
const routes = [
  { path: '/', name: 'LoginFormView', component: LoginFormView },
  { path: '/dashboard', name: 'DashInfoView', component: DashInfoView },
  { path: '/clientes', name: 'ClientesAllView', component: ClientesAllView },
  { path: '/relatorios', name: 'RelatorioFormView', component: RelatorioFormView },
  { path: '/produtos', name: 'ProdutosAllView', component: ProdutosAllView },
  { path: '/vendas', name: 'VendaAllView', component: VendaAllView },
  { path: '/vendedores', name: 'VendedoresAllView', component: VendedoresAllView },
  { path: '/editar-cliente/:id', name: 'EditarClienteView', component: EditarClienteView },

];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
