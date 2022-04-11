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
                        <p><a href="../register">Register</a></p>
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
                console.log(this.showModel);
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
//.btn {
//  display: block;
//  background-color: pink;
//  width: 200px;
//  height: 100px;
//  margin: 0 auto;
//}
</style>