<template>
    <div>
        <h1>학생 상세 정보 목록입니다</h1>
        <p v-for="name in names" @click="detail(name.name)">{{ name.name }} 학생 정보 보기</p>
    </div>
</template>

<script setup>
import { useRouter } from 'vue-router';
import { ref } from 'vue'

const router = useRouter()
const names = ref([
  { name: '김하나' },
  { name: '김두리' },
  { name: '김서이' },
])

const detail = function (num) {
  router.push({ name: 'studentdetail', params: { name: num } })
}
</script>

<style scoped>

</style>