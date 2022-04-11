<template>
    <div class="model" v-show="this.showModel">
        <div class="model-dialog">
            <div class="model-header">
                <span>Warning</span>
            </div>
            <div class="model-body">
                <div class="body" style="font-size: 20px;">If you skip login, you can not enjoy all the functions</div>
            </div>
            <div class="model-footer">
                <button class="btn" @click="skip">Confirm</button>
                <button class="btn" @click="$emit('cancel')">Cancel</button>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "model",
        props:{showModel : Boolean},
        methods:{
            skip(){
                window.location.href="/chooseFunc"
            }
        }
    }
</script>

<style scoped>
    .model-dialog {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        background-color: #fff;
        border-radius: 12px;
        width: 600px;
        height: 300px;
        border: 1px solid #f5f5f5;
        overflow: hidden;
        z-index: 10;
    }
    .model-header {
        position: relative;
        height: 50px;
        padding-left: 10px;
        padding-top: 10px;
        font-size: 20px;
        line-height: 50px;
        background-color: #f5f5f5;
        border-bottom: 1px solid rgb(177, 176, 176);
    }
    .model-body {
        height: 150px;
        line-height: 150px;
        font-size: 28px;
        text-align: center;
        background-color: #fff;
    }
    .model-footer {
        background-color: #f5f5f5;
        height: 100px;
        text-align: center;
        line-height: 100px;
    }
    .btn {
        width: 180px;
        height: 40px;
        border-radius: 8px;
        background-color: rgb(180, 103, 103);
        color: #fff;
        font-size: 18px;
        border: none;
    }
</style>