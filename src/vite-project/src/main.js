import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import { createPinia } from 'pinia'
import { watch } from 'vue'
import { setHeaders } from '@/stores/auth'
import { refreshToken, startTokenRefreshTimer, stopTokenRefreshTimer } from './interceptor/axios'

import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap/dist/js/bootstrap.js';
import '@/style.css';


// AUTH
import { useAuthStore } from '@/stores/auth'

import './interceptor/axios'

// import vue3GoogleLogin from 'vue3-google-login'




const pinia = createPinia()  // Crea l'istanza di Pinia prima di creare l'applicazione

const app = createApp(App)

// app.use(vue3GoogleLogin, {
//     clientId: '1041959334619-iqa170o002jboc7hd3pquur8endahkvt.apps.googleusercontent.com'
//   })




if (localStorage.getItem('state')) {
    pinia.state.value = JSON.parse(localStorage.getItem('state'));
}

watch(
    pinia.state,
    (state) => {
        localStorage.setItem('state', JSON.stringify(state));
    },
    { deep: true }


);

app.use(router)


app.use(pinia)  // Usa Pinia nell'applicazione

const store = useAuthStore()



/////////////////


////////////////

async function initializeApp() {

    if (localStorage.getItem('user')) {
        store.authUser = JSON.parse(localStorage.getItem('user'));
        try {
            const newAccessToken = await refreshToken(); // Chiamata asincrona per il refresh del token
            if (newAccessToken) {
                // Avvia il timer di refresh del token all'avvio dell'applicazione
                setHeaders(newAccessToken);
                startTokenRefreshTimer();
            } else {
                // Se refreshToken() non restituisce un nuovo token, reindirizza alla pagina di login
                store.logout();
                app.mount('#app');
                router.push('/login');
                return;
            }
        } catch (error) {
            stopTokenRefreshTimer()
            console.error("Errore durante il refresh del token:", error);
            // Se c'è un errore nel refresh del token, reindirizza alla pagina di login
            store.logout();
            app.mount('#app');
            router.push('/login');
            return;
        }
    }
    // Monta l'applicazione solo se il token è stato ottenuto con successo
    app.mount('#app');
}

// Chiamata alla funzione di inizializzazione dell'applicazione
initializeApp();

