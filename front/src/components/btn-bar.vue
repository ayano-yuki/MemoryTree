<template>
    <div class="btn-bar">
        <label>
            <input type="button" />
            {{ bntText }}
        </label>
    </div>
</template>

<script>
export default ({
    props: ['bntText']
})
</script>

<style scoped>
@import '../assets/base.css';
.btn-bar label {
    position: relative;
    border-radius: 20px;
    background:var(--btn-color-main);
    color: var(--text-color-sub);
    aspect-ratio: 4;
    display: grid;
    place-items: center;
    padding: 5%;
}
.btn-bar label:hover {
    background: var(--btn-color-sub);
    transition: all 0.4s;
}
.btn-bar label input {
    position: absolute;
    left:0;
    top:0;
    opacity: 0;
    width: 100%;
    height: 100%;
}
</style>