<template>
    <!-- Show login link if user is not authenticated -->
    <div v-if="!this.authStore.isAuthenticated">
        <!-- Redirect to login -->
        <router-link to="/login">Login</router-link>
    </div>
    <!-- Main container -->
    <div class="container bootstrap snippets bootdey mt-5">
        <!-- Header -->
        <h1 class="text-primary">Modifica Profilo</h1>
        <hr>
        <div class="row">
            <!-- Left column -->
            <div class="col-md-3">
                <div class="text-center mt-2">
                    <div class="container_foto shadow">
                        <div class="image-wrapper_foto">
                            <!-- Show user avatar if available -->
                            <div v-if="authStore.authUser.user != null">
                                <img class="avatar-image" :src=authStore.authUser.user.avatar alt="">
                            </div>
                        </div>
                    </div>
                    <h6>Carica una foto differente...</h6>
                    <!-- Image uploader component -->
                    <ImageUploader @updateUserData="getAccount" />
                </div>
            </div>
            <!-- Right column -->
            <div class="col-md-9">
                <!-- Form for user details -->
                <div class="form-group">
                    <label class="col-lg-3 control-label">Username:</label>
                    <div class="col-lg-8">
                        <input class="form-control" type="text" v-model="user.username">
                    </div>
                </div>
                <div class="form-group">
                    <label class="col-lg-3 control-label">Nome:</label>
                    <div class="col-lg-8">
                        <input class="form-control" type="text" v-model="user.nome">
                    </div>
                </div>
                <div class="form-group">
                    <label class="col-lg-3 control-label">Cognome:</label>
                    <div class="col-lg-8">
                        <input class="form-control" type="text" v-model="user.cognome">
                    </div>
                </div>
                <div class="form-group">
                    <label class="col-lg-3 control-label">Email:</label>
                    <div class="col-lg-8">
                        <input class="form-control" type="text" v-model="user.email">
                    </div>
                </div>
                <!-- Button to trigger password popup -->
                <div>
                    <button class="btn btn-primary mb-2 mt-2 " @click="openPasswordPopup">Modifica Password</button>
                    <!-- Password popup component -->
                    <PasswordPopup :id_account="id" :isOpen="isPasswordPopupOpen"
                        @closePopup="isPasswordPopupOpen = false">
                    </PasswordPopup>
                </div>
            </div>
        </div>
        <!-- Buttons for actions -->
        <div>
            <div class="d-flex justify-content-end mt-5">
                <button class="btn btn-primary" @click="openPasswordConfirmationModal">Modifica</button>
                <button type="button" @click="logout" class="btn btn-danger mx-2">Logout</button>
            </div>
        </div>
        <!-- Password confirmation modal component -->
        <div>
            <password-confirmation-modal ref="passwordConfirmationModal" @password-confirmed="modifyAccount"
                @cancel="closePasswordConfirmationModal">
            </password-confirmation-modal>
        </div>
        <hr>
    </div>
</template>


<script>
import { axios } from "@/common/api.service.js";
import { endpoints } from "@/common/endpoints.js";
import router from "../router";
import { useAuthStore } from '@/stores/auth';
import { toast } from "vue3-toastify";
import "vue3-toastify/dist/index.css";
import PasswordConfirmationModal from '@/components/PasswordConfirmationModal.vue';
import ImageUploader from '@/components/ImageUploader.vue';
import PasswordPopup from '@/components/PasswordPopup.vue';

export default {
    components: {
        PasswordPopup
    },
    name: 'accountView',
    props: {
        nome: {
            type: String,
        }
    },
    setup() {
        const authStore = useAuthStore();
        return { authStore };
    },
    data() {
        return {
            showPasswordConfirmationModal: false,
            user: {},
            isPasswordPopupOpen: false,
            id: 0,
        }
    },
    methods: {
        // Method to open password popup
        openPasswordPopup() {
            this.isPasswordPopupOpen = true;
        },
        // Method to fetch user data
        getImage(imagePath) {
            return require(imagePath);
        },
        fetchUserData() {
            this.$refs.userProfileView.fetchUserData();
        },
        // Method to open password confirmation modal
        openPasswordConfirmationModal() {
            if (this.$refs.passwordConfirmationModal) {
                this.$refs.passwordConfirmationModal.open();
            }
        },
        // Method to close password confirmation modal
        closePasswordConfirmationModal() {
            if (this.$refs.passwordConfirmationModal) {
                this.$refs.passwordConfirmationModal.close();
            }
        },
        // Method to reset password
        async resetPassword() {
            try {
                const endpoint = `${endpoints["resetPassword"]}`;
                const response = await axios.post(endpoint, { "email": this.user.email });
                this.user = response.data;
                console.log(this.user);
                toast.info("Email per il recupero della password inviata ");
            } catch (error) {
                console.log(error);
            }
        },
        // Method to logout user
        logout() {
            if (this.authStore.isAuthenticated) {
                this.authStore.logout();
                router.push({ name: 'login' });
            }
        },
        // Method to get account details
        async getAccount() {
            try {
                const endpoint = `${endpoints["account"]}`;
                const response = await axios.get(endpoint);
                this.user = response.data;
                this.authStore.authUser.user = this.user;
                this.id = this.user.id;
            } catch (error) {
                console.log(error);
            }
        },
        // Method to modify account details
        async modifyAccount(password) {
            try {
                const endpoint = `${endpoints["modifyAccount"]}`;
                const formData = new FormData();
                formData.append('username', this.user.username);
                formData.append('nome', this.user.nome);
                formData.append('cognome', this.user.cognome);
                formData.append('email', this.user.email);
                formData.append('password', password);
                const response = await axios.put(endpoint, formData, {
                    headers: {
                        'Content-Type': 'multipart/form-data',
                    },
                });
                console.log(this.user);
                toast.success("Dati modificati con successo");
                this.getAccount();
            } catch (error) {
                console.log(error);
                toast.error("Errore nella modifica dei dati");
            }
        },
    },
    created() {
        this.getAccount();
    },
    watch: {
        $route(to, from) {
            this.getAccount();
            this.userStore.user
        },
        'authStore.user': {
            handler(newVal) {
                if (newVal) {
                    this.user.avatar = newVal.avatar;
                }
            },
            deep: true
        }
    },
    components: {
        PasswordConfirmationModal,
        ImageUploader,
        PasswordPopup
    },
}
</script>


<style>
.container_foto {
    background-color: #cfcfcf;
    max-width: 300px;
    margin: 0 auto;
    overflow: hidden;
    margin-bottom: 20px;
    border-style: solid;
    border-color: azure;
    border-radius: 10%;
}

.image-wrapper_foto {
    width: 100%;
    height: 0;
    padding-top: 100%;
    position: relative;
}

.image-wrapper_foto img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    position: absolute;
    top: 0;
    left: 0;
}
</style>
