<template>
    
    <div>
    <h1>Lista de Clientes</h1>
    <TableClientes/>
    </div>
    
</template>

<script>
import TableClientes from '@/components/clientes/TableClientes.vue';
export default {
    name: 'ClientesGetAll',
    components: {
        TableClientes
    },
}
</script>