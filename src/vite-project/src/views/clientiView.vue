<template>
  <div class="container mt-4">

    <div class="d-flex justify-content-center">
      <h2>Cerca Clienti</h2>

    </div>


    <div class="d-flex justify-content-center">
      <router-link :to="{ name: 'nuovo-cliente-view' }" class="btn btn-success m-3">Crea nuovo cliente</router-link>
    </div>

    <input type="text" v-model="inputValue" @input="searchByQuery()" class="form-control mt-4 mb-4"
      placeholder="Il cognome del cliente da ricercare o la targa" aria-label="Cerca Cliente"
      aria-describedby="button-addon1" />
    <div v-for="cliente in clienti.results" :key="cliente.codice_fiscale">

      <div class="card shadow rounded mb-4">
        <div class="card-body">
          <h4 class="card-title text-primary mb-3">
            Nome: <span class="text-black">{{ cliente.nome }}</span>
          </h4>
          <h4 class="card-title text-primary mb-3">
            Cognome: <span class="text-black">{{ cliente.cognome }}</span>
          </h4>
          <h4 class="card-title text-primary mb-3">
            Codice Fiscale: <span class="text-black">{{ cliente.codice_fiscale }}</span>

            <div>
              <div v-if="cliente.polizze != null && cliente.polizze.length > 0">
                <h4 class="card-title text-success mt-4">Polizze:</h4>
                <div v-for="polizza in cliente.polizze" :key="polizza.id_polizza">
                  <router-link :to="{ name: 'polizza-view', params: { id: polizza.id_polizza } }">
                    <div class="card bg-light mb-3">
                      <div class="card-body">
                        <h5 class="card-title text-primary mb-2">
                          Targa: <span class="text-black">{{ polizza.veicolo }} </span><br>
                          Compagnia: <span class="text-black">{{ polizza.compagnia }}</span>
                        </h5>
                      </div>
                    </div>
                  </router-link>

                
              
            </div>

        </div>

      </div>

      </h4>



      <div v-if="cliente.mostraDettagli">
        <button class="btn btn-primary mb-3" @click="cliente.mostraDettagli = !cliente.mostraDettagli">
          Mostra meno
        </button>
      </div>
      <div v-else>
        <button class="btn btn-primary mb-3" @click="cliente.mostraDettagli = !cliente.mostraDettagli">
          Mostra altro
        </button>
      </div>
      <div v-if="cliente.mostraDettagli">
        <h4 class="card-title text-primary mb-3">
          Email: <span class="text-black">{{ cliente.email }}</span>
        </h4>
        <h4 class="card-title text-primary mb-3">
          Telefono: <span class="text-black">{{ cliente.telefono }}</span>
        </h4>
        <h4 class="card-title text-primary mb-3">
          Indirizzo: <span class="text-black">{{ cliente.indirizzo }}</span>
        </h4>
        <h4 class="card-title text-primary mb-3">
          Città: <span class="text-black">{{ cliente.citta }}</span>
        </h4>
        <h4 class="card-title text-primary mb-3">
          CAP: <span class="text-black">{{ cliente.cap }}</span>
        </h4>
        <h4 class="card-title text-primary mb-3">
          Provincia: <span class="text-black">{{ cliente.provincia }}</span>
        </h4>
        <h4 class="card-title text-primary mb-3">
          Data di nascita:
          <span class="text-black">{{ cliente.data_nascita }}</span>
        </h4>

        <div>
          <router-link :to="{ name: 'cliente-view', params: { id: cliente.codice_fiscale } }">
            <button class="btn btn-primary mb-3">Dettagli</button>
          </router-link>
        </div>

        <h4 v-if="cliente.veicoli.length > 0" class="card-title text-success mt-4">Veicoli:</h4>
        <div v-for="veicolo in cliente.veicoli" :key="veicolo.targa">
          <div class="card bg-light mb-3">
            <div class="card-body">
              <h5 class="card-title text-primary mb-2">
                Targa: <span class="text-black">{{ veicolo.targa }}</span>
              </h5>
              <h5 class="card-title text-primary mb-2">
                Marca: <span class="text-black">{{ veicolo.marca }}</span>
              </h5>
              <h5 class="card-title text-primary mb-2">
                Modello:
                <span class="text-black">{{ veicolo.modello }}</span>
              </h5>
              <h5 class="card-title text-primary mb-2">
                Cilindrata:
                <span class="text-black">{{ veicolo.cilindrata }}</span>
              </h5>

              <h5 class="card-title text-primary mb-2">
                Alimentazione:
                <span class="text-black">{{ veicolo.alimentazione }}</span>
              </h5>
              <h5 class="card-title text-primary mb-2">
                Anno di immatricolazione:
                <span class="text-black">{{
        veicolo.anno_immatricolazione
      }}


                  <div v-if="veicolo.assicurato == false">

                    <h5 class="card-title text-danger mt-2">Veicolo non assicurato</h5>
                    <router-link :to="{ name: 'nuova-polizza-view', params: { id: veicolo.targa } }"
                      class="btn btn-warning m-3">Assicura</router-link>
                  </div>

                  <div v-else>
                    <button type="button" @click="this.apriPolizza(veicolo.targa)" class="btn btn-info">Apri
                      polizza</button>

                  </div>




                </span>
              </h5>
            </div>
          </div>
        </div>
      </div>
      <div class="position-relative">
        <svg viewBox="0 0 24 24" fill="none" @click="deleteCliente(cliente.codice_fiscale)" class="icon_bin"
          xmlns="http://www.w3.org/2000/svg">
          <g id="SVGRepo_bgCarrier" stroke-width="0"></g>
          <g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g>
          <g id="SVGRepo_iconCarrier">
            <path
              d="M1.5 3.75C1.08579 3.75 0.75 4.08579 0.75 4.5C0.75 4.91421 1.08579 5.25 1.5 5.25V3.75ZM22.5 5.25C22.9142 5.25 23.25 4.91421 23.25 4.5C23.25 4.08579 22.9142 3.75 22.5 3.75V5.25ZM1.5 5.25H22.5V3.75H1.5V5.25Z"
              fill="#dd6969"></path>
            <path
              d="M9.75 1.5V0.75V1.5ZM8.25 3H7.5H8.25ZM7.5 4.5C7.5 4.91421 7.83579 5.25 8.25 5.25C8.66421 5.25 9 4.91421 9 4.5H7.5ZM15 4.5C15 4.91421 15.3358 5.25 15.75 5.25C16.1642 5.25 16.5 4.91421 16.5 4.5H15ZM15.75 3H16.5H15.75ZM14.25 0.75H9.75V2.25H14.25V0.75ZM9.75 0.75C9.15326 0.75 8.58097 0.987053 8.15901 1.40901L9.21967 2.46967C9.36032 2.32902 9.55109 2.25 9.75 2.25V0.75ZM8.15901 1.40901C7.73705 1.83097 7.5 2.40326 7.5 3H9C9 2.80109 9.07902 2.61032 9.21967 2.46967L8.15901 1.40901ZM7.5 3V4.5H9V3H7.5ZM16.5 4.5V3H15V4.5H16.5ZM16.5 3C16.5 2.40326 16.2629 1.83097 15.841 1.40901L14.7803 2.46967C14.921 2.61032 15 2.80109 15 3H16.5ZM15.841 1.40901C15.419 0.987053 14.8467 0.75 14.25 0.75V2.25C14.4489 2.25 14.6397 2.32902 14.7803 2.46967L15.841 1.40901Z"
              fill="#dd6969"></path>
            <path
              d="M9 17.25C9 17.6642 9.33579 18 9.75 18C10.1642 18 10.5 17.6642 10.5 17.25H9ZM10.5 9.75C10.5 9.33579 10.1642 9 9.75 9C9.33579 9 9 9.33579 9 9.75H10.5ZM10.5 17.25V9.75H9V17.25H10.5Z"
              fill="#dd6969"></path>
            <path
              d="M13.5 17.25C13.5 17.6642 13.8358 18 14.25 18C14.6642 18 15 17.6642 15 17.25H13.5ZM15 9.75C15 9.33579 14.6642 9 14.25 9C13.8358 9 13.5 9.33579 13.5 9.75H15ZM15 17.25V9.75H13.5V17.25H15Z"
              fill="#dd6969"></path>
            <path
              d="M18.865 21.124L18.1176 21.0617L18.1176 21.062L18.865 21.124ZM17.37 22.5L17.3701 21.75H17.37V22.5ZM6.631 22.5V21.75H6.63093L6.631 22.5ZM5.136 21.124L5.88343 21.062L5.88341 21.0617L5.136 21.124ZM4.49741 4.43769C4.46299 4.0249 4.10047 3.71818 3.68769 3.75259C3.2749 3.78701 2.96818 4.14953 3.00259 4.56231L4.49741 4.43769ZM20.9974 4.56227C21.0318 4.14949 20.7251 3.78698 20.3123 3.75259C19.8995 3.7182 19.537 4.02495 19.5026 4.43773L20.9974 4.56227ZM18.1176 21.062C18.102 21.2495 18.0165 21.4244 17.878 21.5518L18.8939 22.6555C19.3093 22.2732 19.5658 21.7486 19.6124 21.186L18.1176 21.062ZM17.878 21.5518C17.7396 21.6793 17.5583 21.75 17.3701 21.75L17.3699 23.25C17.9345 23.25 18.4785 23.0379 18.8939 22.6555L17.878 21.5518ZM17.37 21.75H6.631V23.25H17.37V21.75ZM6.63093 21.75C6.44274 21.75 6.26142 21.6793 6.12295 21.5518L5.10713 22.6555C5.52253 23.0379 6.06649 23.25 6.63107 23.25L6.63093 21.75ZM6.12295 21.5518C5.98449 21.4244 5.89899 21.2495 5.88343 21.062L4.38857 21.186C4.43524 21.7486 4.69172 22.2732 5.10713 22.6555L6.12295 21.5518ZM5.88341 21.0617L4.49741 4.43769L3.00259 4.56231L4.38859 21.1863L5.88341 21.0617ZM19.5026 4.43773L18.1176 21.0617L19.6124 21.1863L20.9974 4.56227L19.5026 4.43773Z"
              fill="#dd6969"></path>
          </g>
        </svg>
      </div>
    </div>
  </div>

  </div>
  </div>
