import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import 'bootstrap/dist/css/bootstrap.min.css'
window.__VUE_PROD_HYDRATION_MISMATCH_DETAILS__ = true;


createApp(App).use(router).mount('#app');