<template>
  <div>

    <div class="container mt-4">
      <h1 class="text-center">Dettagli Polizza</h1>
      <!-- Card Cliente -->
      <div v-if="data.cliente != undefined">


        <router-link :to="{ name: 'cliente-view', params: { id: data.cliente.codice_fiscale } }" class="card-link">

          <div class="card shadow rounded mb-4">


            <div class="card-header bg-primary text-white">
              <h3 class="card-title">Cliente</h3>

            </div>



            <div class="card-body" v-if="hasCodiceFiscale">
              <div v-if="!editingModeCliente">

                <h4>Nome: {{ data.cliente.nome }}</h4>
                <h4>Cognome: {{ data.cliente.cognome }}</h4>
                <h4 v-if="data.cliente.codice_fiscale">Codice Fiscale: {{ data.cliente.codice_fiscale }}</h4>

                <div v-if="data.cliente.codice_fiscale !== data_veicolo.proprietario">
                  <h4>Proprietario del veicolo: No</h4>
                </div>
                <div v-else>
                  <h4>Proprietario del veicolo: Si</h4>
                  <h4 v-if="data_proprietario.indirizzo">Indirizzo: {{ data_proprietario.indirizzo }}</h4>
                  <h4 v-if="data_proprietario.telefono">Telefono: {{ data_proprietario.telefono }}</h4>
                  <h4 v-if="data_proprietario.email">Email: {{ data_proprietario.email }}</h4>
                  <h4 v-if="data_proprietario.citta">Indirizzo: {{ data_proprietario.citta }}</h4>
                  <h4 v-if="data_proprietario.data_nascita">Data di nascita: {{ data_proprietario.data_nascita }}</h4>

                </div>

              </div>


              <!-- Campi di modifica -->
              <div v-else>


                <div class="container">

                  <!-- NOME -->
                  <div>
                    <div class="input-group mb-3">
                      <span class="input-group-text" id="basic-addon1">Nome</span>
                      <input type="text" class="form-control" :value="this.editDataProprietario.nome" aria-label="nome"
                        aria-describedby="basic-addon1">
                    </div>

                    <!-- COGNOME -->
                    <div class="input-group mb-3">
                      <span class="input-group-text" id="basic-addon1">Cognome</span>
                      <input type="text" class="form-control" :value="this.editDataProprietario.cognome"
                        aria-label="nome" aria-describedby="basic-addon1">
                    </div>

                    <!-- CODICE FISCALE -->
                    <div class="input-group mb-3">
                      <span class="input-group-text" id="basic-addon1">Codice fiscale</span>
                      <input type="text" class="form-control" required :value="this.editDataProprietario.codice_fiscale"
                        aria-label="nome" aria-describedby="basic-addon1">
                    </div>

                    <!-- INDIRIZZO -->
                    <div class="input-group mb-3">
                      <span class="input-group-text" id="basic-addon1">Indirizzo</span>
                      <input type="text" class="form-control" required :value="this.editDataProprietario.indirizzo"
                        aria-label="nome" aria-describedby="basic-addon1">
                    </div>

                    <!-- TELEFONO -->

                    <div class="input-group mb-3">
                      <span class="input-group-text" id="basic-addon1">Telefono</span>
                      <input type="tel" class="form-control" required :value="this.editDataProprietario.telefono"
                        aria-label="nome" aria-describedby="basic-addon1">
                    </div>


                    <!-- EMAIL -->

                    <div class="input-group mb-3">
                      <span class="input-group-text">@</span>
                      <input type="text" class="form-control" :value="this.editDataProprietario.email"
                        aria-label="Server">
                    </div>

                    <!-- CITTA -->

                    <div class="input-group mb-3">
                      <span class="input-group-text" id="basic-addon1">Città</span>
                      <input type="text" class="form-control" required :value="this.editDataProprietario.citta"
                        aria-label="nome" aria-describedby="basic-addon1">
                    </div>

                    <!-- CAP -->

                    <div class="input-group mb-3">
                      <span class="input-group-text" id="basic-addon1">Cap</span>
                      <input type="text" class="form-control" required :value="this.editDataProprietario.cap"
                        aria-label="nome" aria-describedby="basic-addon1">
                    </div>

                    <!-- PROVINCIA -->

                    <div class="input-group mb-3">
                      <span class="input-group-text" id="basic-addon1">Provincia</span>
                      <input type="text" class="form-control" required :value="this.editDataProprietario.provincia"
                        aria-label="nome" aria-describedby="basic-addon1">
                    </div>

                    <!-- DATA DI NASCITA -->

                    <div class="input-group mb-3">
                      <span class="input-group-text" id="basic-addon1">Data di nascita</span>
                      <input type="date" class="form-control" required :value="this.editDataProprietario.data_nascita"
                        aria-label="nome" aria-describedby="basic-addon1">
                    </div>

                  </div>





                  <!-- BOTTONI SALVATAGGIO E ANNULLA -->
                  <div class="d-flex justify-content-end">
                    <button @click="saveChanges" type="button" class="btn btn-success m-3">Salva</button>
                    <button @click="cancelEdit(1)" type="button" class="btn btn-danger m-3">Annulla</button>
                  </div>

                </div>


              </div>



            </div>

          </div>

        </router-link>
      </div>

      <div>

        <router-link :to="{ name: 'cliente-view', params: { id: data_proprietario.codice_fiscale } }" class="card-link">

          <!-- Card Proprietario -->
          <div v-if="data.cliente != undefined && data.cliente.codice_fiscale !== data_veicolo.proprietario">
            <div class="card shadow rounded mb-4">
              <div class="card-header bg-info text-white">
                <h3 class="card-title">Proprietario del veicolo</h3>
              </div>
              <div class="card-body">
                <h4>Nome: {{ data_proprietario.nome }}</h4>
                <h4>Cognome: {{ data_proprietario.cognome }}</h4>
                <h4>Codice fiscale: {{ data_proprietario.codice_fiscale }}</h4>
                <h4>Indirizzo: {{ data_proprietario.indirizzo }}</h4>
                <h4>Telefono: {{ data_proprietario.telefono }}</h4>
                <h4>Email: {{ data_proprietario.email }}</h4>
                <h4>Data di nascita: {{ data_proprietario.data_nascita }}</h4>
              </div>
            </div>

          </div>

        </router-link>





      </div>




      <!-- Card Polizza -->
      <div class="card shadow rounded mb-4">
        <div class="card-header bg-success text-white">
          <h3 class="card-title">Polizza: {{ this.id }}</h3>
        </div>
        <div class="card-body">
          <!-- Campi di visualizzazione -->
          <div v-if="!editingModePolizza">
            <h4>Compagnia: {{ data.compagnia }}</h4>


            <div v-if="data.semestrale" class="d-inline-flex ">
              <h4>Semestrale:</h4>
              <svg fill="#000000" class="icon_semestrale" viewBox="0 0 14 14" role="img" focusable="false"
                aria-hidden="true" xmlns="http://www.w3.org/2000/svg">
                <g id="SVGRepo_bgCarrier" stroke-width="0"></g>
                <g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g>
                <g id="SVGRepo_iconCarrier">
                  <path fill="green"
                    d="M13 4.1974q0 .3097-.21677.5265L7.17806 10.329l-1.0529 1.0529q-.21677.2168-.52645.2168-.30968 0-.52645-.2168L4.01935 10.329 1.21677 7.5264Q1 7.3097 1 7t.21677-.5265l1.05291-1.0529q.21677-.2167.52645-.2167.30968 0 .52645.2167l2.27613 2.2839 5.07871-5.0864q.21677-.2168.52645-.2168.30968 0 .52645.2168l1.05291 1.0529Q13 3.8877 13 4.1974z">
                  </path>
                </g>
              </svg>
            </div>

            <div v-else class="d-inline-flex">
              <h4>Semestrale:</h4>
              <svg viewBox="0 0 25 25" class="icon_semestrale" version="1.1" xmlns="http://www.w3.org/2000/svg"
                xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:sketch="http://www.bohemiancoding.com/sketch/ns"
                fill="#000000">
                <g id="SVGRepo_bgCarrier" stroke-width="0"></g>
                <g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g>
                <g id="SVGRepo_iconCarrier">
                  <title>cross</title>
                  <desc>Created with Sketch Beta.</desc>
                  <defs> </defs>
                  <g id="Page-1" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd" sketch:type="MSPage">
                    <g id="Icon-Set-Filled" sketch:type="MSLayerGroup" transform="translate(-469.000000, -1041.000000)"
                      fill="#f90606">
                      <path
                        d="M487.148,1053.48 L492.813,1047.82 C494.376,1046.26 494.376,1043.72 492.813,1042.16 C491.248,1040.59 488.712,1040.59 487.148,1042.16 L481.484,1047.82 L475.82,1042.16 C474.257,1040.59 471.721,1040.59 470.156,1042.16 C468.593,1043.72 468.593,1046.26 470.156,1047.82 L475.82,1053.48 L470.156,1059.15 C468.593,1060.71 468.593,1063.25 470.156,1064.81 C471.721,1066.38 474.257,1066.38 475.82,1064.81 L481.484,1059.15 L487.148,1064.81 C488.712,1066.38 491.248,1066.38 492.813,1064.81 C494.376,1063.25 494.376,1060.71 492.813,1059.15 L487.148,1053.48"
                        id="cross" sketch:type="MSShapeGroup"> </path>
                    </g>
                  </g>
                </g>
              </svg>
            </div>

            <h4>Emissione polizza: {{ data.data_inizio }}</h4>
            <h4>Scadenza: {{ data.data_fine }}</h4>
            <div v-if="data.semestrale">
              <h4>Scadenza secondo rinnovo: {{ data.data_fine_due }}</h4>
            </div>




            <h4 v-if="data.note">Note: {{ data.note }}</h4>
            <h4 >Premio: {{ data.premio }} €</h4>


            <div v-if="data.documenti && data.documenti.length > 0">
              <h4>Documenti:</h4>
              <div>
                <ul>
                  <li v-for="(documento, index) in data.documenti" :key="index">
                    <a :href="documento.documento" target="_blank">
                      {{ documento.file.split("/").pop() }}
                    </a>
                  </li>
                </ul>
              </div>

              <svg @click="scaricaDocumenti" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"
                class="download_icon">
                <g id="SVGRepo_bgCarrier" stroke-width="0"></g>
                <g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g>
                <g id="SVGRepo_iconCarrier">
                  <path
                    d="M5.625 15C5.625 14.5858 5.28921 14.25 4.875 14.25C4.46079 14.25 4.125 14.5858 4.125 15H5.625ZM4.875 16H4.125H4.875ZM19.275 15C19.275 14.5858 18.9392 14.25 18.525 14.25C18.1108 14.25 17.775 14.5858 17.775 15H19.275ZM11.1086 15.5387C10.8539 15.8653 10.9121 16.3366 11.2387 16.5914C11.5653 16.8461 12.0366 16.7879 12.2914 16.4613L11.1086 15.5387ZM16.1914 11.4613C16.4461 11.1347 16.3879 10.6634 16.0613 10.4086C15.7347 10.1539 15.2634 10.2121 15.0086 10.5387L16.1914 11.4613ZM11.1086 16.4613C11.3634 16.7879 11.8347 16.8461 12.1613 16.5914C12.4879 16.3366 12.5461 15.8653 12.2914 15.5387L11.1086 16.4613ZM8.39138 10.5387C8.13662 10.2121 7.66533 10.1539 7.33873 10.4086C7.01212 10.6634 6.95387 11.1347 7.20862 11.4613L8.39138 10.5387ZM10.95 16C10.95 16.4142 11.2858 16.75 11.7 16.75C12.1142 16.75 12.45 16.4142 12.45 16H10.95ZM12.45 5C12.45 4.58579 12.1142 4.25 11.7 4.25C11.2858 4.25 10.95 4.58579 10.95 5H12.45ZM4.125 15V16H5.625V15H4.125ZM4.125 16C4.125 18.0531 5.75257 19.75 7.8 19.75V18.25C6.61657 18.25 5.625 17.2607 5.625 16H4.125ZM7.8 19.75H15.6V18.25H7.8V19.75ZM15.6 19.75C17.6474 19.75 19.275 18.0531 19.275 16H17.775C17.775 17.2607 16.7834 18.25 15.6 18.25V19.75ZM19.275 16V15H17.775V16H19.275ZM12.2914 16.4613L16.1914 11.4613L15.0086 10.5387L11.1086 15.5387L12.2914 16.4613ZM12.2914 15.5387L8.39138 10.5387L7.20862 11.4613L11.1086 16.4613L12.2914 15.5387ZM12.45 16V5H10.95V16H12.45Z"
                    fill="#000000"></path>
                </g>
              </svg>
            </div>
            <br>

            <button class="btn btn-primary mb-3" @click="toggleEditMenuPolizza">Modifica</button>
          </div>

          <!-- Campi di modifica -->
          <div v-else>


            <div class="container">

              <!-- COMPAGNIA -->
              <div class="input-group mb-3">
                <button  @input="onChangeCampo" class="btn btn-outline-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown"
                  @click="getListCompagnie" aria-expanded="false">Compagnia</button>
                <ul class="dropdown-menu">
                  <li v-for="(compagnia, index) in listaCompagnie.results" :key="index">
                    <a class="dropdown-item" href="#" @click="selezionaCompagnia(compagnia.nome)">{{ compagnia.nome
                      }}</a>
                  </li>
                </ul>
                <input type="text" class="form-control" aria-label="Text input with dropdown button"
                  :value="this.editData.compagnia" readonly @input="onChangeCampo">
              </div>


              <!-- SEMESTRALITA -->
              <div class="btn-group-vertical mt-3" role="group" aria-label="Vertical radio toggle button group">
                <input type="radio" class="btn-check" name="vbtn-radio" id="vbtn-radio1" autocomplete="off"
                  @input="onChangeCampo">
                <label class="btn btn-outline-danger" @click="setSemestralitaTrue()"
                  for="vbtn-radio1">Semestrale</label>
                <input type="radio" class="btn-check" name="vbtn-radio" id="vbtn-radio2" autocomplete="off" checked
                  @input="onChangeCampo">
                <label class="btn btn-outline-danger" @click="setSemestralitaFalse()" for="vbtn-radio2">Annuale</label>
              </div>


              <!-- DATA INIZIO -->
              <div>
                <div class="d-inline-flex p-2 mt-3 mb-3 ">
                  <h5>Data inizio:</h5>
                  <input type="date" v-model="editData.data_inizio" @input="onChangeCampo" />
                </div>
              </div>

              <!-- DATA FINE 1 -->
              <div>
                <div class="d-inline-flex p-2 mt-3 mb-3 ">
                  <h5>Data scadenza:</h5>
                  <input type="date" v-model="editData.data_fine" @input="onChangeCampo" />
                </div>
              </div>

              <!-- DATA FINE 2 -->
              <div v-if="this.editData.semestrale">
                <div class="d-inline-flex p-2 mt-3 mb-3 ">
                  <h5>Data scadenza secondo rinnovo:</h5>
                  <input type="date" v-model="editData.data_fine_due" @input="onChangeCampo" />
                </div>
              </div>

              <!-- NOTE -->

              <div class="input-group mb-3">
                <span class="input-group-text">Note</span>
                <textarea class="form-control" aria-label="With textarea" v-model="editData.note"
                  @input="onChangeCampo"></textarea>
              </div>

              <!-- PREMIO -->
              <div class="input-group mb-3">
                <span class="input-group-text">Premio</span>
                <input type="text" class="form-control" aria-label="Amount (to the nearest dollar)"
                  v-model="editData.premio" @input="onChangeCampo">
                <span class="input-group-text">€</span>
              </div>

              <!-- Modifica documenti -->
              <div v-if="this.data.documenti != undefined && this.data.documenti.length > 0">
                <h4>Documenti:</h4>
                <div>
                  <ul>
                    <li v-for="(documento, index) in this.data.documenti" :key="index">
                      <a :href="documento.documento" target="_blank">
                        {{ documento.file.split("/").pop() }}
                        <button class="btn btn-outline-danger" @click="deleteDocumento(documento.id)">Elimina</button>
                      </a>
                    </li>
                  </ul>

                </div>

                <button class="btn btn-primary" @click="scaricaDocumenti">
                  Scarica
                  <span>
                    <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="download_icon">
                      <g id="SVGRepo_bgCarrier" stroke-width="0"></g>
                      <g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g>
                      <g id="SVGRepo_iconCarrier">
                        <path
                          d="M5.625 15C5.625 14.5858 5.28921 14.25 4.875 14.25C4.46079 14.25 4.125 14.5858 4.125 15H5.625ZM4.875 16H4.125H4.875ZM19.275 15C19.275 14.5858 18.9392 14.25 18.525 14.25C18.1108 14.25 17.775 14.5858 17.775 15H19.275ZM11.1086 15.5387C10.8539 15.8653 10.9121 16.3366 11.2387 16.5914C11.5653 16.8461 12.0366 16.7879 12.2914 16.4613L11.1086 15.5387ZM16.1914 11.4613C16.4461 11.1347 16.3879 10.6634 16.0613 10.4086C15.7347 10.1539 15.2634 10.2121 15.0086 10.5387L16.1914 11.4613ZM11.1086 16.4613C11.3634 16.7879 11.8347 16.8461 12.1613 16.5914C12.4879 16.3366 12.5461 15.8653 12.2914 15.5387L11.1086 16.4613ZM8.39138 10.5387C8.13662 10.2121 7.66533 10.1539 7.33873 10.4086C7.01212 10.6634 6.95387 11.1347 7.20862 11.4613L8.39138 10.5387ZM10.95 16C10.95 16.4142 11.2858 16.75 11.7 16.75C12.1142 16.75 12.45 16.4142 12.45 16H10.95ZM12.45 5C12.45 4.58579 12.1142 4.25 11.7 4.25C11.2858 4.25 10.95 4.58579 10.95 5H12.45ZM4.125 15V16H5.625V15H4.125ZM4.125 16C4.125 18.0531 5.75257 19.75 7.8 19.75V18.25C6.61657 18.25 5.625 17.2607 5.625 16H4.125ZM7.8 19.75H15.6V18.25H7.8V19.75ZM15.6 19.75C17.6474 19.75 19.275 18.0531 19.275 16H17.775C17.775 17.2607 16.7834 18.25 15.6 18.25V19.75ZM19.275 16V15H17.775V16H19.275ZM12.2914 16.4613L16.1914 11.4613L15.0086 10.5387L11.1086 15.5387L12.2914 16.4613ZM12.2914 15.5387L8.39138 10.5387L7.20862 11.4613L11.1086 16.4613L12.2914 15.5387ZM12.45 16V5H10.95V16H12.45Z"
                          fill="#000000"></path>
                      </g>
                    </svg>
                  </span>
                </button>

              </div>

              <div>
                <br>
                <form id="uploadForm" @submit.prevent="uploadFiles">
                  <label for="fileInput">Seleziona i file:</label><br>
                  <input type="file" id="fileInput" name="files" multiple @change="caricaDocumento">
                  <button class="btn btn-outline-primary" type="submit">Carica File</button>
                </form>


              </div>


              <div class="d-flex justify-content-end">
                <button @click="saveChanges()" type="button" class="btn btn-success m-3"
                  :disabled="!modificheEffettuate">Salva</button>
                <button @click="cancelEdit(2)" type="button" class="btn btn-danger m-3">Annulla</button>
              </div>





            </div>
          </div>
          <!-- FINE CAMPO MODIFICA     -->


        </div>
      </div>






      <!-- Card Veicolo -->
      <div class="card shadow rounded mb-4">
        <div class="card-header bg-warning text-white">
          <h3 class="card-title">Veicolo</h3>
        </div>
        <div class="card-body">
          <h4>Targa: {{ data.veicolo }}</h4>
          <h4>Marca: {{ data_veicolo.marca }}</h4>
          <h4>Modello: {{ data_veicolo.modello }}</h4>
          <h4>Cilindrata: {{ data_veicolo.cilindrata }}</h4>
          <h4>Alimentazione: {{ data_veicolo.alimentazione }}</h4>
          <h4>Anno immatricolazione: {{ data_veicolo.anno_immatricolazione }}</h4>
          <!-- Altri dettagli del veicolo -->
        </div>
      </div>
    </div>




    <!-- elimina polizza con conferma -->


    <div class="d-flex justify-content-between">
      <button class="btn btn-info m-3" @click="generatePDF">Genera PDF</button>
      <button @click="deletePolizza" type="button" class="btn btn-danger m-3">Elimina Polizza</button>
    </div>



  </div>
