<template>
    <h1 id="title">日記を削除する</h1>

    <ul v-for="( day, index ) in day">
        <button id="tile" @click="DEL(day, title[index])">
            {{ box[index] }} <br>
            {{ title[index] }}
        </button>
    </ul>

    <button type="submit" id="homeBtn" @click="HOME()">TOP</button>
</template>

<script setup>
import { useRouter } from 'vue-router'
import { ref, onMounted } from 'vue'
import axios from 'axios'

const router = useRouter()
const HOME = () => {
    router.push('/')
}

const day = ref([])
const box = ref([])
const title = ref([])
const DEL = async(day, title) =>{
    await axios.post('http://localhost:8000/delete', {
        day: day,
        title: title,
    })
    .then((res) => {
        console.log(res.data.msg)
        location.reload()
    });

}

onMounted(() => {
    axios.get('http://localhost:8000/get')
    .then((res) => {
        day.value = res.data.day
        title.value = res.data.title

        for(let i = 0; i < day.value.length; i++) {
            var tmp = day.value[i].toString()
            // console.log(i, tmp)
            tmp = tmp.slice( 0, 4 ) + "年" + tmp.slice( 4, 6 ) + "月" + tmp.slice( 6, 8 ) + "日"
            box.value.push(tmp)
        }
    });
})
</script>

<style scoped>
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

#tile {
    width: 50%;
    height: 100px;
    background-color: var(--color-white);
    color: var(--color-black);
    border: 1px solid var(--color-black);
    border-radius: 8px;
    cursor: pointer;
    font-size: large;

    position: relative;
    left: 50%;
    transform: translateX(-50%);
    margin-bottom: 0%;
}
</style>