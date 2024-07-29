import { defineStore } from 'pinia';
import axios from 'axios';
import { startTokenRefreshTimer, stopTokenRefreshTimer } from '../interceptor/axios';
import { toast } from "vue3-toastify";
import "vue3-toastify/dist/index.css";


const INTERVALLO_REFRESH = 400000; // secondi in millisecondi

export function setHeaders(token) { // Imposta gli header di autorizzazione
    if (!token) { // Se non è stato fornito un token
        delete axios.defaults.headers.common['Authorization']; // Rimuovi l'header di autorizzazione
    } else {
        axios.defaults.headers.common['Authorization'] = `Bearer ${token}`; //altrimenti imposta l'header di autorizzazione
    }
}




export const useAuthStore = defineStore('auth', {
    state: () => ({
        authUser: null, // Utente autenticato 
        notifications: [], // Notifiche dell'utente
    }),


    getters: {
        // Restituisce l'utente autenticato
        isAuthenticated: (state) => !!state.getUser, // Restituisce true se l'utente è autenticato
        getUser: (state) => state.authUser, // Restituisce i dati dell'utente
    },

  

    actions: {

        updateAuthUser(user) { // Aggiorna l'utente autenticato
            this.authUser = user;
        },

        pushNotification(notification) { // Aggiunge una notifica 
            this.notifications.push(notification);
        },


        removeNotification(notificationData) {
            console.log(notificationData);
            this.notifications = this.notifications.filter(notification => notification['polizza'] !== notificationData);
        },

        



        // Funzione per eseguire il login
        async login(username, password) {
            const authStore = useAuthStore()

            setHeaders(); //rimuovi gli headers di autorizzazione
            try {
                const response = await axios.post('/api/entra/', { //invia la richiesta di login
                    username: username, //parametri della richiesta
                    password: password,
                },
                    {
                        headers: { // Rimuovi tutti gli header

                        }
                    });

                this.authUser = response.data; //imposta l'utente
                setHeaders(response.data.access); //imposta gli headers di autorizzazione
                startTokenRefreshTimer(); //avvia il timer di refresh del token
                localStorage.setItem('user', JSON.stringify(response.data)); //salva l'utente nel local storage
                //authStore.setUser(response.data);
                localStorage.setItem('refresh', JSON.stringify(response.data.refresh)); //salva il token di refresh nel local storage
                return true;
            } catch (error) {
                if (error.response && error.response.data) {
                    const errori = error.response.data;
                    Object.keys(errori).forEach((campo) => {
                        errori[campo].forEach((messaggio) => {
                            toast.error(`${messaggio}`);
                        });
                    });
                } else {
                    toast.error("Errore durante il login");
                }
                return false;
            }


        },

        async logout() {
            try {
                const response = await axios.post('/api/esci/'); //invia la richiesta di logout
                this.authUser = null; //rimuove l'utente
                setHeaders(); //rimuove gli headers di autorizzazione
                //localStorage.removeItem('user.user'); //rimuove l'utente
                localStorage.removeItem('user'); //rimuove il token di refresh
                localStorage.removeItem('refresh'); //rimuove il token di refresh
                setHeaders(); //rimuove gli headers di autorizzazione
                stopTokenRefreshTimer(); //stoppa il timer di refresh del token
                return response;
            } catch (error) {
                if (error.response && error.response.data) {
                    const errori = error.response.data;
                    Object.keys(errori).forEach((campo) => {
                        errori[campo].forEach((messaggio) => {
                            toast.error(`${campo}: ${messaggio}`);
                        });
                    });
                } else {
                    toast.error("Errore durante il logout.");
                }
            }
        },



        // Registra un nuovo utente
        async register(username, password, email, nome, cognome) {
            try {
                const response = await axios.post('/api/register/', {  //invia la richiesta di registrazione
                    username: username, //parametri della richiesta
                    nome: nome,
                    cognome: cognome,
                    password: password,
                    email: email,
                });
                this.user = response.data; //imposta l'utente
                this.authUser = response.data; //imposta l'utente
                localStorage.setItem('user', JSON.stringify(response.data)); //salva l'utente nel local storage
                setHeaders(response.data.token); //imposta gli headers di autorizzazione
                localStorage.setItem('refresh', JSON.stringify(response.data.refresh)); //salva il token di refresh nel local storage
                startTokenRefreshTimer(); //avvia il timer di refresh del token
                return true;
            } catch (error) {
                if (error.response && error.response.data) {
                    const errori = error.response.data;
                    Object.keys(errori).forEach((campo) => {
                        errori[campo].forEach((messaggio) => {
                            toast.error(`${messaggio}`);
                        });
                    });
                } else {
                    toast.error("Errore registrazione utente");
                }
                return false;
            }
        },




    }



});

