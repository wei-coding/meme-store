<script setup lang="ts">
const props = defineProps<{
    imageUrl: string;
    link: string;
}>();

function copyLink() {
    navigator.clipboard.writeText(props.link);
}
</script>

<template>
    <a v-on:click="copyLink">
        <img :src="props.imageUrl" alt="範例圖片" class="image-item rounded">
    </a>
</template>

<style scoped>
a {
    cursor: pointer;
}
</style>