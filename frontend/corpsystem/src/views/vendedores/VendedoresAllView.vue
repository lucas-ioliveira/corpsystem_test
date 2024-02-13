<template>
    
    <div>
    <h1>Lista de vendedores</h1>
    <TableVendedores/>
    </div>
    
</template>

<script>
import TableVendedores from '@/components/vendedores/TableVendedores.vue';
export default {
    name: 'VendedoresGetAll',
    components: {
        TableVendedores
    },
}
</script>