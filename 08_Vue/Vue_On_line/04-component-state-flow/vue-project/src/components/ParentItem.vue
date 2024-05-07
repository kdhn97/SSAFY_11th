<template>
    <div>
        <p>{{ myProp.id }}</p>
        <p>{{ myProp.name }}</p>
    </div>
</template>

<script setup>
import { ref } from 'vue'
defineProps({
    myProp: Object
})
</script>

<style scoped>

</style>