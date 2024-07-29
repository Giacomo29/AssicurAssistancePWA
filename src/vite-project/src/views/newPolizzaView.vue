<!-- View dedicata alla creazione delle polizze -->

<template>

    <div class="container mt-3 mb-3" v-show="this.newVeicolo">
        <h1 class="text-center text-warning"> Veicolo non esistente, aggiungi il
            veicolo prima di assicurarlo!</h1>
        <button type="button"
            class="btn btn-secondary btn-lg position-absolute top-50 start-50 translate-middle">Aggiungi
            Veicolo</button>
    </div>



    <div v-show="this.newVeicolo == false">
        <h1 class="text-center">Assicura Veicolo</h1>
        <div class="container">


            <!-- ID_POLIZZA -->



            <div class="input-group mb-3">
                <span class="input-group-text" id="basic-addon1">N. Polizza</span>
                <input type="text" class="form-control" aria-label="Username" aria-describedby="basic-addon1"
                    v-model="this.data_polizza.id_polizza">
            </div>



            <!-- TARGA -->
            <div class="input-group mb-3">
                <button class="btn btn-outline-secondary dropdown-toggle" @click="getVeicoli" type="button"
                    data-bs-toggle="dropdown" aria-expanded="false">Targa</button>
                <ul class="dropdown-menu">
                    <template v-if="veicoliScoperti.count === 0">
                        <h4 class="dropdown-header text-center text-warning">Nessun veicolo da assicurare</h4>
                    </template>
                    <template v-else>
                        <li v-for="(veicolo, index) in veicoliScoperti.results" :key="index">
                            <a class="dropdown-item" @click="selezionaVeicolo(veicolo)" href="#"> {{ veicolo.targa
                                }}</a>
                        </li>
                    </template>
                </ul>
                <input v-if="veicoliScoperti.count !== 0" type="text" class="form-control"
                    aria-label="Text input with dropdown button" v-model="data_polizza.veicolo">
            </div>

            <!-- CLIENTE -->


    

            <DropdownFiltrabile @click="this.getClienti" :loading="loading" :clienti="clienti && clienti ? clienti : []"
                v-model="data_polizza.intestatario" @clienteSelezionato="selezionaCliente" />




            <!-- COMPAGNIA -->


            <div class="input-group mb-3">
                <button class="btn btn-outline-secondary dropdown-toggle" @click="this.getCompagnia" type="button"
                    data-bs-toggle="dropdown" aria-expanded="false">Compagnia</button>
                <ul class="dropdown-menu">
                    <div v-if="compagnie.count === 0">
                        <h4 class="dropdown-header text-center text-warning">Aggiungi prima una compagnia</h4>
                    </div>
                    <div v-else>
                        <li v-for="(compagnia, index) in this.compagnie.results" :key="index">
                            <a class="dropdown-item" @click="selezionaCompagnia(compagnia)" href="#">{{ compagnia.nome
                                }}</a>
                        </li>
                    </div>
                </ul>
                <input type="text" class="form-control" aria-label="Text input with dropdown button" readonly
                    v-model="this.data_polizza.compagnia">
            </div>

            <!-- PREMIO -->
            <div class="input-group mb-3">
                <span class="input-group-text">Premio</span>
                <input type="text" class="form-control" aria-label="Amount (to the nearest dollar)"
                    v-model="this.data_polizza.premio">
                <span class="input-group-text">€</span>
            </div>




            <!-- NOTE -->

            <div class="form-floating">
                <textarea class="form-control" placeholder="Leave a comment here" v-model=this.data_polizza.note
                    id="floatingTextarea2" style="height: 100px"></textarea>
                <label for="floatingTextarea2">Prendi nota</label>
            </div>



            <!-- SEMESTRALITA -->
            <div class="btn-group-vertical mt-3" role="group" aria-label="Vertical radio toggle button group">
                <input type="radio" class="btn-check" name="vbtn-radio" id="vbtn-radio1" autocomplete="off">
                <label class="btn btn-outline-danger" @click="setSemestralitaTrue()"
                    for="vbtn-radio1">Semestrale</label>
                <input type="radio" class="btn-check" name="vbtn-radio" id="vbtn-radio2" autocomplete="off" checked>
                <label class="btn btn-outline-danger" @click="setSemestralitaFalse()" for="vbtn-radio2">Annuale</label>
            </div>



            <!-- DATA INIZIO -->
            <div>
                <div class="d-inline-flex p-2 mt-3 mb-3 ">
                    <h5>Data inizio:</h5>
                    <input type="date" v-model="this.data_polizza.data_inizio" />
                </div>
            </div>

            <!-- DATA FINE 1 -->
            <div>
                <div class="d-inline-flex p-2 mt-3 mb-3 ">
                    <h5>Data scadenza:</h5>
                    <input type="date" v-model="this.data_polizza.data_fine" />
                </div>
            </div>

            <!-- DATA FINE 2 -->
            <div v-show="this.data_polizza.semestrale">
                <div class="d-inline-flex p-2 mt-3 mb-3 ">
                    <h5>Data scadenza secondo rinnovo:</h5>
                    <input type="date" v-model="this.data_polizza.data_fine_due" />
                </div>
            </div>

            <!-- CARICA FILE -->
            <div>
                <input type="file" @change="caricaDocumento" multiple />
                <ul>
                    <li v-for="(documento, index) in listaDocumenti" :key="index">
                        {{ documento.nome }}
                        <button @click="rimuoviDocumento(index)">Rimuovi</button>
                    </li>
                </ul>
            </div>


            <div class="d-flex justify-content-end">
                <button @click="this.creaPolizza" type="button" class="btn btn-success m-3">Crea</button>
            </div>



        </div>
    </div>
