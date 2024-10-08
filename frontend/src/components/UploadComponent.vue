<script setup>
import { ref } from 'vue';

const props = defineProps(['afterUpdate']);

const API_URL = "/api";

const uploadFile = ref(null);
const uploadDescription = ref("");
const uploadUrl = ref("");

const handleFileChange = (event) => {
    uploadFile.value = event.target.files[0];
    console.log(uploadFile.value);
}

function clearFile() {
    uploadFile.value = null;
    uploadDescription.value = "";
}

function upload() {
    const formData = new FormData();
    const token = localStorage.getItem("token");

    formData.append("file", uploadFile.value);
    formData.append("url", uploadUrl.value);
    formData.append("description", uploadDescription.value);
    formData.append("token", token);

    fetch(`${API_URL}/upload`, {
        method: "POST",
        body: formData,
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        props.afterUpdate();
    })
    .catch(error => {
        console.error(error);
    });
}

</script>
<template>
    <!-- Button trigger modal -->
    <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#uploadModal">
        上傳圖片
    </button>

    <!-- Modal -->
    <div class="modal fade" id="uploadModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="exampleModalLabel">上傳</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    
                    <div class="input-group mb-3">
                        <span class="input-group-text" id="basic-addon1">描述</span>
                        <input type="text" class="form-control" placeholder="描述" v-model="uploadDescription">
                    </div>
                    <div class="input-group mb-3">
                        <label class="input-group-text" for="inputGroupFile01">圖片</label>
                        <input type="file" class="form-control" id="inputGroupFile01" accept="image/*" v-on:change="handleFileChange">
                    </div>
                    <!-- OR
                    <div class="input-group mb-3">
                        <label class="input-group-text" for="inputGroupFile01">網址</label>
                        <input type="text" class="form-control" placeholder="網址" v-model="uploadUrl">
                    </div> -->
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal" v-on:click="clearFile">Close</button>
                    <button type="button" class="btn btn-primary" v-on:click="upload" data-bs-dismiss="modal">Save changes</button>
                </div>
            </div>
        </div>
    </div>
</template>