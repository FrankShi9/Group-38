<template>
    <div class="container-fluid">

        <div class="row align-items-center">
            <div class="col-6 offset-3">
                <form method="post">
                    <!-- website logo -->
                    <div class="avatar-box">
                        <img src="../assets/logo.png" alt="" >
                    </div>
                    <div class="mb-3 align-self-start">
                        <label for="email" class="form-label">Email address</label>
                        <input v-model="loginForm.email" type="email" class="form-control" id="email" name="email" required>
                    </div>

                    <div class="mb-3 align-self-start">
                        <label for="password" class="form-label">Password</label>
                        <input v-model="loginForm.password" type="password" class="form-control" id="password" name="password" required>
                    </div>
                    <div>
                        <p><a href="../register">Register</a>
                            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                            <a href="../forget">Forget password</a></p>
                    </div>
                    <div class="login-button-box">
                        <button type="submit" class="btn btn-primary">Login</button>
                    </div>
                </form>

            </div>
        </div>

    </div>
</template>

<script>
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