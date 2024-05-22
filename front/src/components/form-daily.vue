<template>
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
import { ref } from 'vue'
import axios from 'axios'

const day = ref(0)
const title = ref("")
const main = ref("")

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
        day.value = 0
        title.value = ""
        main.value = ""
    });
}
</script>

<style scoped>
@import '../assets/base.css';

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
</style>


<!-- 
    Reference
    - [【JavaScript】フォームで必須項目を入力しない限り、送信できないようにする方法](https://www.azukipan.com/posts/javascript-form-disabled/)
    - [【JavaScript】 resetメソッドを使ってフォームをリセットしよう](https://pikawaka.com/javascript/form-reset)
    - [フォームの自動補完を無効にするには](https://developer.mozilla.org/ja/docs/Web/Security/Securing_your_site/Turning_off_form_autocompletion)
 -->