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
    <div class="model" v-show="this.showModelTwo">
        <div class="model-dialog">
            <div class="model-header">
                <span>Attention</span>
            </div>
            <div class="model-body">
                <div class="body" style="font-size: 20px;">Your file is being processed,please wait...</div>
            </div>
        </div>
    </div>
    <div class="model" v-show="this.showModelThree">
        <div class="model-dialog">
            <div class="model-body">
                <div class="body" style="font-size: 20px;">Please choose your preference model</div>
            </div>
            <div class="model-footer">
                <button class="btn" @click="modelOne">AI: LSTM</button>
                <button class="btn" @click="modelTwo">Statistical Model</button>
                <button class="btn" @click="$emit('cancel')">Cancel</button>
            </div>
        </div>
    </div>
    <div class="model" v-show="this.showModelFour">
        <div class="model-dialog">
            <div class="model-body">
                <div class="body" style="font-size: 20px;">Please choose updated model</div>
                <input type="file" @change="handleFileUpload( $event )" placeholder="choose a file">
                <div>{{responseData}}</div>
            </div>
            <div class="model-footer">
                <button class="btn" @click="submitFile">Submit</button>
                <button class="btn" @click="$emit('cancel')">Cancel</button>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from "axios";
    import cookies from "vue-cookies";
    export default {
        name: "model",
        props:{showModel : Boolean, showModelTwo : Boolean, showModelThree: Boolean, showModelFour: Boolean},
        data(){
            return{
                responseData:''
            }
        },
        methods:{
            skip(){
                window.location.href="/chooseFunc"
            },
            modelOne(){
                window.location.href="/uploadfile?funcNum=3.1"
            },
            modelTwo(){
                window.location.href="/uploadfile?funcNum=3.2"
            },
            handleFileUpload( event ){
                // a single file
                this.file = event.target.files[0];
            },
            submitFile(){
                let formData = new FormData();
                cookies.set("funcNum",2)
                //let funcNum = this.$route.query.funcNum
                formData.append('file', this.file);
                // issue a POST request
                axios.post( '', formData, {
                        headers: {
                            'Content-Type': 'multipart/form-data'
                        }
                    }
                ).then((response) => {
                    this.responseData=response.data
                })
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