<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <header>
    <div class="wrapper">
      <nav>
        <RouterLink to="/">Home</RouterLink> | 
        <RouterLink :to="{ name: 'SignUpView' }">회원가입</RouterLink> |
        <RouterLink :to="{ name: 'LogInView' }">로그인</RouterLink> 
      </nav>
    </div>
  </header>

  <RouterView />
</template>

<style scoped>
</style>