</template>



<script>

import { axios } from "@/common/api.service.js";
import { endpoints } from "@/common/endpoints.js";
import { toast } from "vue3-toastify";
import "vue3-toastify/dist/index.css";



import DropdownFiltrabile from "@/components/DropdownFiltrabile.vue";

export default {


    components: {
        DropdownFiltrabile
    },

    name: 'newPolizzaView',
    props: {
        id: {
            type: String,
            required: true
        }
    },
    data() {
        return {
            data_polizza: {},
            veicoliScoperti: [],
            compagnie: [],
            clienti: [],
            veicolo: {},
            newVeicolo: false,
            listaDocumenti: [],
            loading: false
        };
    },
    methods: {

        handleClienteSelezionato(cliente) {
            console.log('Cliente selezionato:', cliente);
            // Eventuali azioni aggiuntive da eseguire quando un cliente viene selezionato
        },

        // Handle file change event
        handleFileChange(event) {
            this.fileInput = event.target;
        },
        // Format date function
        formattaData(date) {
            if (!date) return "";
            date = date instanceof Date ? date : new Date(date);
            const year = date.getFullYear();
            const month = (date.getMonth() + 1).toString().padStart(2, '0');
            const day = date.getDate().toString().padStart(2, '0');
            return `${year}-${month}-${day}`;
        },
        // Load documents function
        caricaDocumento(event) {
            const nuoviDocumenti = Array.from(event.target.files).map(file => ({
                nome: file.name,
                file
            }));
            this.listaDocumenti = [...this.listaDocumenti, ...nuoviDocumenti];
        },
        // Remove document function
        rimuoviDocumento(index) {
            this.listaDocumenti.splice(index, 1);
        },
        // Get uncovered vehicles
        async getVeicoli() {
            try {
                const response = await axios.get(endpoints["veicoliNonAssicurati"]);
                this.veicoliScoperti = response.data;
            } catch (error) {
                console.log(error);
                this.newVeicolo = true;
            }
        },
        // Get clients in all page
        async getClienti() {
            this.loading = true;
            try {
                var response = await axios.get(endpoints["clientiList"]);
                const clientiData = response.data.results; // Prendi solo i dati dei clienti dall'oggetto di risposta
                this.clienti = clientiData;

                // Controlla se ci sono altre pagine di risultati
                while (response.data.next) {
                    response = await axios.get(response.data.next);
                    const nextPageData = response.data.results; // Prendi i dati della pagina successiva
                    this.clienti = this.clienti.concat(nextPageData); // Concatena i dati della pagina successiva a quelli esistenti
                }
                this.loading = false;

            } catch (error) {
                console.log(error);
                this.handleError(error, "Errore durante il caricamento dei clienti");
            }

        },
        // Get insurance companies
        async getCompagnia() {
            try {
                const response = await axios.get(endpoints["compagnieList"]);
                this.compagnie = response.data;
            } catch (error) {
                this.handleError(error, "Errore durante il caricamento delle compagnie assicurative");
            }
        },
        // Create insurance 
        async creaPolizza() {
            const formData = new FormData();
            this.data_polizza.id_polizza = this.data_polizza.id_polizza.replace(/\//g, "-");
            formData.append('id_polizza', this.data_polizza.id_polizza);
            formData.append('data_inizio', this.data_polizza.data_inizio);
            formData.append('data_fine', this.data_polizza.data_fine);
            formData.append('veicolo', this.data_polizza.veicolo);
            formData.append('intestatario', this.data_polizza.intestatario);
            formData.append('compagnia', this.data_polizza.compagnia);
            formData.append('premio', this.data_polizza.premio);
            if (this.listaDocumenti.length !== 0) {
                this.listaDocumenti.forEach((documento) => {
                    formData.append('uploaded_documents', documento.file);
                });
                toast.info("Caricamento documenti effettuato");
            }
            try {
                const response = await axios.post(endpoints["polizzeList"], formData, {
                    headers: {
                        'Content-Type': 'multipart/form-data',
                    },
                });
                this.data_polizza = response.data;
                this.updateAssciurazione(this.data_polizza.veicolo);
                toast.success("Polizza creata con successo");
                this.data_polizza = {};
                this.listaDocumenti = [];
            } catch (error) {
                this.handleError(error, "Errore durante la creazione della polizza");
            }
        },
        // Update insurance
        async updateAssciurazione(targa) {
            const endpoint = `${endpoints["veicoliDetail"]}${targa}/`;
            try {
                const response = await axios.get(endpoint);
                this.veicoloUpdate = response.data;
                this.veicoloUpdate.assicurato = true;
                try {
                    const response2 = await axios.put(endpoint, this.veicoloUpdate);
                    toast("Veicolo assicurato!", {
                        "theme": "auto",
                        "type": "success",
                        "dangerouslyHTMLString": true
                    })
                } catch (error) {
                    this.handleError(error, "Errore");
                }
            } catch (error) {
                this.handleError(error, "Errore");
            }
        },
        // Set semestralita true
        setSemestralitaTrue() {
            this.data_polizza.semestrale = true;
        },
        // Set semestralita false
        setSemestralitaFalse() {
            this.data_polizza.semestrale = false;
        },
        // Select client
        selezionaCliente(cliente) {
            this.data_polizza.intestatario = `${cliente.codice_fiscale}`
            console.log(this.data_polizza.intestatario);
        },
        // Select vehicle
        selezionaVeicolo(veicolo) {
            this.data_polizza.veicolo = `${veicolo.targa}`
        },
        // Select insurance company
        selezionaCompagnia(compagnia) {
            this.data_polizza.compagnia = `${compagnia.nome}`
        },
        // Get vehicle by plate number
        async getVeicolobyTarga(targa) {
            if (!targa) return;
            const endpoint = `${endpoints["veicoliDetail"]}${targa}/`;
            try {
                const response = await axios.get(endpoint);
                this.veicolo = response.data;
            } catch (error) {
                console.log(error);
                this.newVeicolo = true;
            }
        },
        // Handle errors
        handleError(error, message) {
            if (error.response && error.response.data) {
                const errori = error.response.data;
                Object.keys(errori).forEach((campo) => {
                    errori[campo].forEach((messaggio) => {
                        toast.error(`${campo}: ${messaggio}`);
                    });
                });
            } else {
                toast.error(message);
            }
        },
    },
    created() {
        this.getVeicolobyTarga(this.id);
    },
    mounted() {
        const targaFromURL = this.id;
        if (targaFromURL) {
            this.data_polizza.veicolo = targaFromURL;
        }
    },
}
</script>
