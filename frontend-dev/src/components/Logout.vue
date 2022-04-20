<template>
</template>

<script>
import cookies from "vue-cookies";
export default {
    data() {
        return {
            publicPath: process.env.BASE_URL
        }
    },

    methods: {
        logout_user() {
            cookies.remove('is_login');
            cookies.remove('email');
            window.location.href = this.publicPath + 'login'
        }
    },

    created() {
        this.logout_user();
    }
}
</script>

<style lang="scss" scoped>

</style>
