<template>
    <div class="container-fluid">
        <div class="row align-items-center">
            <div class="col-6 offset-3">
                <form method="post">
                    <!-- website logo -->
                    <div class="avatar-box">
                        <img src="../assets/logo.png" style="width:400px;height:300px;-webkit-filter: drop-shadow(5px 5px 5px #808080);
  filter: drop-shadow(5px 5px 5px #808080);" alt="" >
                    </div>
                    <div class="mb-3 align-self-start">
                        <label for="email" class="form-label"><div style="text-align:justify">Email address</div></label>
                        <input v-model="loginForm.email" type="email" class="form-control" id="email" name="email" required>
                    </div>

                    <div class="mb-3 align-self-start">
                        <label for="password" class="form-label">Password&nbsp;&nbsp;<router-link to="/forget/"><i>Forgot password?</i></router-link></label>
                        <input v-model="loginForm.password" type="password" class="form-control" id="password" name="password" required>
                    </div>
                    <div>
                        <router-link to="/register/">Need an account? Sign up</router-link>
                         <!-- <a :href="'../register'">Need an account? Sign up</a> -->
                    </div>
                    <br>
                    <div class="login-button-box">
                        <button type="button" class="btn btn-secondary" @click="show">Skip</button>
                        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                        <button type="submit" class="btn btn-primary" >Login</button>
                    </div>
                </form>
            </div>
        </div>
        <div class="home">
            <model :showModel="this.showModel" @cancel="this.showModel=false"></model>
        </div>
    </div>
</template>

<script>
    import Model from '../components/Model'
    import cookies from "vue-cookies";
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
   height: auto;
}
</style>