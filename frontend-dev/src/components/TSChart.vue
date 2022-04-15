<template>
    <div class="mb-3 align-self-start" id="main">
        <img :src="codeImg" alt=""/>
    </div>
</template>

<script>
    export default {
        name: "TSChart",
        data(){
            return{
                codeImg: ""

            }
        },
        created() {
            this.getImgCode()
        },
        methods:{
            getImgCode(){
                let url=localStorage.getItem('key')
                localStorage.clear()
                this.codeImg="data:image/png;base64,"+url
            }
        }
    }
</script>

<style scoped>
    #main{
        width: 1000px;
        height:400px;
        margin: 20px;
    }
</style>