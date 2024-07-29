<template>
    <h1 class="text-center">Aggiungi un nuovo cliente</h1>
    <div class="container mt-3 mb-3">

        <ul class="nav nav-tabs" id="myTab" role="tablist">
            <li class="nav-item" role="presentation">
                <button class="nav-link active" id="home-tab" data-bs-toggle="tab" data-bs-target="#cliente-tab-pane"
                    type="button" role="tab" aria-controls="home-tab-pane" aria-selected="true">Cliente</button>
            </li>
            <li class="nav-item" role="presentation">
                <button class="nav-link" id="veicolo-tab" data-bs-toggle="tab" data-bs-target="#veicolo-tab-pane"
                    type="button" role="tab" aria-controls="veicolo-tab-pane" aria-selected="false">Veicolo</button>
            </li>
        </ul>
        <div class="tab-content" id="myTabContent">
            <div class="tab-pane fade show active" id="cliente-tab-pane" role="tabpanel" aria-labelledby="cliente-tab"
                tabindex="0">


                <!-- NOME -->
                <div class="input-group mb-3 mt-3">
                    <span class="input-group-text" id="basic-addon1">Nome</span>
                    <input type="text" class="form-control" aria-label="nome" aria-describedby="basic-addon1"
                        v-model="this.data_cliente.nome" required>
                </div>

                <!-- COGNOME -->
                <div class="input-group mb-3 mt-3">
                    <span class="input-group-text" id="basic-addon1">Cognome</span>
                    <input type="text" class="form-control" aria-label="cognome" aria-describedby="basic-addon1"
                        v-model="this.data_cliente.cognome" required>
                </div>

                <!-- DATA DI NASCITA -->
                <div class="input-group mb-3 mt-3">
                    <span class="input-group-text" id="basic-addon1">Data di nascita</span>
                    <input type="date" class="form-control" aria-label="data di nascita" aria-describedby="basic-addon1"
                        v-model="this.data_cliente.data_nascita">
                </div>

                <!-- RESIDENZA -->

                <div class="input-group mb-3 mt-3">
                    <span class="input-group-text" id="basic-addon1">Residenza</span>
                    <input type="text" class="form-control" aria-label="luogo di nascita"
                        aria-describedby="basic-addon1" v-model="this.data_cliente.citta">
                </div>


                <!-- PROVINCIA -->

                <div class="input-group mb-3 mt-3">
                    <span class="input-group-text" id="basic-addon1">Provincia</span>
                    <input type="text" class="form-control" aria-label="provincia" aria-describedby="basic-addon1"
                        v-model="this.data_cliente.provincia">

                </div>

                <!-- CODICE FISCALE -->

                <div class="input-group mb-3 mt-3">
                    <span class="input-group-text" id="basic-addon1">Codice fiscale</span>
                    <input type="text" class="form-control" aria-label="codice fiscale" aria-describedby="basic-addon1"
                        v-model="this.data_cliente.codice_fiscale" required>

                </div>

                <!-- TELEFONO -->

                <div class="input-group mb-3 mt-3">
                    <span class="input-group-text" id="basic-addon1">Telefono</span>
                    <input type="text" class="form-control" aria-label="telefono" aria-describedby="basic-addon1"
                        v-model="this.data_cliente.telefono">
                </div>


                <!-- EMAIL -->

                <div class="input-group mb-3 mt-3">
                    <span class="input-group-text" id="basic-addon1">Email</span>
                    <input type="text" class="form-control" aria-label="email" aria-describedby="basic-addon1"
                        v-model="this.data_cliente.email">

                </div>

                <!-- ACCETTARE INVIO DI EMAIL -->

                <div class=" mx-2 form-check form-switch">
                    <input class="form-check-input" type="checkbox" role="switch" id="flexSwitchCheckChecked"
                        v-model="this.data_cliente.comunicazioni" checked>
                    <label class="form-check-label" for="flexSwitchCheckChecked">Consenso comunicazioni via
                        Email/SMS</label>
                </div>


                <button type="button" @click="addCliente" class="btn btn-success mt-3">Aggiungi</button>




            </div>

            <div class="container">

                <div class="tab-pane fade" id="veicolo-tab-pane" role="tabpanel" aria-labelledby="veicolo-tab"
                    tabindex="0">

                    <div v-if="this.clienteAggiunto == false">
                        <div class="alert alert-warning mt-3" role="alert">
                            Aggiungi prima il cliente per poter aggiungere un veicolo.
                        </div>
                    </div>



                    <!-- Targa -->
                    <div class="input-group mb-3 mt-3">
                        <span class="input-group-text" id="basic-addon1">Targa</span>
                        <input type="text" class="form-control" aria-label="targa" aria-describedby="basic-addon1"
                            v-model="this.data_veicolo.targa" required>
                    </div>

                    <!-- Marca -->
                    <div class="input-group mb-3 mt-3">
                        <span class="input-group-text" id="basic-addon1">Marca</span>
                        <input type="text" class="form-control" aria-label="marca" aria-describedby="basic-addon1"
                            v-model="this.data_veicolo.marca">
                    </div>

                    <!-- Modello -->
                    <div class="input-group mb-3 mt-3">
                        <span class="input-group-text" id="basic-addon1">Modello</span>
                        <input type="text" class="form-control" aria-label="modello" aria-describedby="basic-addon1"
                            v-model="this.data_veicolo.modello">
                    </div>

                    <!-- Cilindrata -->

                    <div class="input-group mb-3 mt-3">
                        <span class="input-group-text" id="basic-addon1">Cilindrata</span>
                        <input type="text" class="form-control" aria-label="cilindrata" aria-describedby="basic-addon1"
                            v-model="this.data_veicolo.cilindrata">
                    </div>


                    <!-- Alimentazione -->

                    <div class="input-group mb-3 mt-3">
                        <span class="input-group-text" id="basic-addon1">Alimentazione</span>
                        <input type="text" class="form-control" aria-label="provincia" aria-describedby="basic-addon1"
                            v-model="this.data_veicolo.alimentazione">

                    </div>

                    <!-- Anno immatricolazione -->

                    <div class="input-group mb-3 mt-3">
                        <span class="input-group-text" id="basic-addon1">Anno immatricolazione</span>
                        <input type="date" class="form-control" aria-label="anno immatricolazione"
                            aria-describedby="basic-addon1" v-model="this.data_veicolo.anno_immatricolazione">

                    </div>

                    <!-- Proprietario -->

                    <div class="input-group mb-3 mt-3">
                        <span class="input-group-text" id="basic-addon1">Proprietario</span>
                        <input type="text" class="form-control" aria-label="telefono"
                            v-model="this.data_cliente.codice_fiscale" aria-describedby="basic-addon1" readonly>
                    </div>

                    <div v-if="clienteAggiunto == true">


                        <button type="button" @click="this.addVeicolo" class="btn btn-warning mt-3">Aggiungi
                            Veicolo</button>
                    </div>


                    <div v-if="veicoloAggiunto == true">

                        <div class="alert alert-success mt-3" role="alert">
                            Veicolo aggiunto con successo.
                        </div>


                        <router-link :to="{ name: 'nuova-polizza-view', params: { id: this.data_veicolo.targa } }"
                            class="btn btn-info">Assicura Veicolo</router-link>


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
    name: 'newClienteView',
    props: {},
    data() {
        return {
            data_cliente: {},
            data_veicolo: {},
            clienteAggiunto: false,
            veicoloAggiunto: false,
        };
    },
    methods: {
        // Add new client
        async addCliente() {
            // Check if required fields are filled
            if (!this.data_cliente.nome || !this.data_cliente.cognome || !this.data_cliente.codice_fiscale) {
                return;
            }

            // Check codice fiscale length
            if (this.data_cliente.codice_fiscale.length !== 16) {
                toast.info("Il codice fiscale deve essere lungo 16 caratteri.");
                return;
            }

            const endpoint = `${endpoints["clientiList"]}`;
            try {
                this.data_cliente.codice_fiscale = this.data_cliente.codice_fiscale.toUpperCase();
                // Add client
                await axios.post(endpoint, this.data_cliente);
                this.clienteAggiunto = true;
                toast.success("Cliente aggiunto con successo");
                // Switch to vehicle tab
                document.getElementById("veicolo-tab").click();
            } catch (error) {
                if (error.response && error.response.data) {
                    const errori = error.response.data;
                    // Display error messages
                    Object.keys(errori).forEach((campo) => {
                        errori[campo].forEach((messaggio) => {
                            toast.error(`${campo}: ${messaggio}`);
                        });
                    });
                } else {
                    toast.error("Errore durante l'aggiunta del cliente");
                }
            }
        },
        // Add new vehicle
        async addVeicolo() {
            const endpoint = `${endpoints["veicoliList"]}`;
            this.data_veicolo.proprietario = this.data_cliente.codice_fiscale;
            try {
                // Add vehicle
                await axios.post(endpoint, this.data_veicolo);
                this.veicoloAggiunto = true;
                toast.success("Veicolo aggiunto con successo");
            } catch (error) {
                if (error.response && error.response.data) {
                    const errori = error.response.data;
                    // Display error messages
                    Object.keys(errori).forEach((campo) => {
                        errori[campo].forEach((messaggio) => {
                            toast.error(`${campo}: ${messaggio}`);
                        });
                    });
                } else {
                    toast.error("Errore durante l'aggiunta del veicolo");
                }
            }
        },
    },
    components: {},
    computed: {},
    created() {},
};

</script>