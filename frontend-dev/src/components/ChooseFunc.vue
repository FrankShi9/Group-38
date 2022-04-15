<template>
    <div class="container-fluid">
        <div class="row align-items-center">
            <div class="col-6 offset-3">
                <div class="mb-3 align-self-start">
                    <button type="submit" class="buttonOne form-control" @click="onSubmitOne">Demand-Supply</button>
                </div>
                <div class="mb-3 align-self-start">
                    <button type="submit" class="buttonTwo form-control" @click="onSubmitTwo">RFM-Prediction</button>
                </div>
                <div class="mb-3 align-self-start">
                    <button type="submit" class="buttonThree form-control" @click="onSubmitThree">Time-Series Prediction</button>
                </div>
            </div>
        </div>
    </div>

</template>

<script>
    import axios from "axios";
    import $ from 'jquery';
    import cookies from 'vue-cookies'
    export default {
        name: "ChooseFunc",
        data(){
            return{
                file:"",
                funcNum: 0,
                status: false
            }
        },
        methods:{
            onSubmitOne(){
                this.funcNum=1
                window.location.href='/uploadfile?funcNum='+this.funcNum
            },
            onSubmitTwo(){
                this.funcNum=2
                window.location.href='/uploadfile?funcNum='+this.funcNum
            },
            onSubmitThree(){
                this.funcNum=3
                if (!this.status){
                    alert("You need to login, help you redirect to login page")
                    window.location.href='/login'
                }else {
                    window.location.href='/uploadfile?funcNum='+this.funcNum
                }
            },
            handleFileUpload( event ){
                // a single file
                this.file = event.target.files[0];
            }
        },
        created() {
            this.status = cookies.get('is_login')

            // if (document.cookie) {
            //     var cookie = {};
            //     var line = document.cookie.split("; ");
            //     cookie[line[0].split("=")[0]] = line[0].split("=")[1];
            //     cookie[line[1].split("=")[0]] = line[1].split("=")[1];
            //     console.log(cookie);
            //     //this.user = "欢迎:" + cookie["username"] + "(id:" + cookie["id"] + ")";
            // }
        }
    }
</script>

<style scoped>

</style>