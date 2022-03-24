<template>
    <div class="container-fluid">

        <div class="row align-items-center">
            <div class="col-6 offset-3">
                <!-- website logo -->
                <div class="avatar-box">
                    <img src="../assets/logo.png" alt="" >
                </div>
                <form >
                    <div class="mb-3 align-self-start">
                        <label for="email" class="form-label">Email address</label>
                        <input v-model="forgetForm.email" type="email" class="form-control" id="email" required>
                        <button @click="send">Verify</button>
                    </div>
                    <div class="mb-3 align-self-start">
                        <label for="verificationCode" class="form-label">Verification code</label>
                        <input v-model="forgetForm.code" type="text" class="form-control" id="verificationCode"  required>
                    </div>
                    <div class="mb-3 align-self-start">
                        <label for="newPassword" class="form-label">New password</label>
                        <input v-model="forgetForm.newPassword"
                               type="password" class="form-control" id="newPassword" required>
                    </div>
                    <div class="login-button-box">
                        <button type="submit" id="forgetButton" class="btn btn-primary" >Continue</button>
                    </div>
                </form>
            </div>
        </div>

    </div>
</template>

<script>
    //import {SMTPClient} from 'emailjs'

    // const client=new SMTPClient({
    //     user:'',
    //     password:'',
    //     host:'',
    //     port:'',
    //     ssl:true
    // })
    export default {
        name: "Forget",
        data(){
            return{
                forgetForm:{
                    email:"",
                    code:"",
                    newPassword:""
                }
            }
        },
        methods:{
            // async send(){
            //     try {
            //         await client.sendAsync({
            //             text:"Hello world",
            //             from:'',
            //             to:"",
            //             subject:''
            //         })
            //     }catch (e){
            //         console.log(e)
            //     }
            // }
        }
    }
</script>

<style scoped>
    .avatar-box {
        text-align: center;
    }
    .login-button-box {
        text-align: center;
    }
</style>