<template>
    <div>
        <h3>자식 페이지</h3>
        {{ child.name }}
    </div>
</template>

<script setup>
import { ref } from 'vue'
defineProps({
    child: Object
})
</script>

<style scoped>

</style>