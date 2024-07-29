// Importa i moduli necessari
import { cleanupOutdatedCaches, precacheAndRoute } from 'workbox-precaching';
import { clientsClaim, setCacheNameDetails } from 'workbox-core';
import { registerRoute } from 'workbox-routing';
import { NetworkFirst, CacheFirst } from 'workbox-strategies';
import { CacheableResponsePlugin } from 'workbox-cacheable-response';
import { ExpirationPlugin } from 'workbox-expiration';


// Imposta i dettagli della cache
setCacheNameDetails({
  prefix: 'my-cache',
  suffix: 'v1',
  precache: 'precache',
  runtime: 'runtime',
});

// Pulisci le cache obsolete
cleanupOutdatedCaches();

// Precarica e instrada le risorse specificate nel manifest
precacheAndRoute(self.__WB_MANIFEST);

// Attiva il service worker senza aspettare che la pagina venga ricaricata
self.addEventListener('install', (event) => {
  console.log('Service worker installato');
  event.waitUntil(self.skipWaiting());
});

self.addEventListener('activate', (event) => {
  event.waitUntil(clientsClaim());
});

// Registra una route per gestire le richieste di navigazione e restituire la pagina di fallback Vue
registerRoute(
  ({ event }) => event.request.mode === 'navigate',
  async (args) => {
    // Verifica lo stato della connessione
    if (!navigator.onLine) {
      // Se il browser è offline, restituisci la pagina offline
      console.log('Il browser è offline. Caricamento della pagina offline.');
      return fetch('/offline.html');
    }

    // Se il browser è online, prova a caricare la risorsa di navigazione dalla rete
    // Utilizza la strategia NetworkFirst per cercare nella rete
    const strategy = new NetworkFirst({
      cacheName: 'my-navigation-cache',
      plugins: [
        // Configura il plugin di risposta cacheable
        new CacheableResponsePlugin({
          statuses: [200], // Considera solo le risposte con stato 200 come cacheable
        }),
        // Configura il plugin di scadenza per rimuovere le risposte vecchie dalla cache
        new ExpirationPlugin({
          maxEntries: 10, // Massimo numero di elementi da mantenere in cache
          maxAgeSeconds: 24 * 60 * 60, // Durata massima della cache in secondi (1 giorno)
        }),
      ],
    });

    try {
      // Prova a caricare la risorsa di navigazione dalla rete
      const response = await strategy.handle(args);
      // Se la risorsa è disponibile, restituiscila
      if (response) {
        return response;
      }
    } catch (error) {
      // Se c'è un errore durante il caricamento della risorsa di navigazione dalla rete,
      // restituisci la pagina offline
      console.log('Il browser è offline. Caricamento della pagina offline.');
      return fetch('/fallback_page.html');
    }
  }
);