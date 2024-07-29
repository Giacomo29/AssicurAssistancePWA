
<template>
  <!DOCTYPE html>
  
  <header>
    <div id="nav">
    <NavbarComponent />
    </div>
    <div class = "container">
      <RouterView/>
    </div>
  </header>
</template>


<script>
import { RouterLink, RouterView } from 'vue-router';
import NavbarComponent from '@/components/NavbarComponent.vue';
export default {
  name: 'App',
  components: {
    NavbarComponent,
  }
}
</script>
