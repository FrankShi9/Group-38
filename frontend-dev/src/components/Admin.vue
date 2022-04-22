<template>
    <div class="container-fluid">
        <div class="row align-items-center">
            <div class="col-6 offset-3">
                <div class="mb-3 align-self-start" style="text-align: center;width: auto;height: 50px;font-size: 50px;font-family: sans-serif">{{user}}</div>
                <br><br>
                <div class="mb-3 align-self-start" style="text-align: center">
                    <button type="submit" class="showUser btn-primary" @click="funcOne" style="width: 150px;border-radius: 8px;margin-right: 50px">Show all users</button>
                    <button type="submit" class="updateModel btn-primary" @click="funcTwo" style="width: 150px;border-radius: 8px;margin-left: 50px">Update models</button>
                </div>
                <div class="mb-3 align-self-start" style="text-align: center">
                    <ul v-show="this.show" style="list-style: none">
                        <li v-for="(data, index) in userAll" style="text-align: center">Index: {{index+1}}, Email: {{data[0]}}, Password:{{data[1]}}</li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
    <div class="home">
        <model :showModelFour="this.showModelFour" @cancel="this.showModelFour=false"></model>
    </div>
</template>

<script>
    import cookies from 'vue-cookies'
    import axios from "axios";
    import Model from '../components/Model'
    export default {
        name: "Admin",
        components:{Model},
        data(){
            return{
                user:'',
                userAll:[],
                show:false,
                showModelFour:false
            }
        },
        created() {
            if(cookies.get("admin")!=null){
                this.user = "Welcome! Admin!";
            }
        },
        methods:{
            funcOne(){
                axios({
                    method:'post',
                    url:''
                }).then((response) => {
                    this.show=!this.show
                    if (this.show && this.userAll.length==0){
                        console.log(response.data)
                        const arg=response.data
                        for (var i=0;i<arg.email.length;i++){
                            this.userAll.push([arg.email[i], arg.password[i]])
                        }
                        console.log(this.userAll)
                    }
                })
                cookies.set("funcNum",1)
            },
            funcTwo(){
                this.showModelFour=!this.showModelFour
            }
        }
    }
</script>

<style scoped>

</style>