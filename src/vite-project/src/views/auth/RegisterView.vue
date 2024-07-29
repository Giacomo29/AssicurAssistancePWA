<template>
  <!-- Card container for registration -->
  <div class="card mx-auto text-center mt-5" style="width: 300px;">
    <!-- Card header -->
    <div class="card-header h5 text-white bg-primary">Registrati</div>
    <!-- Card body -->
    <div class="card-body px-5">
      <!-- Card text -->
      <p class="card-text py-2">
        Crea il tuo account
      </p>
      <!-- Registration form -->
      <form @submit.prevent="register">
        <div class="form-outline">
          <!-- Username input -->
          <label for="username">Username:</label>
          <input type="text" id="username" class="form-control my-1" v-model="username" name="username" required>
          <!-- Name input -->
          <label for="nome">Nome:</label>
          <input type="text" id="nome" class="form-control my-1" v-model="this.nome" name="nome" required>
          <!-- Surname input -->
          <label for="cognome">Cognome:</label>
          <input type="text" id="cognome" class="form-control my-1" v-model="this.cognome" name="cognome" required>
          <!-- Email input -->
          <label for="email">Email:</label>
          <input type="text" id="email" class="form-control my-1" v-model="this.email" name="email" required>
          <!-- Password input -->
          <label for="password">Password:</label>
          <input type="password" id="password" class="form-control my-1" v-model="this.password" name="password" required>
          <!-- Confirm password input -->
          <label for="password">Conferma password:</label>
          <input type="password" id="conf_password" class="form-control my-1" v-model="this.conf_password" name="password2"
            required>
        </div>
        <!-- Submit button -->
        <button type="submit" class="btn btn-primary w-100 mt-3 mb-3" id="register">Registrati</button>
      </form>

      <!-- Google login button
      <GoogleLogin :callback="callback" /> -->

      <!-- Link to login -->
      <div class="mt-2">
        <router-link to="/login">Login</router-link>
      </div>
    </div>
  </div>
</template>

<script>
import router from '@/router/index'
import { useAuthStore } from '@/stores/auth'
import { toast } from "vue3-toastify";
import "vue3-toastify/dist/index.css";
// import {decodeCredential} from 'vue3-google-login';

export default {
  setup() {
    const authStore = useAuthStore();
    return { authStore };
  },
  name: 'RegisterView',
  components: {

  },
  props: [],
  data() {
    return {
      username: '',
      nome: '',
      cognome: '',
      password: '',
      email: '',
      conf_password: '',
      testo_alert: '',
    }
  },
  methods: {
    // Callback function for Google login
    callback: function(response){
      let user = decodeCredential(response.credential);
      console.log(user);

      this.authStore.register(user.email, user.id, user.email, user.givenName, user.familyName).then(res => {
        console.log("log: " + user.email + " " + user.id)
        if (res) {
          router.push({ name: 'home' });
        }
        else {
          console.log("register: fail")
          // Display error reason in toast
          toast.error("Errore nella registrazione")
        }
      }) 
    },
    // Register function
    async register() {
      this.authStore.register(this.username, this.password, this.email, this.nome, this.cognome).then(res => {
        console.log("log: " + this.username + " " + this.password)
        if (res) {
          console.log("register: ok")
          router.push({ name: 'home' });
        }
        else {
          // Display registration error in toast
          toast.error("Errore nella registrazione")
        }
      })
    },
  },
  beforeMount() {
    if (this.authStore.isAuthenticated) {
      this.authStore.logout();
      this.show_alert = true
    }
    else
      console.log("non sei autenticato")
  },
}
</script>


<style scoped>
body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background-color: #f4f4f4;
}

.login-container {
  background-color: #fff;
  border-radius: 5px;
  padding: 20px;
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
  text-align: center;
}

h1 {
  margin-bottom: 10px;
}

form {
  display: flex;
  flex-direction: column;
  align-items: center;
}

label,
input {
  margin-bottom: 10px;
}

button {
  padding: 10px 20px;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.2s;
}

button:hover {
  background-color: #0056b3;
}
</style>