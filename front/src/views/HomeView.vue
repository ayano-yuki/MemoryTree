<template>
    <h1 id="title">Memory Tree</h1>

    <btnBar bntText="日記を書く" id="write" @click="openWriteDiary()" />
    <btnBar bntText="日記を見る" id="watch" @click="openWatchDiary()" />
    <btnBar bntText="日記を編集する" id="edit" @click="openEditDiary()" />
    <btnBar bntText="日記を削除する" id="edit" @click="openDeleteDiary()" />

    <button type="submit" id="treeBtn" @click="TREE()">Tree</button>
</template>

<script setup>
import btnBar from '../components/btn-bar.vue'
import { useRouter } from 'vue-router'

const router = useRouter()

const openWriteDiary = () => {
    router.push('write')
}

const openWatchDiary = () => {
    router.push('watch')
}

const openEditDiary = () => {
    router.push('edit')
}

const openDeleteDiary = () => {
    router.push('delete')
}

const TREE = () => {
    router.push('/tree')
}

</script>

<style scoped>
#title {
    margin-top: 5%;
    color: #323232;
    text-align: center;
    font-size: 400%;
}

#write {
    width: 17%;
    margin-left: auto;
    margin-right: auto;
    margin-top: 5%;
    text-align: center;
    min-width: 200px;
}

#watch {
    width: 17%;
    margin-left: auto;
    margin-right: auto;
    margin-top: 20px;
    text-align: center;
    min-width: 200px;
}

#edit {
    width: 17%;
    margin: 2px auto;
    margin-left: auto;
    margin-right: auto;
    margin-top: 20px;
    min-width: 200px;
}

#treeBtn {
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