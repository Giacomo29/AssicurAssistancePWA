<template>
  <div class="container mt-3">
    <div class="d-flex align-items-center justify-content-between mb-3">
      <h3>Cerca per scadenza o mostra tutte le polizze</h3>
      <div class="form-check form-switch">
        <input class="form-check-input" type="checkbox" id="showScadenzeSwitch" v-model="showScadenze">
        <label class="form-check-label" for="showScadenzeSwitch">Mostra scadenze mese</label>
      </div>
    </div>

    <div v-if="showScadenze">
      <div class="input-group mb-3">
        <select v-model="scadenzaMese" class="form-control">
          <option value="1">Gennaio</option>
          <option value="2">Febbraio</option>
          <option value="3">Marzo</option>
          <option value="4">Aprile</option>
          <option value="5">Maggio</option>
          <option value="6">Giugno</option>
          <option value="7">Luglio</option>
          <option value="8">Agosto</option>
          <option value="9">Settembre</option>
          <option value="10">Ottobre</option>
          <option value="11">Novembre</option>
          <option value="12">Dicembre</option>
        </select>

        <input type="number" v-model="scadenzaAnno" class="form-control" placeholder="Inserisci l'anno" aria-label=""
          aria-describedby="button-addon1">
        <button class="btn btn-primary" @click="getPolizzeInScadenza">Cerca</button>
      </div>


      <div v-if="loadingPolizze" class="text-center mt-3">
        <spinner :loading="loadingPolizze" color="primary" size="lg" />
      </div>
      <div v-else>

      <div v-if="polizzeInScadenza.count === 0">
        <h4 class="text-center">Nessuna polizza in scadenza in questo mese</h4>
      </div>
      <div v-else>
        <h4 class="text-center d-flex align-items-center justify-content-center">Polizze in scadenza in questo mese</h4>
      </div>

        <div class="container mt-3 mb-3">
          <div v-for="polizza in polizzeInScadenza.results" :key="polizza.id_polizza">
            <div class="card shadow rounded mb-4" :class="getPolizzaColor(polizza)">
              <div class="card-body">
                <router-link :to="{ name: 'polizza-view', params: { id: polizza.id_polizza } }">
                  <h4 class="text-dark">Nome: {{ polizza.cliente.nome }}</h4>
                  <h4 class="text-dark">Cognome: {{ polizza.cliente.cognome }}</h4>
                  <h4 class="text-dark">Targa: {{ polizza.veicolo }}</h4>
                  <h4 class="text-dark">Compagnia: {{ polizza.compagnia }}</h4>
                  <div v-if="polizza.semestrale === true">
                    <h4 class="text-dark">Semestrale: Si</h4>
                    <h3 class="text-dark">Scadenza prima rata: {{ polizza.data_fine }}</h3>
                    <h3 class="text-dark">Scadenza seconda rata: {{ polizza.data_fine_due }}</h3>
                  </div>
                  <div v-else>
                    <h4 class="text-dark">Semestrale: No</h4>
                    <h3 class="text-dark">Scadenza: {{ formatDate(polizza.data_fine) }}</h3>
                  </div>
                </router-link>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div v-else>
      <div v-if="loadingPolizze" class="text-center mt-3">
        <spinner :loading="loadingPolizze" color="primary" size="lg" />
      </div>
      <div v-for="polizza in all_polizze.results" :key="polizza.id_polizza">
        <div class="card shadow rounded mb-4" :class="getPolizzaColor(polizza)">
          <div class="card-body">
            <router-link :to="{ name: 'polizza-view', params: { id: polizza.id_polizza } }">
              <h4 class="text-dark">Nome: {{ polizza.cliente.nome }}</h4>
              <h4 class="text-dark">Cognome: {{ polizza.cliente.cognome }}</h4>
              <h4 class="text-dark">Targa: {{ polizza.veicolo }}</h4>
              <h4 class="text-dark">Compagnia: {{ polizza.compagnia }}</h4>
              <div v-if="polizza.semestrale === true">
                <h4 class="text-dark">Semestrale: Si</h4>
                <h3 class="text-dark">Scadenza prima rata: {{ polizza.data_fine }}</h3>
                <h3 class="text-dark">Scadenza seconda rata: {{ polizza.data_fine_due }}</h3>
              </div>
              <div v-else>
                <h4 class="text-dark">Semestrale: No</h4>
                <h3 class="text-dark">Scadenza: {{ formatDate(polizza.data_fine) }}</h3>
              </div>
            </router-link>
          </div>
        </div>
      </div>
    </div>

  </div>
</template>




<style>
.bg-color-danger {
  border: 5px solid rgba(253, 0, 0, 0.628);
  /* Rosso con trasparenza */
  /* Colore rosso */
}

