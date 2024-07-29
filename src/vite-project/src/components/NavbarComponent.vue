<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <div class="container">
      <router-link :to="{ name: 'home' }" class="navbar-brand">AssicurAssistance</router-link>

      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarText">
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse" id="navbarText">
        <ul class="navbar-nav ms-auto mb-2 mb-lg-0 mt-2">
          <li v-if="!authStore.authUser" class="nav-item">
            <router-link :to="{ name: 'login' }" class="nav-link btn btn-primary ms-1">Login</router-link>
          </li>
          <li v-else class="nav-item d-flex align-items-center ms-1">
            <router-link :to="{ name: 'account-view' }" class="nav-link">
              <!-- Codice dell'account -->
              <div v-if="authStore.authUser != null">
                <div class="avatar-container">
                  <div v-if="authStore.authUser.user.avatar != null">
                    <img :src="authStore.authUser.user.avatar" alt="User Avatar" class="avatar_image">
                  </div>
                  <div v-else>
                    <button class="btn btn-primary">{{ authStore.authUser.user.username }}</button>
                  </div>
                </div>
              </div>

            </router-link>

            <!-- Sezione delle notifiche -->
          <li v-if="authStore.notifications.length > 0" class="nav-item dropdown ms-auto" style="padding-right: 10px">
            <a @click.prevent class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button"
              data-bs-toggle="dropdown" aria-expanded="false">
              <svg class="icon_add_nav" fill="#000000" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                <g id="SVGRepo_bgCarrier" stroke-width="0"></g>
                <g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g>
                <g id="SVGRepo_iconCarrier">
                  <path
                    d="M10,20h4a2,2,0,0,1-4,0Zm8-4V10a6,6,0,0,0-5-5.91V3a1,1,0,0,0-2,0V4.09A6,6,0,0,0,6,10v6L4,18H20Z">
                  </path>
                </g>
              </svg>
              <span class="badge bg-danger">{{ authStore.notifications.length }}</span>
            </a>
            <ul class="dropdown-menu notification-menu" aria-labelledby="navbarDropdown"
              style="width: 300px; max-height: 500px; overflow-y: auto;">
              <!-- Imposta la larghezza desiderata (es. 30rem) e le altre proprietà di stile -->
              <li v-for="(notification, index) in authStore.notifications" :key="index">
                <!-- Card delle notifiche -->
                <div class="card w-100">
                  <div class="card-body">
                    <h5 class="card-title">{{ notification.cliente }}</h5>
                    <p class="card-text">La polizza n.{{ notification.polizza }} è in scadenza</p>
                    <button @click="openNotification(notification.polizza)" class="btn btn-primary">Visualizza</button>
                  </div>
                </div>
              </li>
            </ul>
          </li>
          <!-- Icona del pulsante Logout  -->
          <li class="nav-item">
            <svg @click="logout" class="icon_add_nav" viewBox="0 0 24 24" fill="none"
              xmlns="http://www.w3.org/2000/svg">
              <g id="SVGRepo_bgCarrier" stroke-width="0"></g>
              <g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g>
              <g id="SVGRepo_iconCarrier">
                <path
                  d="M17.2929 14.2929C16.9024 14.6834 16.9024 15.3166 17.2929 15.7071C17.6834 16.0976 18.3166 16.0976 18.7071 15.7071L21.6201 12.7941C21.6351 12.7791 21.6497 12.7637 21.6637 12.748C21.87 12.5648 22 12.2976 22 12C22 11.7024 21.87 11.4352 21.6637 11.252C21.6497 11.2363 21.6351 11.2209 21.6201 11.2059L18.7071 8.29289C18.3166 7.90237 17.6834 7.90237 17.2929 8.29289C16.9024 8.68342 16.9024 9.31658 17.2929 9.70711L18.5858 11H13C12.4477 11 12 11.4477 12 12C12 12.5523 12.4477 13 13 13H18.5858L17.2929 14.2929Z"
                  fill="#000000"></path>
                <path
                  d="M5 2C3.34315 2 2 3.34315 2 5V19C2 20.6569 3.34315 22 5 22H14.5C15.8807 22 17 20.8807 17 19.5V16.7326C16.8519 16.647 16.7125 16.5409 16.5858 16.4142C15.9314 15.7598 15.8253 14.7649 16.2674 14H13C11.8954 14 11 13.1046 11 12C11 10.8954 11.8954 10 13 10H16.2674C15.8253 9.23514 15.9314 8.24015 16.5858 7.58579C16.7125 7.4591 16.8519 7.35296 17 7.26738V4.5C17 3.11929 15.8807 2 14.5 2H5Z"
                  fill="#000000"></path>
              </g>
            </svg>
          </li>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>



<script>

import { useAuthStore } from '@/stores/auth'
import router from '@/router/index'
import WebSocketInstance from '@/components/websocket';

export default {
  setup() {
    const authStore = useAuthStore();
    return { authStore };
  },
  name: 'NavbarComponent',
  data() {
    return {
      user: {},
    }
  },
  methods: {
    getUser() {
      const user = JSON.parse(localStorage.getItem('user'))
      this.user = user
      console.log(this.user)
    },

    logout() {
      if (this.authStore.isAuthenticated) {
        this.authStore.logout();
        router.push({ name: 'login' });
      }
    },

    requestNotificationPermission() {
      Notification.requestPermission().then(permission => {
        if (permission === 'granted') {
          console.log('Permission for notifications granted!');
        } else {
          console.warn('Permission for notifications denied!');
        }
      });
    },

    showNotification(polizzaId, cliente) {
      const title = cliente;

      const options = {
        body: `Polizza in scadenza: ${polizzaId} per il cliente ${cliente}`,
      };
      new Notification(title, options);
    },

    updateNotifications(data) {
      const parsedData = JSON.parse(data);
      const user = JSON.parse(localStorage.getItem('user'));

      if (parsedData.payload && parsedData.payload.account.username == user.user.username && parsedData.payload.current_notification) {

        const polizzaId = parsedData.payload.polizza
        const cliente = parsedData.payload.cliente

        //this.notifications.push(polizzaId);
        this.authStore.pushNotification({ polizza: polizzaId, cliente: cliente });
        this.showNotification(polizzaId, cliente); // Visualizza la notifica quando arriva

      }
    },

    openNotification(notification) {
      router.push({ name: 'polizza-view', params: { id: notification } });
      this.authStore.removeNotification(notification);
    }

  },

  created() {
    this.requestNotificationPermission();
  },

  mounted() {
    WebSocketInstance.connect();
    WebSocketInstance.listenForNotifications(this.updateNotifications);
  },

  watch() {

  },


}

</script>


<style scoped>
.notification-menu {
  max-height: 500px;
  /* Altezza massima della sezione delle notifiche */
  overflow-y: auto;
  /* Abilita lo scorrimento verticale */
}
</style>
