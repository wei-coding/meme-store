<script setup type="ts">
import MemeComponent from '../components/MemeComponent.vue';
import UploadComponent from '../components/UploadComponent.vue';
import ManageComponent from '../components/ManageComponent.vue';
import { ref } from 'vue';

const API_URL = "/api";
var memeList = [];
var search = ref("");

var showingMemes = ref([]);
var lastIndex = 0;

function getMemes() {
    fetch(`${API_URL}/memes`)
    .then(response => response.json())
    .then(data => {
        console.log(data);
        memeList = data.memes;
        showingMemes.value = memeList;
    })
}

function isPageScrolledToBottom() {
    const visibleHeight = window.innerHeight;
    const scrollHeight = document.documentElement.scrollTop || document.body.scrollTop;
    const totalHeight = document.documentElement.scrollHeight;
    
    if (totalHeight <= visibleHeight + scrollHeight + 1) {
        showingMemes.value = memeList.slice(0, lastIndex + 10);
        lastIndex += 10;
    }
}

addEventListener("scroll", isPageScrolledToBottom);

function getMemesSearch() {
    fetch(`${API_URL}/memes/${search.value}`)
    .then(response => response.json())
    .then(data => {
        console.log(data);
        memeList = data.memes;
    })
}

function enterToken() {
    const token = prompt("token");
    localStorage.setItem("token", token);
}

getMemes();

</script>

<template>
    <div class="container">
        <nav class="navbar navbar-expand-lg navbar-light bg-light">
            <div class="container">
                <a class="navbar-brand" href="#">MEMEs Search</a>
                <div class="d-flex">
                    <div class="hidden-item" v-on:click="enterToken"></div>
                    <ManageComponent :afterUpdate="getMemes"/>
                </div>
            </div>
        </nav>

        <div class="container mt-4">
            <div class="row justify-content-center mb-4">
                <div class="col-md-6">
                    <input type="text" class="form-control" placeholder="搜尋..." v-model.trim="search" v-on:change="getMemesSearch">
                </div>
            </div>

            <div class="row justify-content-center mb-4">
                <div class="col-md-6 text-center">
                    <UploadComponent :afterUpdate="getMemes"/>
                </div>
            </div>

            <div class="image-grid">
                <MemeComponent v-for="meme in showingMemes" :description="meme.description" :imageUrl="meme.url" />
            </div>
        </div>
    </div>
</template>

<style scoped>
.hidden-item {
    width: 50px;
}
</style>