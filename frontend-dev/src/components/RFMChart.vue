<template>
    <div class="mb-3 align-self-start" id="main"></div>
    <img src="../assets/RFM.png" style="width: 400px;height: 200px" id="Img">
    <div id="buttons">
<!--        <button id="downloadImg" style="margin: 5px;border-radius: 8px" class="btn-primary">Download Charts</button>-->
        <button id="downloadResults" style="margin: 5px;border-radius: 8px" class="btn-primary" @click="askDownload">Download Results</button>
        <button id="return" style="margin: 5px;border-radius: 8px" class="btn-primary" @click="returnBack">Return back to main menu</button>
    </div>
    <div class="mb-3 align-self-start" id="statistics1"></div>
    <div class="mb-3 align-self-start" id="statistics2"></div>
    <div class="mb-3 align-self-start" id="statistics3"></div>
    <div class="home">
        <model :showModelFive="this.showModelFive" @cancel="this.showModelFive=false"></model>
    </div>
</template>

<script>
    import axios from "axios";
    import * as echarts from 'echarts';
    import Model from "@/components/Model";
    import $ from "jquery";
    import cookies from "vue-cookies";
    export default {
        name: "",
        components:{Model},
        data() {
            return {
                publicPath: process.env.BASE_URL,
                showModelFive:false
            }
        },
        methods:{
            askDownload() {
                if (!cookies.get("is_login")){
                    this.showModelFive=true
                }else {
                    window.location.href = this.publicPath + 'pdf_download'
                }
            },
            returnBack(){
                window.location.href="/home"
            }
        },
        created() {
            let arg=JSON.parse(localStorage.getItem('key'))
            console.log(this.publicPath)
            localStorage.clear()
            let keys=Object.keys(arg)
            keys.pop()
            let values=Object.values(arg)
            values.pop()
            const r=[]
            const f=[]
            const m=[]
            for (var i=1;i<arg.r.r.length;i++){
                r.push(Math.round(parseFloat(arg.r.r[i])))
                f.push(Math.round(parseFloat(arg.r.f[i])))
                m.push(Math.round(parseFloat(arg.r.m[i])))
            }
            function generator() {
                const data = []
                const color = [['#ced413', '#d59b33'],['#78cd1b','#e36b02'], ['#cc3833','#13D4C4'],['#78CD1B','#E30202']]
                for (var i = 0; i < keys.length/2; i++) {
                    if (keys.length%2==1){
                        if (i!=Math.round(keys.length/2)-1){
                            data.push({
                                name: i,
                                value: values[i]+values[keys.length-i-1],
                                color: color[i],
                                children:[
                                    {name: keys[i],value: values[i]},
                                    {name: keys[keys.length-i-1], value: values[keys.length-i-1]}
                                ]
                            })
                        }else{
                            data.push({
                                name: keys[i],
                                value: values[i],
                                color: color[i]
                            })
                        }

                    }else{
                        data.push({
                            name: i,
                            value: values[i]+values[keys.length-i-1],
                            color: color[i],
                            children:[
                                {name: keys[i],value: values[i]},
                                {name: keys[keys.length-i-1], value: values[keys.length-i-1]}
                            ]
                        })
                    }

                }
                return data
            }
            const option = {
                title:{
                    text:'Target customer group Analysis',
                    left:'center'
                },
                tooltip:{
                    showContent: true
                },
                toolbox: {
                    show: true,
                    right: '20px',
                    feature: {
                        // 下载保存为图片
                        saveAsImage: {
                            show: true,
                            title: 'Download image'
                        }
                    }
                },
                series: [
                    {
                        type: 'treemap',
                        data: generator()
                    }
                ]
            };
            const option1 ={
                title: [
                    {text: 'Statistics data: Recency', left: 'center'},
                    {
                        text: 'upper: Q3 + 1.5 * IQR \nlower: Q1 - 1.5 * IQR',
                        borderColor: '#999',
                        borderWidth: 1,
                        textStyle: {
                            fontWeight: 'normal',
                            fontSize: 14,
                            lineHeight: 20
                        },
                        left: '10%',
                        top: '90%'
                    }
                ],
                dataset: [
                    {source: [r]},
                    {transform: {type: 'boxplot', config: { itemNameFormatter: 'expr {value}' }}},
                    {fromDatasetIndex: 1, fromTransformResult: 1}],
                tooltip: {trigger: 'item', axisPointer: {type: 'shadow'}},
                grid: {left: '10%', right: '10%', bottom: '15%'},
                xAxis: {type: 'category',
                    boundaryGap: true,
                    nameGap: 30,
                    splitArea: {
                        show: false},
                    splitLine: {show: false}},
                yAxis: {
                    type: 'value',
                    splitArea: {
                        show: true
                    },
                },
                series: [
                    {
                        name: 'boxplot',
                        type: 'boxplot',
                        datasetIndex: 1
                    },
                    {
                        name: 'outlier',
                        type: 'scatter',
                        datasetIndex: 2
                    }
                ]
            }
            const option2 ={
                title: [
                    {text: 'Statistics data: Frequency', left: 'center'},
                    {
                        text: 'upper: Q3 + 1.5 * IQR \nlower: Q1 - 1.5 * IQR',
                        borderColor: '#999',
                        borderWidth: 1,
                        textStyle: {
                            fontWeight: 'normal',
                            fontSize: 14,
                            lineHeight: 20
                        },
                        left: '10%',
                        top: '90%'
                    }
                ],
                dataset: [
                    {source: [f]},
                    {transform: {type: 'boxplot', config: { itemNameFormatter: 'expr {value}' }}},
                    {fromDatasetIndex: 1, fromTransformResult: 1}],
                tooltip: {trigger: 'item', axisPointer: {type: 'shadow'}},
                grid: {left: '10%', right: '10%', bottom: '15%'},
                xAxis: {type: 'category',
                    boundaryGap: true,
                    nameGap: 30,
                    splitArea: {
                        show: false},
                    splitLine: {show: false}},
                yAxis: {
                    type: 'value',
                    splitArea: {
                        show: true
                    },
                    dataZoom:{
                        show: true,

                    }
                },
                series: [
                    {
                        name: 'boxplot',
                        type: 'boxplot',
                        datasetIndex: 1
                    },
                    // {
                    //     name: 'outlier',
                    //     type: 'scatter',
                    //     datasetIndex: 2
                    // }
                ]
            }
            const option3={
                title:
                    [
                    {text: 'Statistics data: Monetary Value', left: 'center'},
                    {
                        text: 'upper: Q3 + 1.5 * IQR \nlower: Q1 - 1.5 * IQR',
                        borderColor: '#999',
                        borderWidth: 1,
                        textStyle: {
                            fontWeight: 'normal',
                            fontSize: 14,
                            lineHeight: 20
                        },
                        left: '10%',
                        top: '90%'
                    }
                ],
                dataset: [
                    {source: [m]},
                    {transform: {type: 'boxplot', config: { itemNameFormatter: 'expr {value}' }}},
                    {fromDatasetIndex: 1, fromTransformResult: 1}],
                tooltip: {trigger: 'item', axisPointer: {type: 'shadow'}},
                grid: {left: '10%', right: '10%', bottom: '15%'},
                xAxis: {type: 'category',
                    boundaryGap: true,
                    nameGap: 30,
                    splitArea: {
                        show: false},
                    splitLine: {show: false}},
                yAxis: {
                    type: 'value',
                    splitArea: {
                        show: true
                    },
                    dataZoom:{
                        show: true,

                    }
                },
                series: [
                    {
                        name: 'boxplot',
                        type: 'boxplot',
                        datasetIndex: 1
                    },
                    // {
                    //     name: 'outlier',
                    //     type: 'scatter',
                    //     datasetIndex: 2
                    // }
                ]
            }
            $(document).ready(function(){
                const chart=echarts.init(document.getElementById("main"))
                const chart1=echarts.init(document.getElementById("statistics1"))
                const chart2=echarts.init(document.getElementById('statistics2'))
                const chart3=echarts.init(document.getElementById("statistics3"))
                chart1.setOption(option1)
                chart2.setOption(option2)
                chart3.setOption(option3)
                chart.setOption(option)

                // const canvas = document.querySelector("#main canvas")
                // const dataUrl = canvas.toDataURL();
                // $("#downloadImg").on("click",function(){
                //     doViewAndPrint(dataUrl)
                // })
                // function doViewAndPrint(canvasUrl) {
                //     const domPrint = document.createElement('img');
                //     domPrint.src = canvasUrl;
                //     let page = window.open('', '_blank'); // 打开一个新窗口，用于打印
                //     page.document.body.appendChild(domPrint);
                //
                //     domPrint.onload = function () {
                //         page.print(); // 打印
                //         page.close(); // 关闭打印窗口
                //     };
                // }
            });
        }
    }
</script>

<style scoped>
    #main{
        float: left;
        width: 60%;
        height:400px;
        margin: 20px;
    }
    #statistics1{
        float: left;
        width: 30%;
        height: 400px;
        margin: 20px
    }
    #statistics2{
        float: left;
        width: 30%;
        height: 400px;
        margin: 20px
    }
    #statistics3{
        float:left;
        width: 30%;
        height: 400px;
        margin: 20px
    }
    #buttons{
        float: left;
        width: 20%;
        height: 200px;
        margin: 20px;
        margin-top: 50px
    }
    #Img{
        width: 20%;
        margin: 20px;
        margin-top: 40px;
        float: left;
    }
</style>