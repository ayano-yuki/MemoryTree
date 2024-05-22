<template>
    <div class="btn-circle">
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
.btn-circle label {
    border-radius: 50%;
    background: var(--btn-color-main);
    color: var(--text-color-sub);
    font-size: 150%;
    aspect-ratio: 1;
    display: grid;
    place-items: center;
}
.btn-circle label:hover {
    background: var(--btn-color-sub);
    transition: all 0.4s;
}
.btn-circle label input {
    position: absolute;
    left:0;
    top:0;
    opacity: 0;
    width: 100%;
    height: 100%;
}
</style>