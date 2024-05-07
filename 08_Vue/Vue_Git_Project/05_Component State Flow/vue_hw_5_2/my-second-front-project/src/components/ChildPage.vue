<template>
    <div class="page">
        <p>자식 페이지입니다</p>
        <p>이름 : {{ myProp.name }}</p>
        <p>나이 : {{ myProp.age }}</p>
    </div>
</template>

<script setup>
import { ref } from 'vue'
defineProps({
    myProp: Object
})
</script>

<style scoped>
.page {
    margin: 1%;
    padding: 1%;
    border: 1px solid black;
}
</style>