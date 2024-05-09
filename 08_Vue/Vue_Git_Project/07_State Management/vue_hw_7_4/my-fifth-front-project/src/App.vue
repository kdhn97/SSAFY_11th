<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <header>
      <nav>
        <RouterLink to="/">main</RouterLink>
      </nav>
      <h1>pinia + router 연습하기</h1>
  </header>

  <RouterView />
</template>

<style scoped>
</style>
