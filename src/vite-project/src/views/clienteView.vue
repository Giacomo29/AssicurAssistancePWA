<template>
    <!-- Card Cliente -->
    <div class="container mt-4">

        <h1 class="text-center text-danger" v-if="Object.keys(data_cliente).length === 0"> Nessun Cliente Trovato</h1>

        <div v-else>
            <h1 class="text-center">Dettagli Cliente</h1>
            <div class="card shadow rounded mb-4">

                <div class="card-header bg-primary text-white">
                    <h3 class="card-title">{{ this.data_cliente.nome }} {{ this.data_cliente.cognome }}</h3>
                </div>
                <div class="card-body">
                    <div v-if="!editingMode">

                        <h4>Codice fiscale: {{ data_cliente.codice_fiscale }}</h4>



                        <h4 v-if="data_cliente.indirizzo">Indirizzo: {{ data_cliente.indirizzo }}</h4>
                        <h4 v-if="data_cliente.telefono">Telefono: {{ data_cliente.telefono }}</h4>
                        <h4 v-if="data_cliente.email">Email: {{ data_cliente.email }}</h4>
                        <h4 v-if="data_cliente.citta">Città: {{ data_cliente.citta }}</h4>
                        <h4 v-if="data_cliente.cap">Cap: {{ data_cliente.cap }}</h4>
                        <h4 v-if="data_cliente.provincia">Provincia: {{ data_cliente.provincia }}</h4>
                        <h4 v-if="data_cliente.data_nascita">Data di nascita: {{ data_cliente.data_nascita }}</h4>


                        <button class="btn btn-primary mb-3" @click="toggleEditMenu">Modifica</button>

                        <div class="position-relative">
                            <svg viewBox="0 0 24 24" fill="none" @click="deleteCliente(data_cliente.codice_fiscale)"
                                    class="icon_bin" xmlns="http://www.w3.org/2000/svg">
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


                    <!-- Campi di modifica -->
                    <div v-else>


                        <div class="container">

                            <!-- NOME -->
                            <div>
                                <div class="input-group mb-3">
                                    <span class="input-group-text" id="basic-addon1">Nome</span>
                                    <input type="text" class="form-control" v-model="this.editData.nome"
                                        aria-label="nome" aria-describedby="basic-addon1">
                                </div>

                                <!-- COGNOME -->
                                <div class="input-group mb-3">
                                    <span class="input-group-text" id="basic-addon1">Cognome</span>
                                    <input type="text" class="form-control" v-model="this.editData.cognome"
                                        aria-label="nome" aria-describedby="basic-addon1">
                                </div>


                                <div class="input-group mb-3">
                                    <span class="input-group-text" id="basic-addon1">Codice fiscale</span>
                                    <input type="text" class="form-control" required
                                        v-model="this.editData.codice_fiscale" aria-label="nome"
                                        aria-describedby="basic-addon1">
                                </div>

                                <!-- INDIRIZZO -->
                                <div class="input-group mb-3">
                                    <span class="input-group-text" id="basic-addon1">Indirizzo</span>
                                    <input type="text" class="form-control" required v-model="this.editData.indirizzo"
                                        aria-label="nome" aria-describedby="basic-addon1">
                                </div>

                                <!-- TELEFONO -->

                                <div class="input-group mb-3">
                                    <span class="input-group-text" id="basic-addon1">Telefono</span>
                                    <input type="tel" class="form-control" required v-model="this.editData.telefono"
                                        aria-label="nome" aria-describedby="basic-addon1">
                                </div>


                                <!-- EMAIL -->

                                <div class="input-group mb-3">
                                    <span class="input-group-text">@</span>
                                    <input type="text" class="form-control" v-model="this.editData.email"
                                        aria-label="Server">
                                </div>

                                <!-- CITTA -->

                                <div class="input-group mb-3">
                                    <span class="input-group-text" id="basic-addon1">Città</span>
                                    <input type="text" class="form-control" required v-model="this.editData.citta"
                                        aria-label="nome" aria-describedby="basic-addon1">
                                </div>

                                <!-- CAP -->

                                <div class="input-group mb-3">
                                    <span class="input-group-text" id="basic-addon1">Cap</span>
                                    <input type="text" class="form-control" required v-model="this.editData.cap"
                                        aria-label="nome" aria-describedby="basic-addon1">
                                </div>

                                <!-- PROVINCIA -->

                                <div class="input-group mb-3">
                                    <span class="input-group-text" id="basic-addon1">Provincia</span>
                                    <input type="text" class="form-control" required v-model="this.editData.provincia"
                                        aria-label="nome" aria-describedby="basic-addon1">
                                </div>

                                <!-- DATA DI NASCITA -->

                                <div class="input-group mb-3">
                                    <span class="input-group-text" id="basic-addon1">Data di nascita</span>
                                    <input type="date" class="form-control" required
                                        v-model="this.editData.data_nascita" aria-label="nome"
                                        aria-describedby="basic-addon1">
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

            <h2 class="text-center">Garage Cliente</h2>


            <!-- Card Veicolo -->
            <div v-for="(veicolo, index) in data_veicoli.results" :key="index">
                <div class="card shadow rounded mb-4">
                    <div class="card-header bg-info text-white">
                        <h3 class="card-title">{{ veicolo.targa }}</h3>
                    </div>
                    <div class="card-body">
                        <div v-if="veicolo.editingMode == false">
                            <h4>Marca: {{ veicolo.marca }}</h4>
                            <h4>Modello: {{ veicolo.modello }}</h4>
                            <h4>Cilindrata: {{ veicolo.cilindrata }}</h4>
                            <h4>Alimentazione: {{ veicolo.alimentazione }}</h4>
                            <h4>Anno immatricolazione: {{ veicolo.anno_immatricolazione }}</h4>
                            <div v-if="veicolo.assicurato == false" class="mb-3">
                                <router-link :to="{ name: 'nuova-polizza-view', params: { id: veicolo.targa } }"
                                    class="btn btn-warning mt-3">Assicura veicolo</router-link>
                            </div>
                            <div v-else class="mb-3">
                                <button type="button" @click="this.apriPolizza(veicolo.targa)" class="btn btn-info mt-3">Apri
                                    polizza</button>
                            </div>
                            <button class="btn btn-primary mb-3"
                                @click="toggleEditMenuVeicolo(veicolo.targa)">Modifica</button>
                            <div class="position-relative">
                                <svg viewBox="0 0 24 24" fill="none" @click="deleteVeicolo(veicolo.targa)"
                                    class="icon_bin" xmlns="http://www.w3.org/2000/svg">
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
                            <!-- Altri dettagli del veicolo -->
                        </div>

                        <div v-else>

                            <div>
                                <div class="input-group mb-3">
                                    <span class="input-group-text" id="basic-addon1">Marca</span>
                                    <input type="text" class="form-control" v-model="this.editDataVeicolo.marca"
                                        aria-label="nome" aria-describedby="basic-addon1">
                                </div>
                            </div>


                            <div>
                                <div class="input-group mb-3">
                                    <span class="input-group-text" id="basic-addon1">Modello</span>
                                    <input type="text" class="form-control" v-model="this.editDataVeicolo.modello"
                                        aria-label="nome" aria-describedby="basic-addon1">
                                </div>
                            </div>


                            <div>
                                <div class="input-group mb-3">
                                    <span class="input-group-text" id="basic-addon1">Cilindrata</span>
                                    <input type="number" class="form-control" v-model="this.editDataVeicolo.cilindrata"
                                        aria-label="nome" aria-describedby="basic-addon1">
                                </div>
                            </div>

                            <div>
                                <div class="input-group mb-3">
                                    <span class="input-group-text" id="basic-addon1">Anno immatricolazione</span>
                                    <input type="text" class="form-control"
                                        v-model="this.editDataVeicolo.anno_immatricolazione" aria-label="nome"
                                        aria-describedby="basic-addon1">
                                </div>
                            </div>

                            <div>
                                <div class="input-group mb-3">
                                    <span class="input-group-text" id="basic-addon1">Alimentazione</span>
                                    <input type="text" class="form-control" v-model="this.editDataVeicolo.alimentazione"
                                        aria-label="nome" aria-describedby="basic-addon1">
                                </div>
                            </div>


                            <!-- BOTTONI SALVATAGGIO E ANNULLA -->
                            <div class="d-flex justify-content-end">
                                <button @click="saveChangesVeicolo(this.editDataVeicolo.targa)" type="button"
                                    class="btn btn-success m-3">Salva</button>
                                <button @click="cancelEdit(2, this.editDataVeicolo.targa)" type="button"
                                    class="btn btn-danger m-3">Annulla</button>
                            </div>


                        </div>
                    </div>

                </div>
            </div>

            <div class="d-flex justify-content-center bg-image hover-overlay hover-zoom hover-shadow ripple mb-5">
                <svg viewBox="0 0 32 32" @click="this.addingMode = !this.addingMode"
                    class="icon_add_aggiungi d-flex justify-content-center" version="1.1" xmlns="http://www.w3.org/2000/svg"
                    xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:sketch="http://www.bohemiancoding.com/sketch/ns"
                    fill="#000000">
                    <g id="SVGRepo_bgCarrier" stroke-width="0"></g>
                    <g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g>
                    <g id="SVGRepo_iconCarrier">
                        <title>plus-circle</title>
                        <desc>Created with Sketch Beta.</desc>
                        <defs> </defs>
                        <g id="Page-1" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd"
                            sketch:type="MSPage">
                            <g id="Icon-Set-Filled" sketch:type="MSLayerGroup"
                                transform="translate(-466.000000, -1089.000000)" fill="#000000">
                                <path
                                    d="M488,1106 L483,1106 L483,1111 C483,1111.55 482.553,1112 482,1112 C481.447,1112 481,1111.55 481,1111 L481,1106 L476,1106 C475.447,1106 475,1105.55 475,1105 C475,1104.45 475.447,1104 476,1104 L481,1104 L481,1099 C481,1098.45 481.447,1098 482,1098 C482.553,1098 483,1098.45 483,1099 L483,1104 L488,1104 C488.553,1104 489,1104.45 489,1105 C489,1105.55 488.553,1106 488,1106 L488,1106 Z M482,1089 C473.163,1089 466,1096.16 466,1105 C466,1113.84 473.163,1121 482,1121 C490.837,1121 498,1113.84 498,1105 C498,1096.16 490.837,1089 482,1089 L482,1089 Z"
                                    id="plus-circle" sketch:type="MSShapeGroup"> </path>
                            </g>
                        </g>
                    </g>
                </svg>
            </div>

            <div v-if="addingMode == true">
                <div>

                    <div class="card text-bg-light mb-3 mt-3" style="max-width">
                        <div class="card-header">Stai aggiungendo un veicolo al cliente {{ data_cliente.cognome }}</div>
                        <div class="card-body">

                            <!-- TARGA -->

                            <div>
                                <div class="input-group mb-3">
                                    <span class="input-group-text" id="basic-addon1">Targa</span>
                                    <input type="text" class="form-control" v-model="this.newVeicolo.targa"
                                        aria-label="nome" aria-describedby="basic-addon1">
                                </div>
                            </div>

                            <!-- MARCA -->
                            <div>
                                <div class="input-group mb-3">
                                    <span class="input-group-text" id="basic-addon1">Marca</span>
                                    <input type="text" class="form-control" v-model="this.newVeicolo.marca"
                                        aria-label="nome" aria-describedby="basic-addon1">
                                </div>
                            </div>

                            <!-- MODELLO -->
                            <div>
                                <div class="input-group mb-3">
                                    <span class="input-group-text" id="basic-addon1">Modello</span>
                                    <input type="text" class="form-control" v-model="this.newVeicolo.modello"
                                        aria-label="nome" aria-describedby="basic-addon1">
                                </div>
                            </div>


                            <!-- CILINDRATA -->

                            <div>
                                <div class="input-group mb-3">
                                    <span class="input-group-text" id="basic-addon1">Cilindrata</span>
                                    <input type="text" class="form-control" v-model="this.newVeicolo.cilindrata"
                                        aria-label="nome" aria-describedby="basic-addon1">
                                </div>
                            </div>


                            <!-- ALIMENTAZIONE -->
                            <div>
                                <div class="input-group mb-3">
                                    <span class="input-group-text" id="basic-addon1">Alimentazione</span>
                                    <input type="text" class="form-control" v-model="this.newVeicolo.alimentazione"
                                        aria-label="nome" aria-describedby="basic-addon1">
                                </div>
                            </div>

                            <!-- ANNO IMMATRICOLAZIONE -->
                            <div>
                                <div class="input-group mb-3">
                                    <span class="input-group-text" id="basic-addon1">Anno immatricolazione</span>
                                    <input type="date" class="form-control"
                                        v-model="this.newVeicolo.anno_immatricolazione" aria-label="nome"
                                        aria-describedby="basic-addon1">
                                </div>
                            </div>

                            <button type="button" @click="addVeicolo" class="btn btn-success">Aggiungi veicolo</button>



                        </div>
                    </div>



                </div>
            </div>

        </div>

    </div>
