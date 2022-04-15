<template>
    <div class="main" style="width: 100%;height: calc(100vh)">
    <div class="container-fluid">
        <div class="row align-items-center">
            <div class="col-6 offset-3">
                <!-- website logo -->
                <div class="avatar-box" >
                    <img src="../assets/logo2.png" alt="" style="height: 150px;width: 200px;align-content: center">
                    <p style="font-size: 20px; align-content: center;color: white">Unique analysis, one click!</p>
                </div>
                <form method="post" action="">
                    <div class="mb-3 align-self-start">
                        <label for="email" class="form-label">Email address</label>
                        <input v-model="registerForm.email" type="email" class="form-control" id="email" name="email" @blur="registeredEmail" required>
                    </div>
                    <div class="mb-3 align-self-start">
                        <label for="password" class="form-label">Password</label>
                        <input v-model="registerForm.password" type="password" class="form-control" @blur="validPwd"
                               id="password" name="password" required>
                        <p id="password-invalid" v-show="invalidPassword" style="color: red">The password should be in the range of 8-20</p>
                    </div>
                    <div class="mb-3 align-self-start">
                        <label for="confirmPassword" class="form-label">Confirm password</label>
                        <input v-model="registerForm.confirmPassword" @blur="pwdNotSame()"
                        type="password" class="form-control" id="confirmPassword" name="confirmPassword" required >
                        <p id="password-not-confirm" style="color: red;" v-show="passwordNotSame">Your password is not consistent</p>
                    </div>
                    <div class="login-button-box">
                        <button type="submit" id="registerButton" class="btn btn-primary" >Register</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
    </div>
</template>
<script>
    import axios from 'axios';
    export default {
        name: 'Register',
        data(){
            return {
                registerForm: {
                    email: '',
                    password: '',
                    confirmPassword: ''
                },
                invalidName: false,
                invalidPassword: false,
                passwordNotSame: false,
            }
        },
        methods:{
            registeredEmail(){
                // axios.request({
                //     method:"post",
                //     url:'',
                //     data:{
                //         'email': this.registerForm.email
                //     },
                // }).then(response => {
                //
                // })
                axios.post( '', this.registerForm.email, {
                    headers: {
                        'Content-Type': 'multipart/form-data'
                    }
                }).then(response => {
                    console.log(123)
                    console.log(response.data)
                    if (response.data){
                        this.duplicateName=false
                    }else {
                        this.duplicateName=true
                    }
                })
            },
            validPwd(){
                if (this.registerForm.password.length<8 || this.registerForm.password.length>20){
                    this.invalidPassword=true
                }else {
                    this.invalidPassword=false
                }
                this.canSubmit()
            },
            pwdNotSame() {
                if (this.registerForm.password !== this.registerForm.confirmPassword) {
                    this.passwordNotSame=true
                }else{
                    this.passwordNotSame=false
                }
                this.canSubmit()
            },
            canSubmit(){
                const button = document.getElementById("registerButton")
                if (this.passwordNotSame || this.invalidPassword || this.invalidName){
                    button.disabled="disabled"
                }else{
                    button.disabled=""
                }
            }
        }
    }
</script>


<style lang="scss" scoped>
  .avatar-box {
    text-align: center;
  }
  .login-button-box {
    text-align: center;
  }
  .main{
    background: url("../assets/bg.jpg");
    background-size: 100%;
  }
</style>
