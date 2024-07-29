import axios from 'axios';
import { setHeaders, useAuthStore } from '@/stores/auth';
import router from '../router';;




const INTERVALLO_REFRESH = 40000; // secondi in millisecondi

let isRefreshing = false;

// Funzione per eseguire il refresh del token
export async function refreshToken() {
    try {
        // Recupera il refresh token dal local storage e rimuove le virgolette
        const refresh = localStorage.getItem('refresh');
        if (refresh) {
            try {
                const response = await axios.post('/api/token/refresh/', {
                    refresh: refresh.replace(/"/g, ''),
                });

                const { access, refresh: newRefreshToken } = response.data;
                localStorage.setItem('refresh', JSON.stringify(newRefreshToken));
                //console.log('Token di accesso aggiornato:', access);
                return access;
            } catch (error) {
                console.error('Errore durante il refresh del token:', error);
                //logout();
                throw error; // Lascia che l'interceptor gestisca il reindirizzamento alla pagina di login
            }
        }
    } catch (error) {
        console.error('Errore durante il refresh del token:', error);
        //logout();
        throw error; // Lascia che l'interceptor gestisca il reindirizzamento alla pagina di login
    }
}

//Interceptor per gestire le risposte 401 (Non autorizzato)
axios.interceptors.response.use(
    response => response,
    async error => {
        const originalRequest = error.config;
        if (error.response.status === 401 && !originalRequest._retry) {
            if (!isRefreshing) {
                isRefreshing = true;
                try {
                    const newAccessToken = await refreshToken();
                    if (newAccessToken) {
                        setHeaders(newAccessToken);
                        originalRequest._retry = true;
                        return axios(originalRequest);
                    }
                } catch (refreshError) {
                    console.error('Errore durante il refresh del token:', refreshError);
                } finally {
                    isRefreshing = false;
                }
            }
        }
        return Promise.reject(error);
    }
);


let tokenRefreshTimer = null;
let elapsedTime = 0;

export function startTokenRefreshTimer() {
    // Avvia il setInterval per il refresh del token
    tokenRefreshTimer = setInterval(async () => {
        try {
            const token = await refreshToken();
            if (token) {
                setHeaders(token);
            }
        } catch (error) {
            console.error('Errore durante il refresh del token:', error);
        }
    }, INTERVALLO_REFRESH)
    return () => clearInterval(tokenRefreshTimer);
}


export function stopTokenRefreshTimer() {
    clearInterval(tokenRefreshTimer);
}