<template>
    <div>
      <input type="file" ref="fileInput" @change="handleFileChange" />
      <button @click="uploadFile">Carica Documento</button>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        file: null,
      };
    },
    methods: {
      handleFileChange(event) {
        this.file = event.target.files[0];
      },
      uploadFile() {
        const formData = new FormData();
        formData.append('documenti', this.file);
  
        // Sostituisci con l'URL corretto della tua API DRF
        const apiUrl = 'http://localhost:8000/api/polizze/';
  
        this.$axios.post(apiUrl, formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        })
        .then(response => {
          console.log('Documento caricato con successo:', response.data);
          // Aggiorna lo stato o gestisci la risposta come necessario
        })
        .catch(error => {
          console.error('Errore durante l\'upload del documento:', error);
          // Gestisci l'errore come necessario
        });
      },
    },
  };
  </script>
  
  <style>
  /* Stili opzionali per il tuo componente */
  </style>
  