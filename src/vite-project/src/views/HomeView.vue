<template>
  <div class="container mt-4">




    <div v-if="authStore.isAuthenticated == true">



      <h2 v-if="authStore.authUser.user != undefined" id="saluto-personalizzato" class="text-center">Ciao {{
      authStore.authUser.user.nome }}!</h2>



      <div class="d-flex justify-content-center align-items-center mb-4 mt-4">





        <div class="d-flex flex-column align-items-center">
          <img :src="broker_img" alt="Aggiungi Broker" class="icon_add_home" @click="addBroker = !addBroker">
          <div class="mt-2">
            <p class="text-center">Broker</p>
          </div>
        </div>


        <div class="d-flex flex-column align-items-center">
          <img :src="compagnia_img" alt="Aggiungi Compagnia" class="icon_add_home"
            @click="addCompagnia = !addCompagnia">
          <div class="mt-2">
            <p class="text-center">Compagnia</p>
          </div>
        </div>




      </div>

      <div v-if="this.addBroker == true" class="d-flex justify-content-center">



        <AggiungiBroker v-model="addBroker" />


      </div>

      <div v-if="this.addCompagnia == true" class="d-flex justify-content-center">


        <AggiungiCompagnia v-model="addCompagnia" @aggiuntaCompagnia="this.getCompagnie();" />

      </div>


      <hr color="blue" size="2" width="100%" noshade>
      <div>
        <!-- Utilizza la direttiva @click per associare la funzione toggleVisibility all'evento di clic -->
        <h3 @click="toggleVisibility" style="color:#595959">Portafoglio corrente: {{ importoVisibile ? portafoglio + '€'
      : '•••••• €' }}</h3>
      </div>




      <div class="container mt-4 my-element shadow">
        <div v-if="compagnie.length == 0">
          <div class="d-flex align-items-center justify-content-center">
            <h4>Nessuna compagnia presente</h4>
          </div>
        </div>

        <div v-else>


          <div id="carouselExampleIndicators" class="carousel slide mt-5 mb-5" data-bs-ride="carousel"
            data-bs-touch="true">
            <ol class="carousel-indicators mb-0">
              <li v-for="(compagnia, index) in compagnieChunks" :key="index"
                :data-bs-target="'#carouselExampleIndicators'" :data-bs-slide-to="index"
                :class="{ active: index === 0 }">
              </li>
            </ol>

            <div class="carousel-inner">
              <div class="carousel-item" v-for="(compagniaChunk, index) in compagnieChunks" :key="index"
                :class="{ active: index === 0 }">

                <div class="row justify-content-center align-items-center">
                  <div class="col-sm-4 mb-3 mb-sm-0" v-for="compagnia in compagniaChunk" :key="compagnia.nome">
                    <router-link :to="{ name: 'compagnia-view', params: { nome: compagnia.nome } }">
                      <div class="card p-2 mb-4 shadow rounded custom-card contorno_compangnie">
                        <div class="card-body">
                          <h5 class="card-title">{{ compagnia.nome }}</h5>
                        </div>
                      </div>
                    </router-link>
                  </div>
                </div>
              </div>
            </div>
            <a class="carousel-control-prev d-none d-sm-block" href="#carouselExampleIndicators" role="button"
              data-bs-slide="prev">
              <span class="carousel-control-prev-icon" aria-hidden="true"></span>
              <span class="visually-hidden">Previous</span>
            </a>
            <a class="carousel-control-next d-none d-sm-block" href="#carouselExampleIndicators" role="button"
              data-bs-slide="next">
              <span class="carousel-control-next-icon" aria-hidden="true"></span>
              <span class="visually-hidden">Next</span>
            </a>
          </div>





        </div>


        <div class="container d-flex justify-content-center mb-2 mt-2">
        </div>
        <div class="d-flex justify-content-center mb-2 mt-2">
          <router-link :to="{ name: 'scadenze-view' }">
            <button type="button" class="btn btn-success btn-lg mx-3">Scadenze</button>
          </router-link>

          <router-link :to="{ name: 'nuova-polizza-view', params: { id: '' } }">
            <button class="btn btn-primary btn-lg mx-3"> Assicura</button>
          </router-link>

          <router-link :to="{ name: 'clienti-view' }">
            <button class="btn btn-warning btn-lg mx-3">Clienti</button>
          </router-link>





        </div>




        <div v-if="loading" class="text-center mt-3">
          <spinner :loading="loading" color="primary" size="lg" />
        </div>

        <div v-else>
          <div v-if="compagnie.length == 0 || polizzeInScadenza.count == 0">
            <h4 class="text-center mt-5">Nessuna polizza in scadenza nel mese corrente</h4>
          </div>

          <div v-else>
            <h4 class="text-center mt-5">Polizze in scadenza in questo mese</h4>

            <div class="container">
              <template v-if="polizzeInScadenza.results.length > 0">
                <div v-for="polizza in polizzeInScadenza.results" :key="polizza.id_polizza">
                  <div class="card shadow rounded mb-4">
                    <div class="card-body contorno_polizza">
                      <router-link :to="{ name: 'polizza-view', params: { id: polizza.id_polizza } }"
                        class="polizza-link">
                        <h4>Nome: {{ polizza.cliente.nome }}</h4>
                        <h4>Cognome: {{ polizza.cliente.cognome }}</h4>
                        <h4>Targa: {{ polizza.veicolo }}</h4>
                        <h4>Compagnia: {{ polizza.compagnia }}</h4>
                        <div v-if="polizza.semestrale === true">
                          <h4>Semestrale: Si</h4>
                          <h3>Scadenza prima rata: {{ formatDate(polizza.data_fine) }}</h3>
                          <h3>Scadenza seconda rata: {{ formatDate(polizza.data_fine) }}</h3>
                        </div>
                        <div v-else>
                          <h4>Semestrale: No</h4>
                          <h3>Scadenza: {{ formatDate(polizza.data_fine) }}</h3>
                        </div>
                      </router-link>
                    </div>
                  </div>
                </div>
              </template>
            </div>
          </div>


        </div>
      </div>


    </div>
    <div v-else="!authStore.user">
      <!-- redirecting to login -->

      <div class="d-flex align-items-center justify-content-center" style="height: 100vh;">
        <h1>Redirecting to login...</h1>
      </div>





    </div>
  </div>
