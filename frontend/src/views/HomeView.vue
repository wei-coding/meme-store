<script setup type="ts">
import MemeComponent from '../components/MemeComponent.vue';
import UploadComponent from '../components/UploadComponent.vue';
import { ref } from 'vue';

var memeList = ref([]);
var search = ref("");

for (let i=0; i<9; i++) {
    memeList.value.push({
        link: "123",
        imageUrl: "https://via.assets.so/img.jpg?w=300&h=300"
    })
}

function isPageScrolledToBottom() {
    const visibleHeight = window.innerHeight;
    const scrollHeight = document.documentElement.scrollTop || document.body.scrollTop;
    const totalHeight = document.documentElement.scrollHeight;
    
    if (totalHeight <= visibleHeight + scrollHeight + 1) {
        for (let i=0; i<9; i++) {
            memeList.value.push({
                link: "123",
                imageUrl: "https://via.assets.so/img.jpg?w=300&h=300"
            })
        }
    }
}

addEventListener("scroll", isPageScrolledToBottom);

</script>

<template>
    <div class="container">
        <nav class="navbar navbar-expand-lg navbar-light bg-light">
            <div class="container">
                <a class="navbar-brand" href="#">MEMEs Search</a>
            </div>
        </nav>

        <div class="container mt-4">
            <div class="row justify-content-center mb-4">
                <div class="col-md-6">
                    <input type="text" class="form-control" placeholder="搜尋..." v-model="search">
                </div>
            </div>

            <div class="row justify-content-center mb-4">
                <div class="col-md-6 text-center">
                    <UploadComponent/>
                </div>
            </div>

            <div class="image-grid">
                <MemeComponent v-for="meme in memeList" :link="meme.link" :imageUrl="meme.imageUrl" />
            </div>
        </div>
    </div>
</template>