<template>
  <!-- Card container for password reset -->
  <div class="card mx-auto text-center mt-5" style="width: 300px;">
    <!-- Card header -->
    <div class="card-header h5 text-white bg-primary">Password Reset</div>
    <!-- Card body -->
    <div class="card-body px-5">
      <!-- Card text -->
      <p class="card-text py-2">
        Inserisci la nuova password
      </p>
      <!-- Password reset form -->
      <form @submit.prevent="resetPassword">
        <div class="form-outline">
          <!-- Password input -->
          <input type="password" id="password" class="form-control my-3" v-model="password" name="email" required>
          <!-- Confirm password input -->
          <input type="password" id="confirmPassword" class="form-control my-3" v-model="confirmPassword" name="email" required>
        </div>
        <!-- Submit button -->
        <button type="submit" class="btn btn-primary w-100" id="email">Reset password</button>
      </form>
      <!-- Links to login and register -->
      <div class="d-flex justify-content-between mt-4">
        <router-link to="/login">Login</router-link>
        <router-link to="/register">Register</router-link>
      </div>
    </div>
  </div>
</template>

<script>
import { endpoints } from "@/common/endpoints.js";
import { toast } from "vue3-toastify";
import "vue3-toastify/dist/index.css";
import { useRouter } from 'vue-router';
import { ref } from 'vue';
import axios from 'axios';

export default {
  setup() {
    const router = useRouter();
    const password = ref('');
    const confirmPassword = ref('');

    // Extract parameters from URL query string
    const uidb64 = router.currentRoute.value.query.uidb64;
    const token = router.currentRoute.value.query.token;

    const resetPassword = () => {
      // Check if passwords match
      if (password.value !== confirmPassword.value) {
        toast.error("Le password non corrispondono");
        return;
      }
      // Code to reset password using uidb64, token, password, and confirmPassword
      // Perform this API call to reset password: path('password-reset/<uidb64>/<token>/',PasswordTokenCheckAPI.as_view(), name='password-reset-confirm'),

      const endpoint = `${endpoints["resetPasswordToken"]}/${uidb64}/${token}/`;
      axios.get(endpoint)
        .then((response) => {
          const endpoint = `${endpoints["newPassword"]}`;
          axios.patch(endpoint, {
            password: password.value,
            confirmPassword: confirmPassword.value,
            uidb64: uidb64,
            token: token
          })
          .then((response) => {
            console.log("Password reimpostata con successo:", response);
            toast.success("Password reimpostata con successo");
            router.push({ name: 'login' });
          })
          .catch((error) => {
            console.error("Errore durante il reset della password:", error);
            toast.error("Errore durante il reset della password assicurati che la password sia lunga almeno 6 caratteri e contenga almeno un numero e un carattere speciale");
          });
        })
        .catch((error) => {
          console.error("Errore durante il reset della password:", error);
          toast.error("Errore durante il reset della password assicurati che la password sia lunga almeno 6 caratteri e contenga almeno un numero e un carattere speciale");
        });
      
    };

    return {
      password,
      confirmPassword,
      resetPassword
    };
  }
};
</script>
