<template>
    <h1 id="title">日記を書く</h1>
    <daily></daily>
    <button type="submit" id="homeBtn" @click="HOME()">TOP</button>
    
</template>

<script setup>
import daily from '../components/form-daily.vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const HOME = () => {
    router.push('/')
}

</script>


<style>
@import '../assets/main.css';

#title {
    margin-top: 3%;
    margin-bottom: 0%;
    color: var(--color-black);
    text-align: center;
    font-size: 400%;
}

#homeBtn {
    position: fixed;
    width: 80px;
    height: 80px;
    bottom: 3%;
    right: 3%;

    background-color: var(--color-orange);
    color: white;
    border: 1px solid var(--color-orange);
    border-radius: 8px;
    margin: 20px auto;
    cursor: pointer;
    font-size: large;
}
</style>

