<!--<template>-->
<!--    <div id="tips"></div>-->
<!--    <div id="nanobar">-->
<!--        <div id="bar"></div>-->
<!--    </div>-->
<!--</template>-->

<!--<script>-->
<!--    import $ from 'jquery'-->
<!--    import axios from "axios";-->
<!--    import 'nanobar'-->

<!--    //进度条设置-->
<!--    const options = {-->
<!--        target: $("#nanobar")-->
<!--    };-->
<!--    //进度条初始化-->
<!--    const nanobar = new Nanobar( options );-->

<!--    export default {-->
<!--        name: "Waiting",-->
<!--        data(){-->
<!--            return {-->

<!--            }-->
<!--        },-->
<!--        beforeCreate() {-->

<!--        },-->
<!--        create() {-->
<!--            const interval=setInterval(function(){-->
<!--                axios.request({-->
<!--                    method:'post',-->
<!--                    url:'',-->
<!--                    dataType:'text',-->
<!--                }).then(response => {-->
<!--                    $("#tips").innerHTML="Analysing, please wait..."-->
<!--                    $("#nanobar").fadeIn()-->
<!--                    nanobar.go(response)-->
<!--                })-->
<!--            },1000)-->

<!--            axios.request({-->
<!--                method:'post',-->
<!--                url:'',-->

<!--            })-->
<!--        }-->
<!--    }-->
<!--</script>-->

<!--<style scoped>-->
<!--    #nanobar{-->
<!--        border: 1px solid 	#DBDBDB;-->
<!--        border-radius: 7px;-->
<!--        background: #FAFAFA;-->
<!--        width: 450px;-->
<!--        height: 14px;-->
<!--    }-->
<!--    #nanobar #bar{-->
<!--        border-radius: 7px;-->
<!--        background: #43CD80;-->
<!--    }-->
<!--</style>-->