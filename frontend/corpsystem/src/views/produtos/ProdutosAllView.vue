<template>
    
    <div>
    <h1>Lista de Produtos</h1>
    <TableProdutos/>
    </div>
    
</template>

<script>
import TableProdutos from '@/components/produtos/TableProdutos.vue';
export default {
    name: 'ClientesGetAll',
    components: {
        TableProdutos
    },
}
</script>