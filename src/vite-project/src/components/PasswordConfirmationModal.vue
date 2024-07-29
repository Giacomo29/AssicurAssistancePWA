<template>
  <div v-if="isVisible" class="password-popup">
    <div class="password-popup-content">
      <h2>Inserisci la tua password di conferma</h2>
      <input v-model="password" type="password" placeholder="Password">
      <button class="btn btn-primary btn-sm mx-1" @click="confirm">Conferma</button>
      <button class="btn btn-primary btn-sm mx-1" @click="cancel">Annulla</button>
    </div>
  </div>
</template>




<script>
export default {
  data() {
    return {
      isVisible: false,
      password: '',
    };
  },
  methods: {
    open() {
      this.isVisible = true;
    },
    close() {
      this.isVisible = false;
      this.password = ''; // Pulisci il campo password quando si chiude
    },
    confirm() {
      this.$emit('password-confirmed', this.password);
      this.close();
    },
    cancel() {
      this.$emit('cancel');
      this.close();
    },
  },
};
</script>

<style scoped>
/* Stili per il modal (puoi personalizzarli secondo le tue esigenze) */

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