<template>
    <div class="model" v-show="this.showModel">
        <div class="modelOne-dialog">
            <div class="modelOne-header">
                <span>Warning</span>
            </div>
            <div class="modelOne-body">
                <div class="body" style="font-size: 20px;">If you skip login, you can not enjoy all the functions</div>
            </div>
            <div class="modelOne-footer">
                <button class="btn" @click="skip">Confirm</button>
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                <button class="btn" @click="$emit('cancel')">Cancel</button>
            </div>
        </div>
    </div>
    <div class="model" v-show="this.showModelTwo">
        <div class="modelTwo-dialog">
            <div class="modelTwo-header">
                <span>Attention</span>
            </div>
            <div class="modelTwo-body">
                Your file is being processed,please wait...
            </div>
        </div>
    </div>
    <div class="model" v-show="this.showModelThree">
        <div class="modelThree-dialog">
            <div class="modelThree-header">Please choose your preference model</div>
            <div class="modelThree-body">
                <div class="introOne" >
                    <p style="border:1px solid black;width:300px; height:280px;padding:5px;">
                        AI Model: I consider that a man's brain originally is like a little empty attic, and you have to stock it with such furniture as you choose. so that he has a difficulty in laying his hands upon it.
                    </p>
                </div>
                <div class="introTwo">
                    <p style="border:1px solid black;width:300px;height: 280px; padding:5px;">
                        Statistical Model: A fool takes in all the lumber of every sort that he comes across, so that the knowledge which might be useful to him gets crowded out, or at best is jumbled up with a lot of other things,
                    </p>
                </div>
            </div>
            <div class="modelThree-footer">
                <button class="btn" @click="modelOne">AI: LSTM</button>
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                <button class="btn" @click="modelTwo">Statistical Model</button>
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                <button class="btn" @click="$emit('cancel')">Cancel</button>
            </div>
        </div>
    </div>
    <div class="model" v-show="this.showModelFour">
        <div class="modelFour-dialog">
            <div class="modelFour-header">Please choose updated model</div>
            <div class="modelFour-body">
                <div href="javascript:;" class="upload">Choose File
                    <input class="inputFile" id="inputFile" type="file" @change="handleFileUpload( $event )"/>
                </div>
                <div id="fileInfo"></div>
            </div>
            <div class="modelFour-footer">
                <button class="btnFour" @click="submitFile">Submit</button>
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                <button class="btnFour" @click="$emit('cancel')">Cancel</button>
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

            }
        },
        methods:{
            skip(){
                window.location.href="/home"
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
                const str=document.getElementById('inputFile').value.split("\\")
                console.log(str)
                document.getElementById('fileInfo').innerHTML = str.pop()
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
                    this.showModelFour=false
                    alert(response.data)
                })
            }
        }
    }
</script>

<style scoped>
    .modelOne-dialog{
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        background-color: #fff;
        border-radius: 12px;
        width: 800px;
        height: 300px;
        border: 1px solid #f5f5f5;
        overflow: hidden;
        z-index: 10;
    }
    .modelOne-header{
        position: relative;
        height: 50px;
        padding-left: 10px;
        padding-top: 10px;
        font-size: 20px;
        line-height: 50px;
        background-color: #f5f5f5;
        border-bottom: 1px solid rgb(177, 176, 176);
    }
    .modelOne-body{
        heigth: 250px;
        line-height: 150px;
        font-size: 28px;
        text-align: center;
        background-color: #fff;
    }
    .modelOne-footer{
        background-color: #f5f5f5;
        height: 100px;
        text-align: center;
        line-height: 100px;
    }
    .modelTwo-dialog{
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        background-color: #fff;
        border-radius: 12px;
        width: 800px;
        height: 150px;
        border: 1px solid #f5f5f5;
        overflow: hidden;
        z-index: 10;
    }
    .modelTwo-header{
        position: relative;
        height: 50px;
        padding-left: 10px;
        padding-top: 10px;
        font-size: 20px;
        line-height: 50px;
        background-color: #f5f5f5;
        border-bottom: 1px solid rgb(177, 176, 176);
    }
    .modelTwo-body{
        height: 100px;
        line-height: 100px;
        font-size: 20px;
        text-align: center;
        background-color: #fff;
    }
    .modelThree-dialog{
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        background-color: #fff;
        border-radius: 12px;
        width: 800px;
        height: 400px;
        border: 1px solid #f5f5f5;
        overflow: hidden;
        z-index: 10;
    }
    .modelThree-header{
        position: relative;
        height: 50px;
        padding-left: 10px;
        padding-top: 10px;
        font-size: 20px;
        background-color: #f5f5f5;
        border-bottom: 1px solid rgb(177, 176, 176);
    }
    .modelThree-body{
        height: 300px;
        font-size: 20px;
        text-align: center;
        background-color: #fff;
    }
    .modelThree-footer{
        background-color: #f5f5f5;
        height: 50px;
        text-align: center;
        line-height: 50px;
    }
    .introOne{
        float: left;
        width: 300px;
        height: 280px;
        font-size: 20px;
        margin-left: 75px;
        margin-top: 10px;
    }
    .introTwo{
        float: left;
        width: 300px;
        height: 280px;
        font-size: 20px;
        margin-left: 75px;
        margin-top: 10px;
    }
    .modelFour-dialog{
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        background-color: #fff;
        border-radius: 12px;
        width: 400px;
        height: 180px;
        border: 1px solid #f5f5f5;
        overflow: hidden;
        z-index: 10;
    }
    .modelFour-header{
        position: relative;
        height: 30px;
        padding-left: 10px;
        padding-top: 10px;
        font-size: 15px;
        background-color: #f5f5f5;
        border-bottom: 1px solid rgb(177, 176, 176);
    }
    .modelFour-body{
        height: 100px;
        font-size: 28px;
        text-align: center;
        background-color: #fff;
    }
    .modelFour-footer{
        background-color: #f5f5f5;
        height: 50px;
        text-align: center;
    }
    .btn {
        width: 150px;
        height: 40px;
        border-radius: 8px;
        background-color: #0a58ca;
        color: #fff;
        font-size: 15px;
        border: none;
    }
    .btnFour{
        width: 150px;
        height: 30px;
        border-radius: 8px;
        background-color: #0a58ca;
        color: #fff;
        font-size: 15px;
        border: none;
        margin-top: 10px;
    }
    .upload{
        width: 150px;
        padding: 4px 10px;
        line-height:25px;
        position: relative;
        border: 1px solid #999;
        border-radius: 8px;
        text-decoration: none;
        background-color: #0a58ca;
        color: #fff;
        font-size: 15px;
        margin-left: 50px;
        margin-top: 15px;
        float: left;
    }
    .inputFile{
        position: absolute;
        overflow: hidden;
        right: 0;
        top: 0;
        opacity: 0;
    }
    #fileInfo{
        float: left;
        font-size: 20px;
        width: 100px;
        heigth: 50px;
        margin-left: 10px;
        margin-top: 17px;
    }
</style>