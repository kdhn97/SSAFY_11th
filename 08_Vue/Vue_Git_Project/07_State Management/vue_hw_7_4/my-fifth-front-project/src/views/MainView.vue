<template>
    <div>
        <h3>메인 페이지</h3>
        <div v-for="balan in store.balances">
        <p>이름 : {{ balan.name }}</p>
        <p>잔고 : {{ balan.balance }}</p>
        <button @click="gobalance(balan.name)">updateBalance</button>
        <hr>
        </div>
    </div>
    
</template>

<script setup>
import { ref } from 'vue'
import { useBalanceStore  } from '@/stores/balance';
import { useRouter } from 'vue-router';
const store = useBalanceStore()
const router = useRouter()
const gobalance =  function(balan_name) {
    router.push({ name: 'update', params: {name: balan_name}})
}
</script>

<style scoped>

</style>