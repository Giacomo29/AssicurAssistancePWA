<template>
    <div class="input-group mb-3 position-relative" ref="dropdown">
        <button class="btn btn-outline-secondary dropdown-toggle" @click="toggleDropdown" type="button"
            aria-expanded="false">
            Cliente

        </button>
        <input type="text" class="form-control" :value="selectedClienteText" />
        <ul class="dropdown-menu position-absolute w-100" :class="{ show: showDropdown }">
            <li>
                <input type="text" class="form-control dropdown-input" placeholder="Cerca..." v-model="searchQuery"
                    @input="filterClienti" />
                    <Spinner :loading="loading" color="primary" size="sm" />
            </li>
            <li v-for="(cliente, index) in filteredClienti" :key="index">
                <a class="dropdown-item" @click="selezionaCliente(cliente)" href="#">{{ cliente.cognome }} {{
            cliente.nome }} - {{ cliente.codice_fiscale }}</a>
            </li>
        </ul>
    </div>
</template>

<script>
import Spinner from './Spinner.vue';

export default {

    components: {
        Spinner,
    },

    props: {
        clienti: {
            type: Array,
            required: true
        },
        value: {
            type: String,
            default: ''
        },

        loading: {
            type: Boolean,
            required: true
        },
    },
    data() {
        return {
            searchQuery: '',
            selectedCliente: null,
            showDropdown: false
        };
    },
    computed: {
        filteredClienti() {
            if (!this.searchQuery) {
                return this.clienti;
            }
            const query = this.searchQuery.toLowerCase();
            return this.clienti.filter(cliente => {
                return cliente.cognome.toLowerCase().includes(query) ||
                    cliente.nome.toLowerCase().includes(query) ||
                    cliente.codice_fiscale.toLowerCase().includes(query);
            });
        },
        selectedClienteText() {
            if (this.selectedCliente) {
                return `${this.selectedCliente.cognome} ${this.selectedCliente.nome} - ${this.selectedCliente.codice_fiscale}`;
            }
            return '';
        }
    },
    methods: {
        toggleDropdown() {
            this.showDropdown = !this.showDropdown;
        },
        filterClienti() {
            this.showDropdown = true;
        },
        selezionaCliente(cliente) {
            this.selectedCliente = cliente;
            this.searchQuery = '';
            this.showDropdown = false;
            this.$emit('input', this.selectedClienteText);
            this.$emit('clienteSelezionato', cliente);
        },
        handleClickOutside(event) {
            if (this.$refs.dropdown && !this.$refs.dropdown.contains(event.target)) {
                this.showDropdown = false;
            }
        }
    },
    watch: {
        value(newValue) {
            this.searchQuery = newValue;
        }
    },
    mounted() {
        document.addEventListener('click', this.handleClickOutside);
    },
    beforeDestroy() {
        document.removeEventListener('click', this.handleClickOutside);
    }
};
</script>

<style scoped>
.dropdown-input {
    margin: 5px;
}
</style>