</template>




<script>




import { axios } from "@/common/api.service.js";
import { endpoints } from "@/common/endpoints.js";
import { useAuthStore } from '@/stores/auth';
import "vue3-toastify/dist/index.css";
import AggiungiBroker from '@/components/AggiungiBroker.vue';
import AggiungiCompagnia from "../components/AggiungiCompagnia.vue";
import broker_img from "../assets/broker_img.svg";
import compagnia_img from "../assets/compagnia_img.svg";
import Spinner from "@/components/Spinner.vue";

export default {
  components: {
    AggiungiBroker,
    AggiungiCompagnia,
    Spinner,
  },
  setup() {
    const authStore = useAuthStore();

    return { authStore };
  },

  name: 'HomeView',

  data() {
    return {
      compagnie: [],
      polizzeInScadenza: [],
      scadenzaMese: null,
      scadenzaAnno: null,
      inputValue: null,
      test: [],
      addCompagnia: false,
      addBroker: false,
      portafoglio: 0,
      importoVisibile: false,
      broker_img: broker_img,
      compagnia_img: compagnia_img,
      loading: false,

    };
  },

  computed: {

    // Generate personalized greeting message based on the time of day and user's name
    salutoPersonalizzato() {
      if (this.authStore.authUser.user === null) {
        return;
      }

      const nome = this.authStore.authUser.user.nome;
      const ora = new Date().getHours();
      let saluto;

      if (ora >= 5 && ora < 12) {
        saluto = "Buongiorno";
      } else if (ora >= 12 && ora < 18) {
        saluto = "Buon pomeriggio";
      } else {
        saluto = "Buonasera";
      }
      return saluto + " " + nome + "!";
    },

    // Divide companies into chunks of two for better display
    compagnieChunks() {
      if (!this.compagnie || !this.compagnie.results || this.compagnie.results.length === 0) {
        return [];
      }

      const chunkSize = 2;
      const chunks = [];
      let index = 0;

      while (index < this.compagnie.results.length) {
        chunks.push(this.compagnie.results.slice(index, index + chunkSize));
        index += chunkSize;
      }

      return chunks;
    },
  },

  methods: {

    toggleVisibility() {
      this.importoVisibile = !this.importoVisibile;
    },
    // Request permission for browser notifications
    async requestNotificationPermission() {
      try {
        const permission = await Notification.requestPermission();

        if (permission === 'granted') {
          this.showNotification('Notifica di prova');
        } else {
          console.error('Permission for notifications was not granted');
        }
      } catch (error) {
        console.error('Error requesting notification permission:', error);
      }
    },

    // Show browser notification with provided message
    showNotification(message) {
      new Notification('Vue.js App', { body: message });
    },

    // Format date into readable format
    formatDate(date) {
      const options = { day: '2-digit', month: 'long', year: 'numeric' };
      return new Date(date).toLocaleDateString(undefined, options);
    },

    // Fetch companies
    async getCompagnie() {
      const endpoint = endpoints["compagnieList"];

      try {
        const response = await axios.get(endpoint);
        this.compagnie = response.data;
      } catch (error) {
        console.log(error);
      }
    },

    // Fetch expiring policies
    async getPolizzeInScadenza() {
      this.loading = true;
      const currentDate = new Date();
      const currentMonth = currentDate.getMonth() + 1;
      const currentYear = currentDate.getFullYear();

      if (this.scadenzaMese === null) {
        this.scadenzaMese = currentMonth;
      }

      if (this.scadenzaAnno === null) {
        this.scadenzaAnno = currentYear;
      }

      const endpoint = `${endpoints["polizzeScadenza"]}${this.scadenzaMese}/?anno=${this.scadenzaAnno}`;

      try {
        const response = await axios.get(endpoint);
        this.polizzeInScadenza = response.data;
      } catch (error) {
        console.log(error);
      }
      finally {
        this.loading = false;
      }
    },

    // Fetch policies expiring in a specific month
    async getPolizzeInMese(mese) {
      let endpoint = `${endpoints["polizzeScadenza"]}${this.scadenzaMese}/`;

      try {
        if (this.scadenzaAnno) {
          this.scadenzaAnno = anno;
          endpoint += `?anno=${this.scadenzaAnno}`;
        }
        this.polizzeInScadenza = response.data;
      } catch (error) {
        console.log(error);
      }
    },

    async getPortafoglio() {
      try {
        const endpoint = `${endpoints["portafoglio"]}`;
        const response = await axios.get(endpoint);
        this.portafoglio = response.data.portafoglio;
      } catch (error) {
        console.log(error);
      }
    },
  },

  created() {
    document.title = "AssicurAssistance";

    if (this.authStore.getUser) {
      this.getPolizzeInScadenza();
      this.getCompagnie();
      this.getPortafoglio();
    }
  },

  mounted() {
    if (!this.authStore.getUser) {
      this.$router.push({ name: 'login' });
    }

    const risultato = this.salutoPersonalizzato;
    document.getElementById("saluto-personalizzato").textContent = risultato;
  },
};

</script>


<style scooped>
.contorno_compangnie {
  border: 2px solid rgba(56, 222, 227, 0.628);
}

h3 {
  cursor: pointer;
}
</style>