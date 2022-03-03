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
                        <label for="Username" class="form-label">Username</label>
                        <input v-model="registerForm.userName" type="text" class="form-control" id="Username" @blur="validUserName" required>
                        <p id="username-invalid" v-show="validName" style="color: red">
                            Invalid username, it should be in the range of 5-15</p>
                        <p id="username-duplicate" v-show="false" style="color: red">This username has been registered</p>
                    </div>
                    <div class="mb-3 align-self-start">
                        <label for="userInputEmail1" class="form-label">Email address</label>
                        <input v-model="registerForm.email" type="email" class="form-control" id="userInputEmail1" required>
                    </div>
                    <div class="mb-3 align-self-start">
                        <label for="userInputPassword" class="form-label">Password</label>
                        <input v-model="registerForm.password" type="password" class="form-control" id="userInputPassword"  required>
                    </div>
                    <div class="mb-3 align-self-start">
                        <label for="userConfirmPassword" class="form-label">Confirm password</label>
                        <input v-model="registerForm.confirmPassword" @blur="pwdNotSame()"
                        type="password" class="form-control" id="userConfirmPassword" required>
                        <p id="password-not-confirm" style="color: red;" v-show="ifDisplay">Your password is not consistent</p>
                    </div>
                    <div class="login-button-box">
                        <button type="submit" id="registerButton" class="btn btn-primary" @click="register" >Register</button>
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
                validName: false,
                validPassword: false,
                ifDisplay: false,
            }
        },
        //监听userName的属性值是改变
        //改变立刻调用一次该函数
        watch:{
            //隐式发送userName至服务器，查找有无重名
            'registerForm.userName':function () {
                console.log(this.registerForm.userName)
                axios.request({
                    url:'',
                    method:'post',
                    headers:{
                        'Content-type':'text/plain'
                    },
                    data:this.registerForm.userName
                }).then(response => console.log(response.data))
            }
        },
        methods:{
            register() {
                console.log("register is clicked")
                const result=axios.request({
                    url:'',
                    method:'post',
                    headers:{
                        'Content-type':'text/plain'
                    },
                    data: this.registerForm
                });
                console.log(result)
            },
            validUserName(){
                if(this.registerForm.userName.length>15 || this.registerForm.userName.length<5){
                    this.validName=true
                }else {
                    this.validName=false
                }
            },
            validPwd(){

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