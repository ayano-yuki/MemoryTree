<template>
    <img v-bind:src="imageData" id="tree" style="max-height: 850px;"/>

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

const imageData = ref()

onMounted(() => {
    axios.get('http://localhost:8000/tree')
    .then((res) => {
        imageData.value = res.data.img
    });
})
</script>

<style>
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

#tree{
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translateY(-50%) translateX(-50%);
}
</style>

<!-- 
Reference
- [CSS：CSSで画像の幅・高さの最大値を指定する](http://raining.bear-life.com/css/css%E3%81%A7%E7%94%BB%E5%83%8F%E3%81%AE%E5%B9%85%E3%83%BB%E9%AB%98%E3%81%95%E3%81%AE%E6%9C%80%E5%A4%A7%E5%80%A4%E3%82%92%E6%8C%87%E5%AE%9A%E3%81%99%E3%82%8B)
- [Pythonで画像をBase64文字列に変換する方法](https://morioh.com/p/13dfe537941c)
- [HTMLファイルの中に画像を埋め込んで表示させる方法](https://allabout.co.jp/gm/gc/23977/)

-->