<script setup lang="ts">
const props = defineProps<{
    imageUrl: string;
    description: string;
}>();

function copyLink() {
    navigator.clipboard.writeText(props.imageUrl);
}
</script>

<template>
    <a v-on:click="copyLink">
        <img :src="props.imageUrl" :alt="props.description" class="image-item rounded">
    </a>
</template>

<style scoped>
a {
    cursor: pointer;
}
</style>