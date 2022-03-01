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
                        <input type="email" class="form-control" id="userInputEmail1">
                    </div>

                    <div class="mb-3 align-self-start">
                        <label for="userInputPassword" class="form-label">Password</label>
                        <input type="password" class="form-control" id="userInputPassword">
                    </div>
                    <div class="login-button-box">
                        <button type="submit" class="btn btn-primary">Log in</button>
                    </div>
                </form>
            </div>
        </div>

    </div>
</template>

<script>
export default {
    
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