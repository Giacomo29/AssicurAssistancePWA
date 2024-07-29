<!-- views/ResetPasswordPage.vue -->

<template>
    <div>
      <h2>Reimposta la tua password</h2>
      <form @submit.prevent="resetPassword">
        <label for="password">Nuova password:</label>
        <input type="password" id="password" v-model="password" required>
        <button type="submit">Conferma</button>
      </form>
    </div>
  </template>
  
  <script>


import { axios } from "@/common/api.service.js";
import { endpoints } from "@/common/endpoints.js";
import "vue3-toastify/dist/index.css";
;


  export default {


    props: ['userId', 'token'],
    data() {
      return {
        password: '',
      };
    },
    methods: {
      async resetPassword() {
        // Esegui la richiesta API per reimpostare la password
        try {
          await axios.patch(`/api/password-reset-complete/`, {
            token: this.token,
            uidb64 : this.userId,
            password: this.password,
          });
          // Reindirizza l'utente a una pagina di conferma o a un'altra destinazione
          this.$router.push('/password-reset-success');
        } catch (error) {
          console.error('Errore durante la reimpostazione della password:', error);
          // Gestisci gli errori o mostra un messaggio all'utente
        }
      },
    },
  };
  </script>
  