<template>
    <div class="main" style="height: calc(100vh);width: 100%">
    <div class="container-fluid">
        <div class="row align-items-center">
            <div class="col-6 offset-3">
                <form method="post">
                    <!-- website logo -->
                    <div class="avatar-box" >
                        <img src="../assets/logo2.png" alt="" style="height: 100px;width: 200px;align-content: center">
                        <p style="font-size: 20px; align-content: center;color: white">Unique analysis, one click!</p>
                    </div>
                    <div class="mb-3 align-self-start">
                        <label for="email" class="form-label" >Email address</label>
                        <input v-model="loginForm.email" type="email" class="form-control" id="email" name="email" required>
                    </div>

                    <div class="mb-3 align-self-start">
                        <label for="password" class="form-label">Password</label>
                        <input v-model="loginForm.password" type="password" class="form-control" id="password" name="password" required>
                    </div>
                    <div >
                        <p><a href="../register" style="color: white">Register</a></p>
                    </div>
                    <div class="login-button-box">
                        <button type="button" class="btn btn-primary" @click="show">Skip</button>
                        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                        <button type="submit" class="btn btn-primary">Login</button>
                    </div>
                </form>

            </div>
        </div>
    </div>
    </div>
    <div class="home">
        <model :showModel="this.showModel" @cancel="this.showModel=false"></model>
    </div>
</template>

<script>
    import Model from '../components/Model'
    export default {
        name: 'Login',
        components:{ Model },
        data() {
            return{
                loginForm: {
                    email:'',
                    password:'',
                },
                showModel: false
            }
        },
        methods:{
            show() {
                this.showModel = true;
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
.home {
   width: 100%;
   height: 1000px;
}
.main{
  background: url("../assets/bg.jpg");
  background-size: 100%;
}
.form-label{
  color: white;
}
</style>