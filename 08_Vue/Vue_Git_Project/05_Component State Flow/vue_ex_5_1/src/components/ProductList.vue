<template>
    <div>
        <li>{{ myProp.name }} - {{ myProp.price }}원</li>
    </div>
</template>

<script setup>
defineProps({
    myProp: Array,
})
</script>

<style scoped>

</style>