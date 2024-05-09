<script setup>
  import { RouterLink, RouterView } from 'vue-router'

</script>

<template>
  <header>
      <nav class="navbar">
        <RouterLink to="/" class="nav">Home</RouterLink>
        <RouterLink to="/products" class="nav">Products</RouterLink>
        <RouterLink to="/favorite" class="nav">Favorite</RouterLink>
      </nav>
  </header>

  <RouterView />
</template>

<style scoped>
.navbar {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 50px;
  background-color: black;
}
.nav {
  margin: 10px;
  color: white;
  text-decoration: none;
}
</style>
