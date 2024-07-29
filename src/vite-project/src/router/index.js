import { createRouter, createWebHistory } from 'vue-router'
import axios from 'axios'
import { useAuthStore } from '@/stores/auth'
import config from '@/config.js'


axios.defaults.baseURL = config.backendUrl;

const router = createRouter({
  history: createWebHistory(),

  routes: [

    {
      path: '/',
      name: 'Home',
      component: () => import("@/views/HomeView.vue"),
    },

    {
      path: '/home',
      name: 'home',
      component: () => import("@/views/HomeView.vue"),
    },

    {
      path: '/login',
      name: 'login',
      component: () => import("@/views/auth/LoginView.vue")
    },

    {
      path: '/register',
      name: 'register',
      component: () => import("@/views/auth/RegisterView.vue")
    },

    {
      path: '/reset-password/',
      name: 'reset-password',
      component: () => import("@/views/auth/ResetPasswordView.vue")
    },
    
    {
      path: '/new-password/:userId/:token',
      name: 'new-password',
      component: () => import("@/views/auth/newPasswordPage.vue"),
      props: true, 
    },

    //AUTH
    {
      path: '/auth/login',
      name: 'loginToken',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('@/views/auth/LoginView.vue')
    },
    

    {
      path: '/register',
      name: 'register',
      component: () => import('@/views/auth/RegisterView.vue')
    },

    {
      path: "/compagnia/:nome",
      name: "compagnia-view",
      component: () => import("../views/compagniaView.vue"),
      props: true,
    },

    {
      path: "/scadenze/",
      name: "scadenze-view",
      component: () => import("../views/ScadenzeView.vue"),
      props: true,
    },

    {
      path: "/clienti/",
      name: "clienti-view",
      component: () => import("../views/clientiView.vue"),
      meta: { requiresAuth: true } ,
      props: true,
    },

    {
      path: "/cliente/:id?",
      name: "cliente-view",
      component: () => import("../views/clienteView.vue"),
      props: true,
    },

    {
      path: "/nuovo-cliente/",
      name: "nuovo-cliente-view",
      component: () => import("../views/newClienteView.vue"),
    },

    {
      path: "/polizza/:id",
      name: "polizza-view",
      component: () => import("../views/polizzaView.vue"),
      props: true,
    },

    {
      path: "/nuova-polizza/:id?",
      name: "nuova-polizza-view",
      component: () => import("../views/newPolizzaView.vue"),
      props: true,
    },

    {
      path: "/veicolo/:targa",
      name: "veicolo-view",
      component: () => import("../views/veicoloView.vue"),
      props: true,
    },


    {
      path: "/account/",
      name: "account-view",
      component: () => import("../views/accountView.vue"),
      props: true,

    },


    {
      path : "/password-reset",
      name : "password-reset",
      component: () => import("../views/auth/passwordResetView.vue"),
      props: route => ({ uid: route.query.uidb64, token: route.query.token })
    },

    {
      path: '/offlineView',
      name: 'offlineView',
      component: () => import('../views/offlineView.vue'),
    }


  ]

})

router.beforeEach(async (to, from) => {
  if (!navigator.onLine && to.path !== '/offlineView') {
    // redirect the user to the offline page
    return { name: 'offlineView' }
  }
  const store = await useAuthStore()
  // if the route requires auth and the user is not authenticated, redirect to login page
  if (!store.isAuthenticated && to.name !== 'login' && to.name !== 'register' && to.name !== 'home' && to.name !== 'password-reset' && to.name !== 'new-password' && to.name !== 'reset-password') {
    // redirect the user to the login page
    return { name: 'login' }
  }
})

const DEFAULT_TITLE = 'AssicurAssistance';
router.afterEach((to, from) => {
  document.title = to.meta.title || DEFAULT_TITLE;
});
  

export default router
