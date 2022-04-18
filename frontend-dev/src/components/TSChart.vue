<template>
    <div class="mb-3 align-self-start" id="main"></div>
    <div class="mb-3 align-self-start" id="params">
        <form method="post">
            <input type="text">
        </form>
    </div>
    <div id="buttons">
        <button id="downloadImg">Download Charts</button>
        <button id="downloadResults">Download Results</button>
        <button id="return">Return back to main menu</button>
    </div>
    <div class="mb-3 align-self-start" id="statistics1"></div>
    <div class="mb-3 align-self-start" id="statistics2"></div>
</template>

<script>
    import $ from 'jquery'
    import * as echarts from "echarts";
    export default {
        name: "TSChart",
        data(){
            return{
                codeImg: "",
                publicPath: process.env.BASE_URL,
            }
        },
        created() {
            let funcNum=this.$route.query.funcNum
            console.log(funcNum)
            let arg=JSON.parse(localStorage.getItem('key'))
            localStorage.clear()
            console.log(arg)
            if (parseFloat(funcNum)==3.1){
                let data1=[]
                let data2=[]
                let open=[],high=[],low=[],close=[], adj_close=[],volume=[]
                let base=+new Date(2014,9,17)
                let oneDay = 24 * 3600 *1000
                for (var i=0;i<arg.y1.length;i++){
                    let now = new Date((base+=oneDay))
                    console.log(now)
                    data1.push([+now,arg.y1[i]])
                    data2.push([+now,arg.y2[i]])
                }
                for(var i=0;i<arg.open.length;i++){
                    open.push(arg.open[i])
                    high.push(arg.high[i])
                    low.push(arg.low[i])
                    close.push(arg.close[i])
                    adj_close.push(arg.adjClose[i])
                    volume.push(arg.volume[i])
                }
                const option = {
                    toolbox: {
                        show:true,
                        right: '20px',
                        feature: {
                            dataZoom: {
                                yAxisIndex: 'none'
                            },
                            restore: {},
                            saveAsImage: {
                                show:true,
                                title: 'Download image'
                            }
                        }
                    },
                    title: {
                        text: 'Dynamic Data & Time Axis'
                    },
                    tooltip: {
                        trigger: 'axis',
                        formatter: function (params) {
                            console.log("params:"+params)
                            params = params[0];
                            console.log("params:"+params)
                            var date = new Date(params.name);
                            console.log(date)
                            return (
                                date.getDate() +
                                '/' +
                                (date.getMonth() + 1) +
                                '/' +
                                date.getFullYear() +
                                ' : ' +
                                params.value[1]
                            );
                        },
                        axisPointer: {
                            animation: false
                        }
                    },
                    xAxis: {
                        type: 'time',
                        splitLine: {
                            show: false
                        }
                    },
                    yAxis: {
                        type: 'value',
                        boundaryGap: [0, '100%'],
                        splitLine: {
                            show: false
                        }
                    },
                    dataZoom: [
                        {
                            type: 'inside',
                            start: 0,
                            end: 20
                        },
                        {
                            start: 0,
                            end: 20
                        }
                    ],
                    series: [
                        {
                            name: 'One',
                            type: 'line',
                            showSymbol: false,
                            data: data1
                        },
                        {
                            name: 'Two',
                            type: 'line',
                            showSymbol: false,
                            data: data2
                        }
                    ]
                };
                const option1={
                    title: [
                        {text: 'Statistics data', left: 'center'},
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
                        {source: [open,high,low,close,adj_close]},
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
                const option2={
                    title: [
                        {text: 'Statistics data', left: 'center'},
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
                        {source: [volume]},
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
                $(document).ready(function(){
                    const chart1=echarts.init(document.getElementById("main"))
                    const chart2=echarts.init(document.getElementById("statistics1"))
                    const chart3=echarts.init(document.getElementById("statistics2"))
                    chart1.setOption(option)
                    chart2.setOption(option1)
                    chart3.setOption(option2)

                    const canvas = document.querySelector("#main canvas")
                    const dataUrl = canvas.toDataURL();
                    $('#downloadImg').on("click",function(){
                        doViewAndPrint(dataUrl)
                    })
                })
            }
            else if (parseFloat(funcNum)==3.2){
                const y1=[],y2=[],y3=[],value=[]
                let base=+new Date(1970,1,1)
                let oneDay = 24 * 3600 *1000
                for (var i=0;i<arg.y1.length;i++){
                    let now = new Date((base+=oneDay))
                    y1.push([+now,arg.y1[i]])
                }
                for (var i=0;i<arg.y2.length;i++){
                    let now = new Date((base+=oneDay))
                    y2.push([+now,arg.y2[i]])
                    y3.push([+now,arg.y3[i]])
                }
                for (var i=0;i<arg.value.length;i++){
                    value.push(arg.value[i])
                }
                const option1={
                    toolbox: {
                        show:true,
                        right: '20px',
                        feature: {
                            dataZoom: {
                                yAxisIndex: 'none'
                            },
                            restore: {},
                            saveAsImage: {
                                show:true,
                                title: 'Download image'
                            }
                        }
                    },
                    title: {
                        text: 'Dynamic Data & Time Axis'
                    },
                    tooltip: {
                        trigger: 'axis',
                        formatter: function (params) {
                            console.log("params:"+params)
                            params = params[0];
                            console.log("params:"+params)
                            var date = new Date(params.name);
                            console.log(date)
                            return (
                                date.getDate() +
                                '/' +
                                (date.getMonth() + 1) +
                                '/' +
                                date.getFullYear() +
                                ' : ' +
                                params.value[1]
                            );
                        },
                        axisPointer: {
                            animation: false
                        }
                    },
                    xAxis: {
                        type: 'time',
                        splitLine: {
                            show: false
                        }
                    },
                    yAxis: {
                        type: 'value',
                        boundaryGap: [0, '100%'],
                        splitLine: {
                            show: false
                        }
                    },
                    dataZoom: [
                        {
                            type: 'inside',
                            start: 0,
                            end: 20
                        },
                        {
                            start: 0,
                            end: 20
                        }
                    ],
                    series: [
                        {
                            name: 'One',
                            type: 'line',
                            showSymbol: false,
                            data: y1
                        },
                        {
                            name: 'Two',
                            type: 'line',
                            showSymbol: false,
                            data: y2
                        },
                        {
                            name: 'Two',
                            type: 'line',
                            showSymbol: false,
                            data: y3
                        }
                    ]
                }
                const option2={
                    title: [
                        {text: 'Statistics data', left: 'center'},
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
                        {source: [value]},
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
                $(document).ready(function(){
                    const chart1=echarts.init(document.getElementById("main"))
                    const chart2=echarts.init(document.getElementById("statistics1"))
                    chart1.setOption(option1)
                    chart2.setOption(option2)

                    const canvas = document.querySelector("#main canvas")
                    const dataUrl = canvas.toDataURL();
                    $('#downloadImg').on("click",function(){
                        doViewAndPrint(dataUrl)
                    })
                })
            }


            function doViewAndPrint(canvasUrl) {
                const domPrint = document.createElement('img');
                domPrint.src = canvasUrl;
                let page = window.open('', '_blank'); // 打开一个新窗口，用于打印
                page.document.body.appendChild(domPrint);

                domPrint.onload = function () {
                    page.print(); // 打印
                    page.close(); // 关闭打印窗口
                };
            }

        },
        methods:{
            askDownload() {
                window.location.href = this.publicPath + 'pdf_download'
            },
            // getImgCode(){
            //     let url=localStorage.getItem('key')
            //     localStorage.clear()
            //     this.codeImg="data:image/png;base64,"+url
            // }
        }
    }
</script>

<style scoped>
    #main{
        float: left;
        width: 60%;
        height: 400px;
        margin: 20px;
    }
    #params{
        float: left;
        width: 20%;
        height: 100px;
        margin: 20px;
        margin-top: 100px;
        margin-left: 50px;
    }
    #buttons{
        float: left;
        width: 20%;
        height: 200px;
        margin: 20px;
        margin-top: 100px;
        margin-left: 50px;
    }
    #statistics1{
        float: left;
        width: 40%;
        height: 400px;
        margin: 20px
    }
    #statistics2{
        float: left;
        width: 40%;
        height: 400px;
        margin: 20px
    }
</style>