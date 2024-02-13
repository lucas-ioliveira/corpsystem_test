<template>
    
    <div>
    <h1>Lista de Vendas</h1>
    <TableVendas/>
    </div>
    
</template>

<script>
import TableVendas from '@/components/vendas/TableVendas.vue';
export default {
    name: 'VendasGetAll',
    components: {
        TableVendas
    },
}
</script>