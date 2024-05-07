<template>
    <header>
      <h1 class="title">명함 관리 페이지</h1>
    </header>
    <main>
      <p class="pTag">명함을 관리하는 페이지입니다. 여기에 명함 목록이 표시됩니다.</p>
    </main>
    <footer>
      <p class="footer">&copy; 2023 My Business Cards</p>
    </footer>
</template>

<script setup>
import { ref } from 'vue'

</script>

<style scoped>
.title {
  margin: 0% auto;
  display: flex;
  justify-content: center;
  align-items: center;
  width: 300px;
  height: 100px;
  background-color: blue;
  text-align: center;
  color: white;
}
.pTag {
  text-align: center;
}
.footer {
    width: 100%;
    height: 50px;
    background-color: gainsboro;
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    text-align: center;
}

</style>