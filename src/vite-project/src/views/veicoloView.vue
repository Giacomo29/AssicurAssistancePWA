<template>
  <div>
    <h4>Veicolo: {{ veicolo.targa }}</h4>
    <h4>Marca: {{ veicolo.marca }}</h4>
    <h4>Modello: {{ veicolo.modello }}</h4>
    <h4>Cilindrata: {{ veicolo.cilindrata }}</h4>
    <h4>Alimentazione: {{ veicolo.alimentazione }}</h4>
    <h4>Anno di immatricolazione: {{ veicolo.anno_immatricolazione }}</h4>
    <div v-if="veicolo.assicurato">
      <h4>Veicolo assicurato</h4>
      <h4>ID Polizza: {{ polizza.results[0].id_polizza }}</h4>
      <h4>Data Scadenza: {{ polizza.results[0].data_fine }}</h4>
      <h4>Compagnia: {{ polizza.results[0].compagnia }}</h4>
      <h4>Note: {{ polizza.results[0].note }}</h4>
      <h4>Semestrale?</h4>
      <div>
        <span v-if="!polizza.results[0].semestrale">No</span>
        <span v-else>Scadenza secondo rinnovo: {{ polizza.results[0].data_fine_due }}</span>
      </div>
      <!-- Aggiungi altri dettagli della polizza come desideri -->
    </div>
    <h4 class="card-title text-danger mt-2" v-else>Veicolo non assicurato</h4>
    <div class="input-group mb-3">
    </div>
  </div>
</template>


<style>
.bg-color-danger {
background-color: rgb(254, 166, 166); /* Colore rosso */
}

.bg-color-warning {
background-color: #fcfccc; /* Colore giallo */
}

.bg-color-light {
background-color: #d5ffd1; /* Colore grigio chiaro */
}
</style>




<script>
import {axios} from "@/common/api.service.js";
import {endpoints} from "@/common/endpoints.js";
import 'flatpickr/dist/flatpickr.css';






export default {
  components: {
      VueFlatpickr,
  },
  name: 'ScadenzeNelMeseView',
  props: {
       targa:{
          type: String,
          required: true,
       }
   },
   data(){
       return {
          veicolo: {},
          polizza: {},
       }
   },

   
   methods: {
      async getVeicolo(){
        try{
          const endpoint = `${endpoints["veicoliDetail"]}${this.targa}/`;
          const response = await axios.get(endpoint);
          this.veicolo = response.data;
          this.getPolizza();
        }catch(error){
          console.log(error);
        }
      },

      async getPolizza(){
        try{
          const endpoint = `${endpoints["polizzeTarga"]}${this.veicolo.targa}/`;
          const response = await axios.get(endpoint);
          this.polizza = response.data;
          console.log(this.polizza);
        }catch(error){
          console.log(error);
        }
      }
          

   },
   created(){
       this.getVeicolo();
   }
   }
</script>