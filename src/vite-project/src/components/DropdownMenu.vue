<template>
    <div class="input-group mb-3">
        <button class="btn btn-outline-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown"
            aria-expanded="false">Cliente</button>
        <ul class="dropdown-menu">
            <li v-for="(cliente, index) in filteredClienti" :key="index">
                <a class="dropdown-item" @click="selezionaCliente(cliente)" href="#">{{ cliente.cognome }} {{
                cliente.nome }} - {{ cliente.codice_fiscale }}</a>
            </li>
        </ul>
        <input type="text" class="form-control" aria-label="Text input with dropdown button" v-model="searchTerm"
            @input="searchClienti">
    </div>
</template>

<script>
export default {
    props: {
        clienti: {
            type: Array,
            required: true
        },
        data_polizza: {
            type: Object,
            required: true
        }
    },
    data() {
        return {
            searchTerm: ''
        };
    },
    computed: {
        filteredClienti() {
            return this.clienti.filter(cliente =>
                cliente.cognome.toLowerCase().includes(this.searchTerm.toLowerCase()) ||
                cliente.nome.toLowerCase().includes(this.searchTerm.toLowerCase()) ||
                cliente.codice_fiscale.toLowerCase().includes(this.searchTerm.toLowerCase())
            );
        }
    },
    methods: {
        selezionaCliente(cliente) {
            this.data_polizza.intestatario = `${cliente.cognome} ${cliente.nome} - ${cliente.codice_fiscale}`;
        },
        searchClienti() {
            this.filteredClienti = this.clienti.filter(cliente =>
                cliente.cognome.toLowerCase().includes(this.searchTerm.toLowerCase()) ||
                cliente.nome.toLowerCase().includes(this.searchTerm.toLowerCase()) ||
                cliente.codice_fiscale.toLowerCase().includes(this.searchTerm.toLowerCase())
            );
        }
    }
};
</script>

<!-- Aggiungi qui il CSS se necessario -->