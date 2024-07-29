<template>
    <!-- Card container for password reset -->
    <div class="card mx-auto text-center mt-5" style="width: 300px;">
        <!-- Card header -->
        <div class="card-header h5 text-white bg-primary">Password Reset</div>
        <!-- Card body -->
        <div class="card-body px-5">
            <!-- Card text -->
            <p class="card-text py-2">
                Inserisci l'email associata al tuo account per reimpostare la password, se l'email esiste verrà inviata una email con le istruzioni per il reset.
            </p>
            <!-- Reset password form -->
            <form @submit.prevent="resetPassword">
                <div class="form-outline">
                    <!-- Email input -->
                    <input type="email" id="typeEmail" class="form-control my-3" v-model="email" name="email" required>
                    <label class="form-label" for="typeEmail">Email input</label>
                </div>
                <!-- Submit button -->
                <button type="submit" class="btn btn-primary w-100" id="email" :disabled="buttonDisabled">Reset password</button>
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
import { useAuthStore } from '@/stores/auth'
import { axios } from "@/common/api.service.js";
import { endpoints } from "@/common/endpoints.js";
import router from "@/router";
import { toast } from "vue3-toastify";
import "vue3-toastify/dist/index.css";

export default {
    setup() {
        const authStore = useAuthStore();
        return { authStore };
    },
    name: 'ResetPasswordView',
    components: {

    },
    props: [],
    data() {
        return {
            email: '',
            buttonDisabled: false,
        }
    },
    methods: {
        // Function to reset password
        async resetPassword() {
            try {
                const endpoint = `${endpoints["resetPassword"]}`;
                const response = await axios.post(endpoint, {
                    email: this.email,
                });
                console.log(response);
                toast.info("Email inviata con successo.");
                // Disable button for 30 seconds after submission
                this.buttonDisabled = true;
                setTimeout(() => {
                    this.buttonDisabled = false;
                }, 30000);
            } catch (error) {
                // Handle error
                toast.info("Email inviata con successo.");
                console.log(error);
            }
        }
    },
    computed: {

    },
    mounted() {

    },
    watch: {

    }
}
</script>
