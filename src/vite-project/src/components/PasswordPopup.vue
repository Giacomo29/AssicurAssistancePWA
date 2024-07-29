<template>
  <div v-show="isOpen" class="password-popup">
    <div class="password-popup-content">
      <h2>Modifica Password</h2>
      <form @submit.prevent="changePassword">
        <div class="form-group">
          <label for="oldPassword">Vecchia Password</label>
          <input type="password" class="form-control" id="oldPassword" v-model="oldPassword">
        </div>
        <div class="form-group">
          <label for="newPassword">Nuova Password</label>
          <input type="password" class="form-control" id="newPassword" v-model="newPassword">
        </div>
        <div class="form-group">
          <label for="confirmNewPassword">Conferma Nuova Password</label>
          <input type="password" class="form-control" id="confirmNewPassword" v-model="confirmNewPassword">
        </div>
        <button type="submit" class="btn btn-primary mb-2 mt-2">Salva Modifiche</button>
      </form>
      <p v-if="errorMessage" class="text-danger">{{ errorMessage }}</p>
      <p v-if="successMessage" class="text-success">{{ successMessage }}</p>
      <button @click="closePopup" class="btn btn-secondary">Chiudi</button>
    </div>
  </div>
</template>

<script>

import { useAuthStore } from '@/stores/auth'
import { axios } from "@/common/api.service.js";
import { toast } from "vue3-toastify";
import "vue3-toastify/dist/index.css";

export default {

  props: {
    isOpen: {
      type: Boolean,
      required: true
    },
    id_account: {
      type: Number,
      required: true
    }
  },
  data() {
    return {
      oldPassword: '',
      newPassword: '',
      confirmNewPassword: '',
      errorMessage: '',
      successMessage: ''
    };
  },
  methods: {
    closePopup() {
      this.$emit('closePopup');
    },
    async changePassword() {

      const authStore = useAuthStore();

      if (this.newPassword !== this.confirmNewPassword) {
        toast.error('Le due password non corrispondono');
        return;
      }

      if (this.newPassword.length < 8) {
        // Se la nuova password non è lunga almeno 8 caratteri, mostra un messaggio di errore
        toast.error('La nuova password deve essere lunga almeno 8 caratteri');
        return;
      }

      try {
        // Effettua la chiamata API per cambiare la password
        const response = await axios.put(`/api/user/change_password/${this.id_account}/`, {
          old_password: this.oldPassword,
          password: this.newPassword,
          password2: this.confirmNewPassword
        });

        // Verifica se la richiesta è stata eseguita con successo
        if (response.status === 200) {
          // Password modificata con successo
          toast.success('Password modificata con successo');
          // Resetta i campi della password
          this.oldPassword = '';
          this.newPassword = '';
          this.confirmNewPassword = '';
        } else {
          // Gestione degli errori in caso di risposta non corretta
          console.error('Errore durante la modifica della password:', response);
          toast.error('Si è verificato un errore durante la modifica della password. Si prega di riprovare più tardi.');
        }
      } catch (error) {
        // Gestione degli errori di rete o altri errori
        console.error('Errore durante la modifica della password:', error);
        toast.error('Si è verificato un errore durante la modifica della password. Si prega di riprovare più tardi.');
      }

    }
  }
};
</script>

<style scoped>
.password-popup {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
}

.password-popup-content {
  background-color: #fff;
  padding: 20px;
  border-radius: 5px;
}
</style>
