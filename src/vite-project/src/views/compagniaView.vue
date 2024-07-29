<template>



    <div v-if="polizzeCompagnia.count == 0">
        <div class=" container mb-2 mt-3 d-flex justify-content-center">
            <div class="card" style="width: 18rem;">
                <img src="@/assets/compagnia.jpeg" class="card-img-top" alt="...">
                <div class="card-body">
                    <p class="card-text">Non hai ancora aggiunto polizze per questa compagnia.</p>
                </div>
                <button type="button" @click="eliminaCompagnia" class="btn btn-danger">Elimina Compagnia</button>
                
            </div>

        </div>
    </div>
    <div v-else-if="checkCompagnia">

        <div class=" container mb-2 mt-3">
            <h1>{{ nome }}</h1>
        </div>
        <div class="container mb-2 mt-3">
            <h3>Numero polizze compagnia: {{ polizzeCompagnia.count }}</h3>

        </div>


        <div class="container mt-3 mb-2 my-element">
            <div v-for="polizza in polizzeCompagnia.results" :key="polizza.id_polizza">
                <div class="card p-2 mb-4 shadow rounded mb-4">
                    <div class="card-body">
                        <router-link :to="{ name: 'polizza-view', params: { id: polizza.id_polizza } }"
                            class="polizza-link">
                            <h4>Nome: {{ polizza.cliente.nome }}</h4>
                            <h4>Cognome: {{ polizza.cliente.cognome }}</h4>
                            <h4>Targa: {{ polizza.veicolo }}</h4>
                            <h4>Semestrale: {{ polizza.semestrale }}</h4>


                            <h3>{{ polizza.data_fine }}</h3>
                        </router-link>
                    </div>
                </div>
            </div>
            <button type="button" @click="this.eliminaCompagnia" class="btn btn-danger">Elimina Compagnia</button>

            
            
        </div>
    </div>


    <div v-else>
        <h1 class="text-danger text-center">404 - Compagnia non trovata</h1>
    </div>

</template>


<script>
import { axios } from "@/common/api.service.js";
import { endpoints } from "@/common/endpoints.js";
import router from "../router";


export default {
    name: 'compagniaView',
    props: {
        nome: {
            type: String,
            required: true
        }
    },

    data() {
        return {
            polizzeCompagnia: [],
            checkCompagnia: true
        }
    },
    methods: {
        async getPolizzeCompagniaData() {
            const endpoint = `${endpoints["compagniePolizze"]}${this.nome}/`;
            try {
                const response = await axios.get(endpoint);
                this.polizzeCompagnia = response.data;
            } catch (error) {
                console.log(error);
                this.checkCompagnia = false;

            }
        },

        async eliminaCompagnia() {
            const conferma = window.confirm("Sei sicuro di voler eliminare questo cliente? Eliminando la compagnia verranno eliminate anche tutte le polizze emesse con questa compagnia.");
            if (!conferma) {
                return;
            }

            const endpoint = `${endpoints["compagnieDetail"]}${this.nome}/`;
            try {
                const response = await axios.delete(endpoint);
                router.push({ name: 'home' });
            } catch (error) {
                console.log(error);
            }
        }
    },
    created() {
        this.getPolizzeCompagniaData();
    }
}
</script>
