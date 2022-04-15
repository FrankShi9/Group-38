<template>
    <div class="mb-3 align-self-start" id="main"></div>
</template>

<script>
    import * as echarts from 'echarts';
    import $ from "jquery";
    export default {
        name: "",
        data(){
            return{

            }
        },
        methods:{

        },
        created() {
            let url=decodeURIComponent(this.$route.query.arg)
            let arg=JSON.parse(url)
            let keys=Object.keys(arg)
            let values=Object.values(arg)

            function generator(){
                const data=[]
                for(var i=0;i<keys.length;i++){
                    data.push({name: keys[i], value: values[i]})
                }
                return data
            }
            const option = {
                tooltip:{
                    showContent: true
                },
                series: [
                    {
                        type: 'treemap',
                        data: generator()
                    }
                ]
            };
            $(document).ready(function(){
                const chart=echarts.init(document.getElementById("main"))
                chart.setOption(option)
            });
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