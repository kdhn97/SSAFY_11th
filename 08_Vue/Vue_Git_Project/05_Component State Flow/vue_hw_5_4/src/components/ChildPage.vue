<template>
    <div>
        <p>자식 페이지입니다.</p>
        <p>이름 : {{ myProp.name }}</p>
        <p>나이 : {{ myProp.age }}</p>
        <p>용돈 : {{ myProp.balance }}</p>
        <button @click="giveMeAllowance">용돈 주세요.</button>
    </div>
</template>

<script setup>

defineProps({
    myProp: Object
})

const emit = defineEmits(['giveMeAllowance'])
const giveMeAllowance = function () {
    emit('giveMeAllowance')
}
</script>

<style scoped>

</style>