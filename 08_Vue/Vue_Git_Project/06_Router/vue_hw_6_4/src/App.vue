<script setup>
import { RouterLink, RouterView } from 'vue-router'
import MainPage from '@/components/MainPage.vue'
</script>

<template>
  <header>
    <div class="wrapper">
      <MainPage />
      <nav>
        <!-- <RouterLink to="/"></RouterLink> -->
        <RouterLink to="/">Some</RouterLink>
        |
        <RouterLink to="/other">Other</RouterLink>
        |
        <RouterLink to="/students">Students</RouterLink>
      </nav>
    </div>
  </header>
  <RouterView />
</template>

<style scoped>

</style>
