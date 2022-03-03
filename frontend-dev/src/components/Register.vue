<template>
    <div class="container-fluid">

        <div class="row align-items-center">
            <div class="col-6 offset-3">
                <!-- website logo -->
                <div class="avatar-box">
                    <img src="../assets/logo.png" alt="" >
                </div>
                <form>
                    <div class="mb-3 align-self-start">
                        <label for="Username" class="form-label">Username</label>
                        <input v-model="registerForm.userName" type="text" class="form-control" id="Username"  required>
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
                        <p id="password-not-confirm" style="visibility:hidden; color: red">Your password is not consistent</p>
                    </div>
                    <div class="login-button-box">
                        <button type="submit" class="btn btn-primary" @click="register">Register</button>
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
                }
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

            pwdNotSame() {
                if (this.registerForm.password != this.registerForm.confirmPassword) {
                    console.log("Pwd not the same")
                    var feedback = document.getElementById("password-not-confirm")
                    feedback.style.visibility = 'visible'
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
</style>