.bg-color-warning {
  border: 5px solid #eaea7a;
  /* Colore giallo */
}

.bg-color-light {
  border: 5px solid #9af892;
}


a {
  text-decoration: none;
  /* Rimuovi la sottolineatura */
  color: inherit;
  /* Eredità il colore dallo stile genitore (text-dark) */
}

a:hover {
  text-decoration: none;
  /* Rimuovi la sottolineatura anche al passaggio del mouse */
  color: inherit;
  /* Eredità il colore anche al passaggio del mouse */
}
</style>




<script>
import { axios } from "@/common/api.service.js";
import { endpoints } from "@/common/endpoints.js";

import { toast } from "vue3-toastify";
import "vue3-toastify/dist/index.css";
import Spinner from "../components/Spinner.vue";









export default {
  components: {
    Spinner,
  },
  name: 'ScadenzeNelMeseView',
  props: {
    nome: {
      type: String,

    }
  },
  data() {
    return {
      showScadenze: true,
      scadenzaMese: null,
      scadenzaAnno: null,
      polizzeInScadenza: [],
      data_cliente: {},
      data_veicolo: {},
      data_proprietario: {},
      data_polizza: {},
      all_polizze: [],
      loadingPolizze: false,

    }
  },


  methods: {

    // Metodo per ottenere le polizze in scadenza
    async getPolizzeInScadenza() {
      this.loadingPolizze = true;
      const currentDate = new Date();
      const currentMonth = currentDate.getMonth(); // Mesi numerati da 0 a 11, quindi aggiungiamo 1
      const currentYear = currentDate.getFullYear();

      if (this.scadenzaMese === null) {
        this.scadenzaMese = currentMonth + 1;
      }

      if (this.scadenzaAnno === null) {
        this.scadenzaAnno = currentYear;
      }

      const endpoint = `${endpoints["polizzeScadenza"]}${this.scadenzaMese}/?anno=${this.scadenzaAnno}`;

      try {
        const response = await axios.get(endpoint);
        this.polizzeInScadenza = response.data;
        this.loadingPolizze = false;
      } catch (error) {
        console.log(error);
        alert(error.response.statusText);

      }
    },


    //metodo che restituisce tutte le polizze in ordine di scadenza

    async getAllPolizze() {
      this.loadingPolizze = true;
      const endpoint = `${endpoints["polizzeList"]}`;
      try {
        const response = await axios.get(endpoint);
        this.all_polizze = response.data;
        this.loadingPolizze = false;
      } catch (error) {
        console.log(error);
        alert(error.response.statusText);
      }

    },

    formatDate(date) {
      const options = { day: '2-digit', month: 'long', year: 'numeric' };
      return new Date(date).toLocaleDateString(undefined, options);
    },



    getPolizzaColor(polizza) {

      const dataOggi = new Date();
      const dataScadenza1 = new Date(polizza.data_fine);
      const dataScadenza2 = polizza.data_fine_due ? new Date(polizza.data_fine_due) : null;

      // Calcola la differenza in giorni tra oggi e la prima data di scadenza
      const diffGiorni1 = Math.floor((dataScadenza1 - dataOggi) / (1000 * 60 * 60 * 24));

      // Se c'è una seconda data di scadenza, calcola la differenza in giorni anche per quella
      let diffGiorni2 = null;
      if (dataScadenza2) {
        diffGiorni2 = Math.floor((dataScadenza2 - dataOggi) / (1000 * 60 * 60 * 24));
      }

      // Se entrambe le date di scadenza sono passate, restituisci "contorno_rosso flashing-red"
      if (diffGiorni1 <= 0 && (!dataScadenza2 || diffGiorni2 <= 0)) {
        return "contorno_rosso flashing-red";
      }
      // Se solo la prima data di scadenza è passata, restituisci "contorno_rosso"
      else if (diffGiorni1 <= 0 || (diffGiorni2 !== null && diffGiorni2 <= 0)) {
        return "contorno_rosso";
      }
      // Altrimenti, valuta la differenza in giorni per entrambe le date e restituisci il colore corrispondente
      else if (diffGiorni1 <= 7 || (diffGiorni2 !== null && diffGiorni2 <= 7)) {
        return "contorno_rosso";
      } else if (diffGiorni1 <= 30 || (diffGiorni2 !== null && diffGiorni2 <= 30)) {
        return "contorno_giallo";
      } else {
        return "contorno_verde";
      }
    },
  },
  created() {
    this.getPolizzeInScadenza();
    this.getAllPolizze();
  }
}
</script>

<style scoped>
@keyframes flash {
  0% {
    background-color: transparent;
  }

  50% {
    background-color: rgba(249, 0, 0, 0.395);
  }

  100% {
    background-color: transparent;
  }
}

.flashing-red {
  animation: flash 3s infinite;
}
</style>
```