<template>
    <button>게시글 생성</button>
</template>

<script setup>
import axios from 'axios'
import { onMounted } from 'vue';
import { useArticleStore } from '@/stores/articles'
const store = useArticleStore()

onMounted(() => {
  axios({
    method: 'get',
    url: `http://127.0.0.1:8000/api/v1/articles/`,
  })
  .then((response) => {
    console.log(response.data)
  })
  .catch((error) => {
    console.log(error);
  })
})
</script>

<style lang="scss" scoped>

</style>