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
                        <input v-model="registerForm.confirmPassword" type="password" class="form-control" id="userConfirmPassword" required>
                        <p id="password-not-confirm" style="display:none; color: red" v-show="registerForm.password!=registerForm.confirmPassword">Your password is not consistent</p>
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
    export default {
        name: 'Register',
        data(){
            return{
                registerForm: {
                    userName: '',
                    email: '',
                    password: '',
                    confirmPassword: ''
                }
            }
        },
        methods:{
            register(){
                const result=axios.request({
                    url:'',
                    method:'post',
                    headers:{
                        'Content-type':'text/plain'
                    },
                    data:this.registerForm
                });
                console.log(result)
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