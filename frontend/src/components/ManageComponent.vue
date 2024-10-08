<script setup>
import { ref } from 'vue';

const props = defineProps(['afterUpdate']);

const API_URL = "/api";
var memeList = ref([]);

function getMemes() {
    fetch(`${API_URL}/memeswithid`)
    .then(response => response.json())
    .then(data => {
        console.log(data);
        memeList.value = data.memes;
    })
}

function deleteMeme(id) {
    const token = localStorage.getItem("token");
    fetch(`${API_URL}/memes/${id}?token=${token}`, {
        method: 'DELETE',
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        getMemes();
        props.afterUpdate();
    })
}
getMemes();

</script>
<template>
    <!-- Button trigger modal -->
    <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#manageModal" v-on:click="getMemes">
        Manage
    </button>

    <!-- Modal -->
    <div class="modal fade" id="manageModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="exampleModalLabel">管理頁面</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <ul class="list-group">
                        <li v-for="meme in memeList" class="list-group-item d-flex justify-content-between align-items-center">
                            <img :src="meme.url" class="img-fluid" style="width: 50px; height: 50px;">
                            {{ meme.description }}
                            <button type="button" class="btn btn-danger" v-on:click="deleteMeme(meme.id)">Delete</button>
                        </li>
                    </ul>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal" v-on:click="clearFile">Close</button>
                </div>
            </div>
        </div>
    </div>
</template>