</template>


<style scooped>
.icon {
  width: 24px;
  height: 24px;
  margin-left: 5px;
  margin-right: 5px;
}

.icon_avatar {
  width: 70px;
  height: 70px;
  margin-left: 5px;
  margin-right: 5px;
}

.card-link {
  font-weight: 600;
  color: #000;
  text-decoration: none;
}

.card-link:hover {
  color: #000;
}


.download_icon {
  width: 40px;
  height: 40px;
  margin-left: 6px;
  margin-right: 5px;
}

.download_icon:hover {
  transform: scale(1.10);
}
</style>




<script>
// Import necessary modules
import { axios } from "@/common/api.service.js";
import { endpoints } from "@/common/endpoints.js";
import router from "../router";
import { useAuthStore } from '@/stores/auth';
import 'jspdf-autotable'; // Import necessary libraries
import "vue3-toastify/dist/index.css"; // Import necessary styles
import { toast } from "vue3-toastify";
import jsPDF from 'jspdf';

export default {
  name: 'polizzaView',
  props: {
    id: {
      type: String,
      required: true
    }
  },

  setup() {
    // Use VueX store for authentication
    const authStore = useAuthStore();
    return { authStore };
  },

  data() {
    return {
      data: {}, // Data related to the policy
      data_veicolo: {}, // Data related to the vehicle
      data_proprietario: {}, // Data related to the owner of the vehicle
      data_cliente: {}, // Data related to the client
      editingModePolizza: false, // Flag for editing policy mode
      editingModeCliente: false, // Flag for editing client mode
      editData: {}, // Data for editing
      compagnieNomi: [], // Names of insurance companies
      listaCompagnie: [], // List of insurance companies
      listaClienti: [], // List of clients
      data_user: {}, // Data related to the user
      listaDocumenti: [], // List of documents
      modificheEffettuate: false, // Flag for changes made
    };
  },
  computed: {
    // Calculate data_fine_due by adding 6 months to data_fine
    data_fine_due_calcolata() {
      if (this.editData.data_fine) {
        const dataFine = new Date(this.editData.data_fine);
        dataFine.setMonth(dataFine.getMonth() + 6);
        return dataFine.toISOString().slice(0, 10);
      } else {
        return null;
      }
    }
  },
  watch: {
    // Automatically update data_fine_due when data_fine changes
    'editData.data_fine': function (newDate) {
      this.editData.data_fine_due = this.data_fine_due_calcolata;
    }
  },
  methods: {
    // Method to generate PDF document
    generatePDF() {
  const pdf = new jsPDF(); // Create new PDF document
  // Add title to the document
  pdf.setFontSize(24);
  pdf.text('AssicurAssistance', 105, 20, { align: 'center' });
  // Add header information
  pdf.setFontSize(12);
  pdf.text('Data: ' + new Date().toLocaleDateString(), 15, 30);
  pdf.text('Consulente: ' + this.authStore.authUser.user.nome + ' ' + this.authStore.authUser.user.cognome, 15, 35);

  // Spazio tra intestazione e dettagli veicolo
  let yPosition = 45;

  // Aggiungi dettagli veicolo in una tabella
  const vehicleData = [
    ['Targa', this.data_veicolo.targa],
    ['Marca', this.data_veicolo.marca],
    ['Modello', this.data_veicolo.modello],
    ['Cilindrata', this.data_veicolo.cilindrata],
    ['Alimentazione', this.data_veicolo.alimentazione],
    ['Anno immatricolazione', this.data_veicolo.anno_immatricolazione]
  ];

  pdf.autoTable({
    startY: yPosition,
    head: [['Dettagli veicolo', ' ']],
    body: vehicleData
  });

  // Spazio tra dettagli veicolo e dettagli cliente
  yPosition = pdf.autoTable.previous.finalY + 10;

  // Controlla se il cliente è anche il proprietario del veicolo
  const isOwner = this.data.cliente.codice_fiscale === this.data_veicolo.proprietario;

  if (!isOwner) {
    // Se il cliente non è il proprietario, aggiungi dettagli del proprietario in una tabella
    const proprietarioData = [
      ['Nome', this.data_proprietario.nome],
      ['Cognome', this.data_proprietario.cognome],
      ['Codice fiscale', this.data_proprietario.codice_fiscale],
      ['Indirizzo', this.data_proprietario.citta],
      ['Telefono', this.data_proprietario.telefono],
      ['Email', this.data_proprietario.email]
    ];

    pdf.autoTable({
      startY: yPosition,
      head: [['Dettagli Proprietario', ' ']],
      body: proprietarioData
    });

    // Aggiorna la posizione Y
    yPosition = pdf.autoTable.previous.finalY + 10;
  }

  // Aggiungi dettagli del cliente in una tabella
  let userData = [];
  if(isOwner){
    userData = [
    ['Nome', this.data.cliente.nome],
    ['Cognome', this.data.cliente.cognome],
    ['Codice fiscale', this.data.cliente.codice_fiscale],
    ['Indirizzo', this.data_proprietario.citta],
    ['Telefono', this.data_proprietario.telefono],
    ['Email', this.data_proprietario.email]
  ];
  }
  else{
    userData = [
      ['Nome', this.data.cliente.nome],
      ['Cognome', this.data.cliente.cognome],
      ['Codice fiscale', this.data.cliente.codice_fiscale],
    ];
  }

  pdf.autoTable({
    startY: yPosition,
    head: [['Dettagli cliente', ' ']],
    body: userData
  });

  // Spazio tra dettagli cliente e dettagli polizza
  yPosition = pdf.autoTable.previous.finalY + 10;

  // Aggiungi dettagli della polizza in una tabella
  const policyData = [
    ['Compagnia', this.data.compagnia],
    ['Data emissione', this.data.data_inizio],
    ['Data di scadenza', this.data.data_fine],
    ['Premio', this.data.premio]
  ];
  if (this.data.semestrale) {
    policyData.push(['Data fine secondo rinnovo', this.data.data_fine_due]);
  }
  policyData.push(['Note', this.editData.note], ['Premio', this.editData.premio]);

  pdf.autoTable({
    startY: yPosition,
    head: [['Dettagli polizza', ' ']],
    body: policyData
  });

  // Spazio tra dettagli polizza e documenti
  yPosition = pdf.autoTable.previous.finalY + 10;

  // aggiungi recepiti agenzia a pie di pagina

  // Salva il documento PDF
  if (this.data.cognome) {
    pdf.save(this.data.cognome + '.pdf');
  } else {
    pdf.save('polizza.pdf');
  }
},


    onChangeCampo() {
      this.modificheEffettuate = true;
    },

    handleFileChange(event) {
      this.fileInput = event.target;
    },

    caricaDocumento(event) {
      const nuoviDocumenti = Array.from(event.target.files).map(file => ({
        nome: file.name,
        file
      }));

      // Aggiungi i nuovi documenti alla lista esistente
      this.listaDocumenti = [...this.listaDocumenti, ...nuoviDocumenti];
    },

    rimuoviDocumento(index) {
      // Rimuovi il documento dalla lista in base all'indice
      this.listaDocumenti.splice(index, 1);
    },


    uploadFiles() {
      if (this.listaDocumenti.length === 0) {
        toast.error("Nessun documento caricato");
        return;
      }



      const formData = new FormData();


      if (this.listaDocumenti.length !== 0) {
        this.listaDocumenti.forEach((documento) => {
          formData.append('polizza', this.id);
          formData.append('file', documento.file);
        });
      }
      else {
        toast.error("Nessun documento caricato");
        return;
      }

      const endpoint = `${endpoints["AggiungiDocumento"]}${this.id}/`;

      axios.post(endpoint, formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      })
        .then(() => {
          toast.success("Documenti caricati con successo.");
          this.getPolizza();
        })
        .catch(error => {
          console.error('Errore durante il caricamento dei documenti:', error);
          toast.error("Si è verificato un errore durante il caricamento dei documenti.");
        });
    },

    deleteDocumento(id) {
      if (!confirm("Sei sicuro di voler eliminare il documento?")) {
        return;
      }
      this.data.documenti = this.data.documenti.filter((documento) => documento.id !== id);
      const endpoint = `${endpoints["EliminaDocumento"]}${this.id}/elimina_documento/${id}/`;
      try {
        axios.delete(endpoint);
        toast.info("Documento eliminato.");
        this.getPolizza();
      }
      catch (error) {
        console.log(error);
        toast.error("Si è verificato un errore durante l'eliminazione del documento.");
      }


    },


    // Funzioni per la modofica dei campi della polizza
    async toggleEditMenuPolizza() {
      this.editingModePolizza = !this.editingModePolizza;
      // Quando attivi la modalità di modifica, copia i dati originali in editData
      if (this.editingModePolizza) {
        this.editData = { ...this.data };
      }
    },
    async getListCompagnie() {
      const endpoint = `${endpoints["compagnieList"]}`;
      try {
        const response = await axios.get(endpoint);
        this.listaCompagnie = response.data;
      }
      catch (error) {
        console.log(error);
        toast.error(error.response.statusText);
      }
    },

    selezionaCompagnia(nomeCompagnia) {
      this.editData.compagnia = nomeCompagnia;
    },
    setSemestralitaTrue() {
      this.editData.semestrale = true;
    },
    setSemestralitaFalse() {
      this.editData.semestrale = false;
    },
    async getListClienti() {
      const endpoint = `${endpoints["clientiList"]}`;
      try {
        const response = await axios.get(endpoint);
        this.listaClienti = response.data;
      }
      catch (error) {
        console.log(error);
        toast.error(error.response.statusText);
      }
    },


    // Funzioni per la modofica dei campi della polizza
    async toggleEditMenuCliente() {
      this.editingModeCliente = !this.editingModeCliente;
      // Quando attivi la modalità di modifica, copia i dati originali in editData
      if (this.editingModeCliente) {
        this.editDataProprietario = { ...this.data_proprietario };
      }
    },
    //
    async getPolizza() {
      const endpoint = `${endpoints["polizzeDetail"]}${this.id}/`;

      try {
        const response = await axios.get(endpoint);
        this.data = response.data;

  
        await this.getVeicolo(this.data.veicolo);
      }
      catch (error) {
        console.log(error);
        toast.error(error.response.statusText);
      }
    },
    async getVeicolo(targa) {
      const endpoint = `${endpoints["veicoliDetail"]}${targa}/`;
      try {
        const response = await axios.get(endpoint);
        this.data_veicolo = response.data;
        await this.getProprietario(this.data_veicolo.proprietario);
      }
      catch (error) {
        console.log(error);
        toast.error(error.response.statusText);
      }
    },
    async getProprietario(codice_fiscale) {
      const endpoint = `${endpoints["clientiDetail"]}${codice_fiscale}/`;
      try {
        const response = await axios.get(endpoint);
        this.data_proprietario = response.data;
      }
      catch (error) {
        console.log(error);
        toast.error(error.response.statusText);
      }
    },

    async saveChanges() {
      this.modificheEffettuate = false;

      const endpoint = `${endpoints["polizzeDetail"]}${this.id}/`;
      try {
        this.editData.intestatario = this.data.cliente.codice_fiscale;
        await axios.put(endpoint, this.editData);
        this.data = { ...this.editData };
        this.editingModePolizza = false;

      }
      catch (error) {
        console.log(error);
        toast.error("Si è verificato un errore durante il salvataggio delle modifiche.");
      }
    },
    cancelEdit(card) {
      this.modificheEffettuate = false;
      // Annulla le modifiche e disattiva la modalità di modifica
      if (card == 1)
        this.editingModeCliente = false;
      else if (card == 2)
        this.editingModePolizza = false;
      else if (card == 3)
        this.editingModeVeicolo = false;
    },


    hasCodiceFiscale() {
      return !!this.data.cliente.codice_fiscale;
    },


    async deletePolizza() {
      // Conferma eliminazione
      if (!confirm("Sei sicuro di voler eliminare la polizza?")) {
        return;
      }
      const endpoint = `${endpoints["polizzeDetail"]}${this.id}/`;
      try {
        await axios.delete(endpoint);
        toast.success("Polizza eliminata con successo.");
        // Aggiorna il veicolo mettendo assicurato su false

        try {
          this.editData.intestatario = this.data.cliente.codice_fiscale;
          await axios.put(endpoint, this.editData);
          this.data = { ...this.editData };
          this.editingModePolizza = false;
        } catch (error) {
          console.log(error);
          toast.error("Si è verificato un errore durante il salvataggio delle modifiche.");
        }
      } catch (error) {
        console.log(error);
        toast.error("Si è verificato un errore durante l'eliminazione della polizza.");
      }
    },

    
    cancelEdit(card) {
      // Annulla le modifiche e disattiva la modalità di modifica
      if (card == 1)
        this.editingModeCliente = false;
      else if (card == 2)
        this.editingModePolizza = false;
      else if (card == 3)
        this.editingModeVeicolo = false;
    },


    hasCodiceFiscale() {
      return !!this.data.cliente.codice_fiscale;
    },

    async deletePolizza() {

      //conferma eliminaizione
      if (!confirm("Sei sicuro di voler eliminare la polizza?")) {
        return;
      }
      const endpoint = `${endpoints["polizzeDetail"]}${this.id}/`;
      try {
        await axios.delete(endpoint);
        toast.success("Polizza eliminata con successo.");
        //aggiorna il veicolo mettendo assicurato su false


        try {

          const endpointVeicolo = `${endpoints["veicoliDetail"]}${this.data_veicolo.targa}/`;
          const dataVeicolo = {
            targa: this.data_veicolo.targa,
            marca: this.data_veicolo.marca,
            modello: this.data_veicolo.modello,
            cilindrata: this.data_veicolo.cilindrata,
            alimentazione: this.data_veicolo.alimentazione,
            anno_immatricolazione: this.data_veicolo.anno_immatricolazione,
            proprietario: this.data_veicolo.proprietario,
            documenti: this.data_veicolo.documenti,
            assicurato: false,
          };

          toast.success("Veicolo aggiornato con successo.");
          await axios.put(endpointVeicolo, dataVeicolo);
        }
        catch (error) {
          console.log(error);
          toast.error("Si è verificato un errore durante il salvataggio delle modifiche.");
        }


        router.push({ name: 'home' });
      }
      catch (error) {
        console.log(error);
        toast.error("Si è verificato un errore durante l'eliminazione della polizza.");
      }
    },





    async scaricaDocumenti() {
      const endpoint = `${endpoints["DownloadDocumenti"]}${this.id}/`

      try {
        const response = await axios.get(endpoint, {
          responseType: 'arraybuffer',
        });

        const blob = new Blob([response.data]);
        const url = window.URL.createObjectURL(blob);

        const link = document.createElement('a');
        link.href = url;
        link.download = this.id + '_documento.zip'; // Specifica il nome del file da scaricare
        document.body.appendChild(link);

        link.click();

        document.body.removeChild(link);
        toast("Scarico i documenti...", {
          "theme": "auto",
          "type": "info",
          "dangerouslyHTMLString": true
        })
      } catch (error) {
        toast.error("Si è verificato un errore durante il download dei documenti.");
        console.error('Errore durante il download del documento:', error);
      }
    },

  },


  created() {
    this.getPolizza();
  },

  watch: {
    // Watch per l'ID della polizza
    id: {
      immediate: true,
      handler(newId, oldId) {
        if (newId !== oldId) {
          // Se l'ID della polizza è cambiato, ottieni i nuovi dati della polizza
          this.getPolizza();
        }
      }
    }
  },


  components: { router }
}
</script>