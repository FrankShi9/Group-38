<template>
    <div class="container-fluid">

        <div class="row align-items-center">
            <div class="col-6 offset-3">
                <form>
                    <!-- website logo -->
                    <div class="avatar-box">
                        <img src="../assets/logo.png" alt="" >
                    </div>
                    <div class="mb-3 align-self-start">
                        <label for="userInputEmail1" class="form-label">Email address</label>
                        <input v-model="loginForm.email" type="email" class="form-control" id="userInputEmail1" required>
                    </div>

                    <div class="mb-3 align-self-start">
                        <label for="userInputPassword" class="form-label">Password</label>
                        <input v-model="loginForm.password" type="password" class="form-control" id="userInputPassword" required>
                    </div>
                    <div class="login-button-box">
                        <button type="submit" class="btn btn-primary" @click="login">Log in</button>
                    </div>
                </form>

            </div>
        </div>

    </div>
</template>

<script>
    import axios from 'axios';

    export default {
        name: 'Login',
        data() {
            return{
                loginForm: {
                    email:'',
                    password:''
                }
            }
        },
        methods:{
            login(event) {
                event.preventDefault()
                console.log("login is clicked")


                axios.post(
                    'https://jsonplaceholder.typicode.com/users',
                    {
                        email: this.loginForm.email,
                        password: this.loginForm.password
                    }
                )
                .then(response => console.log(response.data))
                .catch(error => console.log(error))
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