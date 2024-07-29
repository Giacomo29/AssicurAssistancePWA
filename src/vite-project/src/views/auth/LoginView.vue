<template>
  <!-- Centered card container -->
  <div class="card mx-auto text-center mt-5" style="width: 300px;">
    <!-- Card header -->
    <div class="card-header h5 text-white bg-primary">Login</div>
    <!-- Card body -->
    <div class="card-body px-5">
      <!-- Card text -->
      <p class="card-text py-2">
        Sign in to your account
      </p>
      <!-- Login form -->
      <form @submit.prevent="login">
        <!-- Username input -->
        <div class="form-outline">
          <label for="username">Username:</label>
          <input type="text" id="username" class="form-control my-1" v-model="username" name="username" required>
          <!-- Password input -->
          <label for="password">Password:</label>
          <input type="password" id="password" class="form-control my-1" v-model="password" name="email" required>
        </div>
        <!-- Submit button -->
        <button type="submit" class="btn btn-primary w-100 mb-3 mt-3" id="email">Sign In</button>

        <!-- Google Login component -->
        <GoogleLogin :callback="callback" />

        <!-- Forgot password link -->
        <div class="mt-4">
          <router-link to="/reset-password">Forgot Password?</router-link>
        </div>
        <!-- Registration link -->
        <div class="mt-2">
          <router-link to="/register">Register</router-link>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import router from '@/router/index'
import { useAuthStore } from '@/stores/auth'
import { ref } from 'vue';
import { toast } from "vue3-toastify";
import "vue3-toastify/dist/index.css";
import { decodeCredential } from 'vue3-google-login';

export default {
  setup() {
    const authStore = useAuthStore();
    const username = ref('');
    const password = ref('');

    const login = async () => {
      try {
        if (await authStore.login(username.value, password.value)) {
          router.push({ name: 'home' });
          toast.success("Login successful");
        } else {
          toast.error("Incorrect credentials");
        }
      } catch (error) {
        console.error("Error during login:", error);
      }
    };

    return { authStore, username, password, login };
  },
  data() {
    return {
      callback: function(response) {
        console.log("login success");
        let user = decodeCredential(response.credential);
        console.log(user);
      }
    }
  }
};
</script>

<style scoped>
/* Styles specific to this component */
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
