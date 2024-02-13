<template>
  <div>
    <h1 class="mb-3">Relatórios</h1>
    <form @submit.prevent="gerarRelatorio" class="w-50 mx-auto mb-3">

        <div class="form-group row  mb-3">
            <label for="relatorio" class="col-sm-3 col-form-label">Formato do relatorio:</label>
            <div class="col-sm-9">
                <input type="text" id="relatorio" v-model="relatorio" class="form-control">
            </div>
        </div>
       
        <div class="form-group row  mb-3">
            <label for="vendedor" class="col-sm-3 col-form-label">Vendedor:</label>
            <div class="col-sm-9">
                <input type="text" id="vendedor" v-model="vendedor" class="form-control">
            </div>
        </div>
        <div class="form-group row  mb-3">
            <label for="cliente" class="col-sm-3 col-form-label">Cliente:</label>
            <div class="col-sm-9">
                <input type="text" id="cliente" v-model="cliente" class="form-control">
            </div>
        </div>
        <div class="form-group row">
            <label for="data" class="col-sm-3 col-form-label">Data:</label>
            <div class="col-sm-9  mb-3">
            <input type="date" id="data" v-model="data" class="form-control">
            </div>
        </div>
        <div class="form-group row  mb-3">
            <div class="col-sm-9">
                <button type="submit" class="btn btn-primary">Gerar Relatório</button>
            </div>
      </div>
    </form>
  </div>
</template>

<script>
import axios from 'axios';
import { saveAs } from 'file-saver';

export default {
  data() {
    return {
      data: '',
      vendedor: '',
      cliente: '',
      opcao: 'pdf', // Define PDF como opção padrão
    };
  },
  methods: {
    async gerarRelatorio() {
      try {
        const formattedData = this.data ? new Date(this.data).toISOString().slice(0, 10) : '';
        const params = {
          data: formattedData,
          vendedor: parseInt(this.vendedor),
          cliente: this.cliente,
          opcao: this.opcao
        };

        const response = await axios.post('http://127.0.0.1:8000/api/v1/relatorios/exportar/', params, {
          responseType: 'blob'
        });

        if (this.opcao === 'pdf') {
          const url = window.URL.createObjectURL(new Blob([response.data]));
          const link = document.createElement('a');
          link.href = url;
          link.setAttribute('download', 'relatorio.pdf');
          document.body.appendChild(link);
          link.click();
        } else if (this.opcao === 'excel') {
          const contentType = response.headers['content-type'];
          const blob = new Blob([response.data], { type: contentType });
          saveAs(blob, 'relatorio.xlsx');
        }
      } catch (error) {
        console.error('Erro ao gerar relatório:', error);
      }
    }
  }
}
</script>

<style scoped>
</style>
