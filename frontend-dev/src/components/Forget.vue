<template>
    <div class="container-fluid">

        <div class="row align-items-center">
            <div class="col-6 offset-3">
                <!-- website logo -->
                <div class="avatar-box">
                    <img src="../assets/logo.png" style="width: 300px;height: 200px" alt="" >
                </div>
                <form >
                    <div class="mb-3 align-self-start">
                        <label for="email" class="form-label">Email address</label>
                        <input type="email" class="form-control" id="email" style="width: 85%;float: left" required>
                        <button class="btn btn-primary" style="border-radius: 8px;float: left; margin-left: 15px">Verify</button>
                    </div><br><br>
                    <div class="mb-3 align-self-start">
                        <label for="verificationCode" class="form-label">Verification code</label>
                        <input  type="text" class="form-control" id="verificationCode"  required>
                    </div>
                    <div class="mb-3 align-self-start">
                        <label for="newPassword" class="form-label">New password</label>
                        <input type="password" class="form-control" id="newPassword" required>
                    </div>
                    <div class="login-button-box">
                        <button type="submit" id="forgetButton" class="btn btn-primary" >Continue</button>
                    </div>
                </form>
            </div>
        </div>

    </div>
</template>

<script>
    export default {
        name: "Forget",
    }
</script>

<style scoped>
    .avatar-box {
        text-align: center;
    }
    .login-button-box {
        text-align: center;
    }
</style>