<template>
    <div>
        <h1>데이터 수정 페이지</h1>
        <p>이름 : {{ userName }}</p>
        <p>잔고 : {{ store.getbalance(userName).balance }}</p>
        <button>+</button>
    </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRoute } from 'vue-router';
import { useBalanceStore } from '@/stores/balance' 
const route = useRoute()
const userName = ref(route.params.name)
const store = useBalanceStore()
</script>

<style scoped>

</style>