<template>
    <div>
      <div class="container mt-4">
        <!-- Card Cliente -->
        <div class="card shadow rounded mb-4">
          <div class="card-header bg-primary text-white">
            <h3 class="card-title">Cliente</h3>
          </div>
          <div class="card-body" v-if="clienteData">
            <h4>Nome: {{ clienteData.nome }}</h4>
            <h4>Cognome: {{ clienteData.cognome }}</h4>
            <h4>Codice Fiscale: {{ clienteData.codice_fiscale }}</h4>
            <div v-if="clienteData.codice_fiscale !== veicoloData.proprietario">
              <h4>Proprietario del veicolo: No</h4>
            </div>
            <div v-else>
              <h4>Proprietario del veicolo: Si</h4>
            </div>
          </div>
        </div>
  
        <!-- Card Proprietario -->
        <div v-if="clienteData.codice_fiscale !== veicoloData.proprietario">
          <div class="card shadow rounded mb-4">
            <div class="card-header bg-info text-white">
              <h3 class="card-title">Proprietario del veicolo</h3>
            </div>
            <div class="card-body">
              <h4>Nome: {{ proprietarioData.nome }}</h4>
              <h4>Cognome: {{ proprietarioData.cognome }}</h4>
              <h4>Codice fiscale: {{ proprietarioData.codice_fiscale }}</h4>
            </div>
          </div>
        </div>
  
        <!-- Card Polizza -->
        <div class="card shadow rounded mb-4">
          <div class="card-header bg-success text-white">
            <h3 class="card-title">Polizza</h3>
          </div>
          <div class="card-body">
            <h4>Compagnia: {{ polizzaData.compagnia }}</h4>
            <h4>Semestrale: {{ polizzaData.semestrale }}</h4>
            <h4>Scadenza: {{ polizzaData.data_fine }}</h4>
            <div v-if="polizzaData.semestrale">
              <h4>Scadenza secondo rinnovo: {{ polizzaData.data_fine_due }}</h4>
            </div>
            <!-- Altri dettagli della polizza -->
          </div>
        </div>
  
        <!-- Card Veicolo -->
        <div class="card shadow rounded mb-4">
          <div class="card-header bg-info text-white">
            <h3 class="card-title">Veicolo</h3>
          </div>
          <div class="card-body">
            <h4>Targa: {{ veicoloData.targa }}</h4>
            <h4>Marca: {{ veicoloData.marca }}</h4>
            <h4>Modello: {{ veicoloData.modello }}</h4>
            <h4>Cilindrata: {{ veicoloData.cilindrata }}</h4>
            <h4>Alimentazione: {{ veicoloData.alimentazione }}</h4>
            <h4>Anno immatricolazione: {{ veicoloData.anno_immatricolazione }}</h4>
            <!-- Altri dettagli del veicolo -->
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'CardCliente',
    props: {
      clienteData: {
        type: Object,
        required: true,
      },
      veicoloData: {
        type: Object,
        required: true,
      },
      proprietarioData: {
        type: Object,
        required: true,
      },
      polizzaData: {
        type: Object,
        required: true,
      },
    },
  };
  </script>
  