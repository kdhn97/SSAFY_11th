<!-- <template>을 하나만 포함할 수 있음 -->
<template>
    <div>
        <p class="greeting">{{ msg }}</p>
    </div>
</template>

<!-- setup() 함수 사용하며 인스턴스 실행 -->
<!-- 
    변수 및 함수는 동일한 컴포넌트의 
    템플릿에서 자동으로 사용 가능 
-->
<script setup>
import { ref } from 'vue'
const msg = ref('Hello World')
</script>

<!-- CSS는 현재 컴포넌트에만 적용 -->
<style scoped>
.greeting {
    color: crimson;
}
</style>
