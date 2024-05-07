<template>
    <div class="Ppage">
        <h1>부모 페이지입니다.</h1>
        <ChildPage
        v-for="item in items"
        :my-prop="item"/>
    </div>
</template>

<script setup>
import { ref } from 'vue'
const items = ref([
    { name:'김하나', age: 30 },    
    { name:'김두리', age: 20 },    
    { name:'김서이', age: 10 },    
])
import ChildPage from '@/components/ChildPage.vue'
</script>

<style scoped>
.Ppage {
    padding: 1%;
    border: 1px solid black;
}
</style>