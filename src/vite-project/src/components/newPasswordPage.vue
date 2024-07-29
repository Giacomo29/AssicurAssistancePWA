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
          await axios.post(`/api/password-reset/${this.userId}/${this.token}`, {
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
  