<template>
    <h1 id="td">
        {{ hday }}　{{ htitle }}
    </h1>

    <form id="daily" name="daily" @submit.prevent="mail" autocomplete="off">
        <div>
            　日付　：<input type="date" v-model="day" id="line" required />
        </div>

        <div>
            タイトル：<input type="text" v-model="title" id="line" required />
        </div>

        <div>
            <br>日記<br>
            <textarea id="long" v-model="main" required />
        </div>

        <div>
            <button type="submit" id="button">決定</button>
        </div>
    </form>

</template>

<script setup>
import { useRouter } from 'vue-router'
import { ref, onMounted } from 'vue'
import axios from 'axios'

const router = useRouter()

const day = ref(0)
const title = ref("")
const main = ref("")
const hday = ref("")
const htitle = ref("")

const mail = async () => {
    var date = day.value.replace(/-/g, "");
    // console.log(date, title.value, main.value)

    await axios.post('http://localhost:8000/add', {
        day: date,
        title: title.value,
        main: main.value,
    })
    .then((res) => {
        console.log(res.data.msg)
        document.daily.reset();
        router.push('/edit')
    });
}

onMounted(async() => {
    const path = location.pathname.split("/").slice(-2);
    const url = "http://localhost:8000/get/" + path[0] + "/" + path[1]

    await axios.get(url)
    .then((res) => {
        day.value = res.data.day.toString()
        title.value = res.data.title
        main.value = res.data.main

        hday.value = day.value.slice( 0, 4 ) + "年" + day.value.slice( 4, 6 ) + "月" + day.value.slice( 6, 8 ) + "日"
        htitle.value = title.value

        day.value = hday.value.replace(/年|月/g, "-");
        day.value = day.value.replace(/日/g, "");
    });

    await axios.post('http://localhost:8000/delete', {
        day: day.value.replace(/-/g, ""),
        title: title.value,
    })
    .then((res) => {
        console.log(res.data.msg)
    });
})

</script>


<style>
@import '../assets/main.css';

#daily {
    text-align: center;
}

#line {
    width: 40%;
    height: 25px;
    text-align: center;
    font-size: large;
    margin: 5px;
}

#long {
    width: 55%;
    height: 300px;
    vertical-align: top;
    white-space: pre-wrap;
    font-size: large;
}

button {
    width: 160px;
    height: 50px;
    background-color: var(--color-black);
    color: white;
    border: 1px solid var(--color-black);
    border-radius: 8px;
    margin: 20px auto;
    cursor: pointer;
    font-size: large;
}

#td {
    margin-top: 3%;
    margin-bottom: 1%;
    color: var(--color-black);
    font-size: 250%;
    text-align: center;
}
</style>