</template>






<script>
import { axios } from "@/common/api.service.js";
import { endpoints } from "@/common/endpoints.js";
import router from "../router";
import { toast } from "vue3-toastify";
import "vue3-toastify/dist/index.css";




export default {
    name: 'clienteView',
    props: {
        id: {
            type: String,
            required: true
        }
    },
    data() {
        return {
            data_cliente: {},
            data_veicoli: [],
            newVeicolo: {},
            editData: {},
            editDataVeicolo: {},
            editingMode: false,
            editingModeVeicolo: false,
            addingMode: false,
            clienti: [],
            id_cliente: this.id,

        };
    },
    methods: {

        async addVeicolo() {

            const endpoint = `${endpoints["veicoliList"]}`;
            this.newVeicolo.proprietario = this.id;
            this.newVeicolo.assicurato = false;
            try {
                await axios.post(endpoint, this.newVeicolo);
                toast.success("Veicolo aggiunto con successo");
                this.getVeicoliCliente();
            }
            catch (error) {
                if (error.response && error.response.data) {
                    const errori = error.response.data;
                    Object.keys(errori).forEach((campo) => {
                        errori[campo].forEach((messaggio) => {
                            toast.error(`${campo}: ${messaggio}`);
                        });
                    });
                } else {
                    toast.error("Errore durante l'aggiunta del veicolo");
                }
            }
            this.addingMode = false;

        },

        async deleteVeicolo(targa) {
            const conferma = window.confirm("Sei sicuro di voler eliminare questo veicolo?");
            if (!conferma) {
                return;
            }
            const endpoint = `${endpoints["veicoliDetail"]}${targa}/`;
            try {
                await axios.delete(endpoint);
                toast.info("Veicolo eliminato con successo");
                this.getVeicoliCliente();
            }
            catch (error) {
                if (error.response && error.response.data) {
                    const errori = error.response.data;
                    Object.keys(errori).forEach((campo) => {
                        errori[campo].forEach((messaggio) => {
                            toast.error(`${campo}: ${messaggio}`);
                        });
                    });
                } else {
                    toast.error("Errore durante l'eliminazione del veicolo");
                }
            }
        },

        async deleteCliente(codice_fiscale) {

            const conferma = window.confirm("Sei sicuro di voler eliminare questo cliente? Eliminando il cliente verranno eliminati anche tutti i suoi veicoli.");
            if (!conferma) {
                return;
            }
            const endpoint = `${endpoints["clientiDetail"]}${codice_fiscale}/`;
            try {
                await axios.delete(endpoint);
                toast.info("Cliente eliminato con successo.");
                this.getClienti();
            }
            catch (error) {
                if (error.response && error.response.data) {
                    const errori = error.response.data;
                    Object.keys(errori).forEach((campo) => {
                        errori[campo].forEach((messaggio) => {
                            toast.error(`${campo}: ${messaggio}`);
                        });
                    });
                } else {
                    toast.error("Errore durante l'eliminazione del cliente.");
                }
            }

        },

        async apriPolizza(targa) {

            const polizza_id = await this.getPolizzaIdByTarga(targa);
            this.$router.push({ name: "polizza-view", params: { id: polizza_id } });
        },


        async getDataCliente() {
            try {
                const endpoint = `${endpoints["clientiDetail"]}${this.id}/`;
                const response = await axios.get(endpoint);
                this.data_cliente = response.data;
            }
            catch (error) {
                if (error.response && error.response.data) {
                    const errori = error.response.data;
                    Object.keys(errori).forEach((campo) => {
                        errori[campo].forEach((messaggio) => {
                            toast.error(`${campo}: ${messaggio}`);
                        });
                    });
                } else {
                    toast.error("Errore durante il recupero dei dati del cliente.");
                }
            }
        },

        async getVeicoliCliente() {
            try {
                const endpoint = `${endpoints["veicoliCliente"]}${this.id}/`;
                const response = await axios.get(endpoint);
                this.data_veicoli = response.data;
                

                this.data_veicoli.results = this.data_veicoli.results.map(veicolo => {
                    return {
                        ...veicolo,
                        editingMode: false,
                    };
                });



            }
            catch (error) {
                if (error.response && error.response.data) {
                    const errori = error.response.data;
                    Object.keys(errori).forEach((campo) => {
                        errori[campo].forEach((messaggio) => {
                            toast.error(`${campo}: ${messaggio}`);
                        });
                    });
                } else {
                    toast.error("Errore durante il recupero dei veicoli del cliente.");
                }
            }
        },


        async toggleEditMenu() {
            this.editingMode = !this.editingMode;
            // Quando attivi la modalità di modifica, copia i dati originali in editData
            if (this.editingMode) {
                this.editData = { ...this.data_cliente };
            }
        },



        async toggleEditMenuVeicolo(targa) {
            const veicolo = this.data_veicoli.results.find(x => x.targa == targa);
            veicolo.editingMode = !veicolo.editingMode;
            // Quando attivi la modalità di modifica, copia i dati originali in editData
            if (veicolo.editingMode) {
                this.editDataVeicolo = { ...this.data_veicoli.results.find(x => x.targa == targa) };
            }
        },


        async saveChangesVeicolo(targa) {
            const endpoint = `${endpoints["veicoliDetail"]}${this.editDataVeicolo.targa}/`;
            try {

                console.log(this.editDataVeicolo)
                await axios.put(endpoint, this.editDataVeicolo);
                toast.info("Modifiche salvate con successo.");
                this.data_veicoli.results.splice(this.data_veicoli.results.findIndex(x => x.targa == this.editDataVeicolo.targa), 1, this.editDataVeicolo);
                const veicolo = this.data_veicoli.results.find(x => x.targa == targa);
                veicolo.editingMode = false;


            }
            catch (error) {
                if (error.response && error.response.data) {
                    const errori = error.response.data;
                    Object.keys(errori).forEach((campo) => {
                        errori[campo].forEach((messaggio) => {
                            toast.error(`${campo}: ${messaggio}`);
                        });
                    });
                } else {
                    toast.error("Errore durante il salvataggio delle modifiche.");
                }
            }
        },


        async saveChanges() {
            const endpoint = `${endpoints["clientiDetail"]}${this.id}/`;
            try {

                console.log(this.editData);
                await axios.put(endpoint, this.editData);
                this.data_cliente = { ...this.editData };
                toast.info("Modifiche salvate con successo.");
                this.editingMode = false;
            }
            catch (error) {
                if (error.response && error.response.data) {
                    const errori = error.response.data;
                    Object.keys(errori).forEach((campo) => {
                        errori[campo].forEach((messaggio) => {
                            toast.error(`${campo}: ${messaggio}`);
                        });
                    });
                } else {
                    toast.error("Errore durante il salvataggio delle modifiche.");
                }
            }
        },

        cancelEdit(card, targa) {
            // Annulla le modifiche e disattiva la modalità di modifica
            if (card == 1)
                this.editingMode = false;
            else if (card == 2) {
                const veicolo = this.data_veicoli.results.find(x => x.targa == targa);
                veicolo.editingMode = false;
            }
        },


        async getClienti() {
            try {
                const endpoint = `${endpoints["clientiList"]}`;

                const response = await axios.get(endpoint);
                this.clienti = response.data;

            }
            catch (error) {
                if (error.response && error.response.data) {
                    const errori = error.response.data;
                    Object.keys(errori).forEach((campo) => {
                        errori[campo].forEach((messaggio) => {
                            toast.error(`${campo}: ${messaggio}`);
                        });
                    });
                } else {
                    toast.error("Errore durante il recupero dei clienti.");
                }
            }
        },

        selectCliente(cliente) {
            this.id_cliente = cliente.codice_fiscale;
        },


        async apriPolizza(targa) {
            const polizza_id = await this.getPolizzaIdByTarga(targa);
            this.$router.push({ name: "polizza-view", params: { id: polizza_id } });
        },


        async getPolizzaIdByTarga(targa) {
            const endpoint = `${endpoints["polizzeTarga"]}${targa}/`;
            try {
                const response = await axios.get(endpoint);
                const polizza = response.data;
                if (polizza.results.length > 0) {
                    return polizza.results[0].id_polizza;
                } else {
                    return null; // Se la polizza non viene trovata, restituisci un valore nullo o un valore di default
                }
            } catch (error) {
                console.log(error);
                return null; // In caso di errore, restituisci un valore nullo o un valore di default
            }
        },




    },
    components: { router },
    created() {


        this.getDataCliente();
        this.getVeicoliCliente();

    },
}
</script>