<template>
    <div class="card text-bg-dark mb-3" style="max-width: 18rem;">
        <div class="card-header text-center">Aggiungi Broker</div>
        <div class="card-body">
            <div class="input-group mb-3">
                <span class="input-group-text" id="basic-addon1">Nome</span>
                <input type="text" class="form-control" placeholder="Nome Broker" v-model="data_broker.nome" required
                    aria-describedby="basic-addon1">
            </div>
            <div class="input-group mb-3">
                <span class="input-group-text" id="basic-addon2">Note</span>
                <textarea class="form-control" placeholder="Note" v-model="data_broker.note"
                    aria-describedby="basic-addon2"></textarea>
            </div>
            <button type="button" @click="aggiungiBroker" class="btn btn-info mx-auto d-block">Aggiungi</button>
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
            data_broker: {
                nome: '',
                note: ''
            }
        };
    },
    methods: {
        // Add a new broker
        async aggiungiBroker() {
            try {
                let endpoint = `${endpoints["brokerList"]}`;
                await axios.post(endpoint, this.data_broker);
                this.$emit('update:modelValue', false); // Imposta addBroker su false
                toast.success("Broker aggiunto", { position: "top-right", duration: 5000 });
            } catch (error) {
                console.log(error);
            }
        },
    }
};
</script>