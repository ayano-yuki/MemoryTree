<template>
    <button type="submit" id="returnBtn" @click="RET()">戻る</button>
    
    <h1 id="td">
        {{ day }}　{{ title }}
    </h1>

    <div id="main">
        {{ main }}
    </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
import { ref, onMounted } from 'vue'
import axios from 'axios'

const router = useRouter()
const RET = () => {
    router.push('/watch')
}

const day = ref("")
const title = ref("")
const main = ref("")

onMounted(() => {
    const path = location.pathname.split("/").slice(-2);
    const url = "http://localhost:8000/get/" + path[0] + "/" + path[1]

    axios.get(url)
    .then((res) => {
        day.value = res.data.day.toString()
        day.value = day.value.slice( 0, 4 ) + "年" + day.value.slice( 4, 6 ) + "月" + day.value.slice( 6, 8 ) + "日"
        title.value = res.data.title
        main.value = res.data.main

    });
})

</script>


<style>
@import '../assets/main.css';

#td {
    margin-top: 3%;
    margin-bottom: 0%;
    color: var(--color-black);
    font-size: 250%;
    text-align: center;
}

#main {
    margin-top: 5%;
    margin-bottom: 100px;
    width: 55%;
    vertical-align: top;
    white-space: pre-wrap;
    font-size: 150%;

    position: relative;
    left: 50%;
    transform: translateX(-50%);
}

#returnBtn {
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