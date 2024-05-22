<template>
    <ul v-for="( day, index ) in day">
        <button id="tile" @click="router.push('/' + root + '/' + day + '/' + title[index])">
            {{ box[index] }} <br>
            {{ title[index] }}
        </button>
    </ul>
</template>

<script setup>
import { useRouter } from 'vue-router'
import { ref, onMounted } from 'vue'
import axios from 'axios'

defineProps(["root"])

const router = useRouter()
const day = ref([])
const box = ref([])
const title = ref([])

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