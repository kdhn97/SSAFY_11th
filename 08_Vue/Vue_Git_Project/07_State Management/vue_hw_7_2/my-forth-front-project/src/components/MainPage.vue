<template>
    <div >
        <h1>pinia 연습하기</h1>
        <ParentPage
        v-for="family in store.familyinfo"
        :family="family"
        class="txt"
        />
        
    </div>
</template>

<script setup>
import { ref } from 'vue'
import { useFamilyStore } from '@/stores/family'
import ParentPage from './ParentPage.vue';

const store = useFamilyStore()
</script>

<style scoped>
.txt {
  text-align: center;
}
</style>