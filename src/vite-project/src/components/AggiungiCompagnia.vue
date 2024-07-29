<template>

    <div class="card text-bg-dark mb-3" style="max-width: 18rem;">


        <div class="card-header">Aggiungi Compagnia</div>
        <div class="card-body">


            <div class="input-group mb-3">
                <button class="btn btn-outline-secondary dropdown-toggle" @click="this.showBroker()" type="button"
                    data-bs-toggle="dropdown" aria-expanded="false">Broker</button>
                <ul class="dropdown-menu">
                    <li v-for="(broker, index) in this.lista_broker_copy.results" :key="index">
                        <a class="dropdown-item" @click="this.selezionaBroker(broker)" href="#"> {{ broker.nome }}</a>
                    </li>
                </ul>
                <input type="text" class="form-control" aria-label="Broker" readonly
                    v-model="this.data_compagnia.broker">
            </div>

            <div class="input-group mb-3">
                <span class="input-group-text" id="basic-addon1">Nome</span>
                <input type="text" class="form-control" placeholder="Nome Compagnia" v-model="this.data_compagnia.nome"
                    required aria-label="Username" aria-describedby="basic-addon1">
            </div>
            <div class="input-group mb-3">
                <span class="input-group-text" id="basic-addon1">Email</span>
                <input type="text-area" class="form-control" placeholder="email" v-model="this.data_compagnia.email"
                    aria-label="Username" aria-describedby="basic-addon1">
            </div>

            <div class="input-group mb-3">
                <span class="input-group-text" id="basic-addon1">Telefono</span>
                <input type="text-area" class="form-control" placeholder="telefono"
                    v-model="this.data_compagnia.telefono" aria-label="Username" aria-describedby="basic-addon1">
            </div>

            <div class="input-group mb-3">
                <span class="input-group-text" id="basic-addon1">Sito Web</span>
                <input type="text-area" class="form-control" placeholder="sito web"
                    v-model="this.data_compagnia.sito_web" aria-label="Username" aria-describedby="basic-addon1">
            </div>


            <button type="button" @click="this.aggiungiCompagnia" class="btn btn-info">Aggiungi</button>
        </div>


    </div>

</template>

<script>

import { axios } from "@/common/api.service.js";
import { endpoints } from "@/common/endpoints.js";
import { toast } from "vue3-toastify";


export default {

    props: {

        modelValue: {
            type: Boolean,
            required: true
        }

    },

    data() {
        return {
            data_compagnia: {},
            lista_broker_copy: []
        };
    },
    methods: {
        // Add a new company
        async aggiungiCompagnia() {
            try {
                let endpoint = `${endpoints["compagnieList"]}`;
                this.data_compagnia.nome = `${this.data_compagnia.nome} - ${this.data_compagnia.broker}`;
                await axios.post(endpoint, this.data_compagnia);
                this.$emit('update:modelValue', false); // Imposta addBroker su false
                this.$emit('aggiuntaCompagnia');
                toast.success("Compagnia aggiunta", { position: "top-right", duration: 5000 });
            } catch (error) {
                console.log(error);
            }
        },

        // Fetch list of brokers
        async showBroker() {
            try {
                const endpoint = `${endpoints["brokerList"]}`;
                const response = await axios.get(endpoint);
                this.lista_broker_copy = response.data;
            } catch (error) {
                console.log(error);
            }
        },

        selezionaBroker(broker) {
            this.data_compagnia.broker = `${broker.nome}`;
        },
    }
};


</script>