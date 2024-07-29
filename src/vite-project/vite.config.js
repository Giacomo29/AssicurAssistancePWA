import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import { VitePWA } from 'vite-plugin-pwa'


// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    VitePWA({
      injectRegister: 'auto',
      registerType: 'autoUpdate', //'injectManifest',
      devOptions: {
        enabled: true
      },
     
      // -----  serviceworker peronsalizzato
      // strategies: 'injectManifest',
      // srcDir: 'public',
      // filename: 'sw.js',

      manifest: {
        name: 'AssicurAssistance',
        description: 'AssicurAssistance is a simple app to manage your car insuranceeee',
        theme_color: '#ffffff',
        icons: [
          {
            src: '/img/icons/calendar.svg',
            sizes: '192x192',
            type: 'image/png'
          },
          {
            src: '/img/icons/calendar.svg',
            sizes: '512x512',
            type: 'image/png'
          }
        ]
          
      },

    })
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  },

  server: {
    host: true,
    https: false,
  }
})