</template>







<script>
import { axios } from "@/common/api.service.js";
import { endpoints } from "@/common/endpoints.js";
import { toast } from "vue3-toastify";
import "vue3-toastify/dist/index.css";

export default {
  name: "clientiView",
  props: {
    nome: {
      type: String,
    },
  },
  data() {
    return {
      clienti: [],
      inputValue: "",
      test: [],
      veicoliScoperti: [],
    };
  },

  methods: {
    // Method to delete a client
    async deleteCliente(codice_fiscale) {
      // Confirmation dialog
      const conferma = window.confirm("Sei sicuro di voler eliminare questo cliente? Eliminando il cliente verranno eliminati anche tutti i suoi veicoli.");
      if (!conferma) {
        return;
      }
      // Delete request
      const endpoint = `${endpoints["clientiDetail"]}${codice_fiscale}/`;
      try {
        await axios.delete(endpoint);
        this.getClienti();
        // Show toast notification
        toast("Cliente eliminato", {
          "theme": "auto",
          "type": "info",
          "dangerouslyHTMLString": true
        })
      } catch (error) {
        console.log(error);
      }
    },

    // Method to search for clients by fiscal code
    async cercaPerCF(codice_fiscale) {

      // Search endpoint
      const endpoint = `${endpoints["polizzeCodiceFiscale"]}${codice_fiscale}/`;

      try {
        const response = await axios.get(endpoint);
        return response.data.results;
      } catch (error) {
        console.log(error);
      }
    },

    // Method to open a policy details
    async apriPolizza(targa) {
      // Get policy ID by vehicle registration number
      const polizza_id = await this.getPolizzaIdByTarga(targa);
      this.$router.push({ name: "polizza-view", params: { id: polizza_id } });
    },

    // Method to get clients by last name
    async getClienteByCognome(cognome) {
      const endpoint = `${endpoints["clientiCognome"]}${cognome}/`;
      try {
        const response = await axios.get(endpoint);
        this.clienti = response.data;
        // Iterate through clients and get associated policies
        for (const cliente of this.clienti.results) {
          for (const veicolo of cliente.veicoli) {
            const polizzaId = await this.getPolizzaIdByTarga(veicolo.targa);
            veicolo.id_polizza = polizzaId;
          }
        }
      } catch (error) {
        console.log(error);
      }
    },

    // Method to search for clients by last name or vehicle registration number
    searchByQuery() {
      if (this.inputValue === "") return;
      var tmp = this.inputValue.toUpperCase();
      const isItalianTarga = /^[A-Z]{2}\d{3}[A-Z]{2}$/.test(tmp);

      if (isItalianTarga) {
        this.getClienteByTarga(tmp);
      } else {
        this.getClienteByCognome(tmp);
      }
    },

    // Method to get clients by vehicle registration number
    async getClienteByTarga(targa) {
      const endpoint = `${endpoints["clientiTarga"]}${targa}/`;
      try {
        const response = await axios.get(endpoint);
        this.clienti = response.data;
        // Iterate through clients and get associated policies
        for (const cliente of this.clienti.results) {
          for (const veicolo of cliente.veicoli) {
            const polizzaId = await this.getPolizzaIdByTarga(veicolo.targa);
            veicolo.id_polizza = polizzaId;
          }
        }
      } catch (error) {
        console.log(error);
      }
    },

    // Method to get all clients
    async getClienti() {
      const endpoint = `${endpoints["clientiList"]}`;
      try {
        const response = await axios.get(endpoint);
        this.clienti = response.data;
        // Iterate through clients and get associated policies
        for (const cliente of this.clienti.results) {
          const polizze = await this.cercaPerCF(cliente.codice_fiscale);
          cliente.polizze = polizze;
          for (const veicolo of cliente.veicoli) {
            const polizzaId = await this.getPolizzaIdByTarga(veicolo.targa);
            veicolo.id_polizza = polizzaId;
          }
        }
      } catch (error) {
        console.log(error);
        alert(error.response.statusText);
      }
    },

    // Method to get policy ID by vehicle registration number
    async getPolizzaIdByTarga(targa) {
      const endpoint = `${endpoints["polizzeTarga"]}${targa}/`;
      try {
        const response = await axios.get(endpoint);
        const polizza = response.data;
        if (polizza.results.length > 0) {
          return polizza.results[0].id_polizza;
        } else {
          return null; // If policy not found, return null or a default value
        }
      } catch (error) {
        console.log(error);
        alert(error.response.statusText);
        return null; // In case of error, return null or a default value
      }
    },
  },

  created() {
    this.getClienti();
  },
};
</script>


<style>
.card {
  background-color: #fff;
  border: 1px solid #ccc;
  border-radius: 0.5rem;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.card-body {
  padding: 1.5rem;
}

.card-title {
  font-size: 1.2rem;
  font-weight: bold;
}

.text-primary {
  color: #000;
}

.text-success {
  color: #28a745;
}

.text-black {
  color: #000;
}

.bg-light {
  background-color: #f8f9fa;
}


.icon_bin {
  width: 40px;
  height: 40px;
  margin-left: 5px;
  margin-right: 5px;
}

.icon_bin:hover {
  transform: scale(1.2);
}
</style>