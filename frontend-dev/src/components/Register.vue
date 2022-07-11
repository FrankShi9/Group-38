<template>
    <div class="container-fluid">

        <div class="row align-items-center">
            <div class="col-6 offset-3">
                <!-- website logo -->
                <div class="avatar-box">
                    <img src="../assets/logo.png" alt="" >
                </div>
                <form method="post" action="/Area_38_app/views.py">
                    <div class="mb-3 align-self-start">
                        <label for="userName" class="form-label">Username</label>
                        <input v-model="registerForm.userName" type="text" class="form-control" id="userName" name="userName" @blur="validUserName" required>
                        <p id="username-invalid" v-show="invalidName" style="color: red">
                            Invalid username, it should be in the range of 5-15</p>
                        <p id="username-duplicate" v-show="false" style="color: red">This username has been registered</p>
                    </div>
                    <div class="mb-3 align-self-start">
                        <label for="email" class="form-label">Email address</label>
                        <input v-model="registerForm.email" type="email" class="form-control" id="email" name="email" required>
                    </div>
                    <div class="mb-3 align-self-start">
                        <label for="password" class="form-label">Password</label>
                        <input v-model="registerForm.password" type="password" class="form-control" @blur="validPwd"
                               id="password" name="password" required>
                        <p id="password-invalid"></p>
                    </div>
                    <div class="mb-3 align-self-start">
                        <label for="confirmPassword" class="form-label">Confirm password</label>
                        <input v-model="registerForm.confirmPassword" @blur="pwdNotSame()"
                        type="password" class="form-control" id="confirmPassword" name="confirmPassword" required >
                        <p id="password-not-confirm" style="color: red;" v-show="ifDisplay">Your password is not consistent</p>
                    </div>
                    <div class="login-button-box">
                        <button type="submit" id="registerButton" class="btn btn-primary" >Register</button>
                    </div>
                </form>
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
                    userName: '',
                    email: '',
                    password: '',
                    confirmPassword: ''
                },
                invalidName: false,
                validPassword: false,
                ifDisplay: false,
            }
        },
        //监听userName的属性值是改变
        //改变立刻调用一次该函数
        watch:{
            //隐式发送userName至服务器，查找有无重名
            'registerForm.userName':function (value) {
                console.log(this.registerForm.userName)
                console.log(value)
                axios.request({
                    url:'https://jsonplaceholder.typicode.com/users',
                    method:'post',
                    data:{
                        userName: this.registerForm.userName
                    }
                }).then(response => console.log(response.data))
            }
        },
        methods:{
            validUserName(){
                const button = document.getElementById("registerButton")
                if(this.registerForm.userName.length>15 || this.registerForm.userName.length<5){
                    this.invalidName=true
                    button.disabled="disabled"
                }else {
                    this.invalidName=false
                    button.disabled=""
                }
            },
            validPwd(){
                const button = document.getElementById("registerButton")
                const p=document.getElementById("password-invalid")
                if (this.registerForm.password.length<8 || this.registerForm.password.length>20){
                    p.innerHTML="The password should be in the range of 8-20"
                    p.style.color="red"
                    button.disabled="disabled"
                }else {
                    p.innerHTML=""
                    button.disabled=""
                }
            },
            pwdNotSame() {
                const button = document.getElementById("registerButton")
                if (this.registerForm.password !== this.registerForm.confirmPassword) {
                    this.ifDisplay=true
                    button.disabled="disabled"
                }else{
                    this.ifDisplay=false
                    button.disabled=""
                }
            },
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
</style>