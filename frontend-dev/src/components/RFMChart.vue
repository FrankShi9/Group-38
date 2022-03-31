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
            // for (const key in arg) {
            //     keys.push(key)
            //     console.log(Object.keys(arg)[0])
            // }
            console.log(keys)

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
                        //     [
                        //     {
                        //         name: 'Activate them',
                        //         value: 392,
                        //         // children: [
                        //         //     {
                        //         //         name: 'nodeAa',
                        //         //         value: 4
                        //         //     },
                        //         //     {
                        //         //         name: 'nodeAb',
                        //         //         value: 6
                        //         //     }
                        //         // ]
                        //     },
                        //     {
                        //         name: 'Champions',
                        //         value: 421,
                        //         // children: [
                        //         //     {
                        //         //         name: 'nodeBa',
                        //         //         value: 20,
                        //         //         children: [
                        //         //             {
                        //         //                 name: 'nodeBa1',
                        //         //                 value: 20
                        //         //             }
                        //         //         ]
                        //         //
                        //         //
                        //         //
                        //         //     }
                        //         // ]
                        //     },
                        //     {
                        //         name: 'Do not lose them',
                        //         value: 1690
                        //     },
                        //     {
                        //         name: 'Loyal',
                        //         value: 447
                        //     },
                        //     {
                        //         name: 'Pay attention',
                        //         value: 391
                        //     },
                        //     {
                        //         name: 'Potential',
                        //         value: 468
                        //     },
                        //     {
                        //         name: 'Promising',
                        //         value: 517
                        //     }
                        // ]
                    }
                ]
            };
            $(document).ready(function(){
                const chart=echarts.init(document.getElementById("main"))
                chart.setOption(option)
                chart.on('click',function (params){
                    if (params.componentType==='series'){
                        console.log(params)
                    }
                    console.log(params)
                })
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