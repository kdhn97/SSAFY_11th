<template>
    <div>
        <h1>부모 페이지입니다</h1>
        <ChildPage
        v-for="item in items"
        :my-prop="item"
        @give-me-allowance="updateBalance(item)"
        />
    </div>
</template>

<script setup>
import { ref } from 'vue'
const items = ref([
    { name: '김하나', age: 30, balance: 100000 },
    { name: '김두리', age: 20, balance: 10000 },
    { name: '김서이', age: 10, balance: 1000 }
])

import ChildPage from '@/components/ChildPage.vue';

const updateBalance = function (item) {
    item.balance += 1000
}
</script>

<style scoped>
</style>