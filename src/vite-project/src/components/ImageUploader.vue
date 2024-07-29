<template>
    <div>
      <input type="file" ref="fileInput" @change="handleFileChange" class="form-control"/>
    </div>


  </template>
  
  <script>



import { axios } from "@/common/api.service.js";
import { endpoints } from "@/common/endpoints.js";
import { toast } from "vue3-toastify";
import "vue3-toastify/dist/index.css";



  export default {



    data() {
      return {
        selectedFile: null,
      };
    },
    methods: {
      handleFileChange(event) {
        this.selectedFile = event.target.files[0];
        this.uploadImage();
      },
      uploadImage() {
        const formData = new FormData();
        formData.append('avatar', this.selectedFile);
  
        // Utilizza Axios per inviare la richiesta POST con l'immagine
        // Sostituisci 'API_URL' con l'URL effettivo della tua API
        const endpoint = `${endpoints["updateAvatar"]}`;
        axios.post(endpoint, formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        })
        .then(response => {
          console.log('Immagine caricata con successo:', response.data);
          toast.success("Immagine caricata con successo");
          // Aggiorna i dati dell'utente per riflettere l'immagine del profilo aggiornata
          this.$emit('updateUserData');
        })
        .catch(error => {
          console.error('Errore durante l\'upload dell\'immagine:', error);
            toast.error("Errore durante l'upload dell'immagine");
          // Gestisci eventuali errori
        });
      },
    },
  };
  </script>