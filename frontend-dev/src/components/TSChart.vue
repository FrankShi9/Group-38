<template>
    <div class="mb-3 align-self-start" id="main"></div>
    <div class="mb-3 align-self-start" id="params">
        <span>Please input future days to print</span>
        <input type="text" min="0" max="30" style="width: 50%" v-model="futureDays">
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        <button type="submit" class="btn-primary" style="margin: 5px;border-radius: 8px" @click="Predict">Predict</button>
        <span v-show="showOne">Prediction is processing...</span>
        <span v-show="showTwo">Prediction complete !</span>
    </div>
    <div id="buttons">
        <button id="downloadResults" style="margin: 5px ;border-radius: 8px" class="btn-primary" @click="askDownload">Download Results</button>
        <button id="return" style="margin: 5px ;border-radius: 8px" class="btn-primary" @click="returnBack">Return back to main menu</button>
    </div>
    <div class="mb-3 align-self-start" id="statistics1"></div>
    <div class="mb-3 align-self-start" id="statistics2"></div>
</template>

<script>
    import $ from 'jquery'
    import * as echarts from "echarts";
    import axios from "axios";

    let chart1=undefined
    let base=undefined
    export default {
        name: "TSChart",
        data(){
            return{
                codeImg: "",
                funcNum: 0,
                publicPath: process.env.BASE_URL,
                futureDays: 0,
                showOne: false,
                showTwo: false,
                startTime: ""
            }
        },
        created() {
            let funcNum=this.$route.query.funcNum
            this.funcNum=funcNum
            console.log(funcNum)
            let arg=JSON.parse(localStorage.getItem('key'))
            localStorage.clear()
            console.log(arg)
            let y1=[],y2=[],y3=[],value=[]
            let oneDay = 24 * 3600 * 1000
            base=+new Date(arg.start)
            this.startTime=+new Date(arg.start)
            for (var i=0;i<arg.y1.length;i++){
                let now = new Date((base+=oneDay))
                y1.push([+now,arg.y1[i]])
                value.push(arg.y1[i])
            }
            // if (parseFloat(funcNum)==3.1){
            //     for (var i=0;i<arg.y1.length;i++){
            //         let now = new Date((base+=oneDay))
            //         y1.push([+now,arg.y1[i]])
            //         value.push(arg.y1[i])
            //     }
            //     // const option = {
            //     //     toolbox: {
            //     //         show:true,
            //     //         right: '20px',
            //     //         feature: {
            //     //             dataZoom: {
            //     //                 yAxisIndex: 'none'
            //     //             },
            //     //             restore: {},
            //     //             saveAsImage: {
            //     //                 show:true,
            //     //                 title: 'Download image'
            //     //             }
            //     //         }
            //     //     },
            //     //     title: {
            //     //         text: 'Time Series Prediction'
            //     //     },
            //     //     tooltip: {
            //     //         trigger: 'axis',
            //     //         // formatter: function (params) {
            //     //         //     console.log("params:"+params)
            //     //         //     params = params[0];
            //     //         //     console.log("params:"+params)
            //     //         //     var date = new Date(params.name);
            //     //         //     console.log(date)
            //     //         //     return (
            //     //         //         date.getDate() +
            //     //         //         '/' +
            //     //         //         (date.getMonth() + 1) +
            //     //         //         '/' +
            //     //         //         date.getFullYear() +
            //     //         //         ' : ' +
            //     //         //         params.value[1]
            //     //         //     );
            //     //         // },
            //     //         axisPointer: {
            //     //             animation: false
            //     //         }
            //     //     },
            //     //     xAxis: {
            //     //         type: 'time',
            //     //         splitLine: {
            //     //             show: false
            //     //         }
            //     //     },
            //     //     yAxis: {
            //     //         type: 'value',
            //     //         boundaryGap: [0, '100%'],
            //     //         splitLine: {
            //     //             show: false
            //     //         }
            //     //     },
            //     //     dataZoom: [
            //     //         {
            //     //             type: 'inside',
            //     //             start: 0,
            //     //             //end: 20
            //     //         },
            //     //         {
            //     //             start: 0,
            //     //             //end: 20
            //     //         }
            //     //     ],
            //     //     series: [
            //     //         {
            //     //             name: 'One',
            //     //             type: 'line',
            //     //             showSymbol: false,
            //     //             data: y1
            //     //         }
            //     //     ]
            //     // };
            //     // const option1={
            //     //     title: [
            //     //         {text: 'Statistics data: Value', left: 'center'},
            //     //         {
            //     //             text: 'upper: Q3 + 1.5 * IQR \nlower: Q1 - 1.5 * IQR',
            //     //             borderColor: '#999',
            //     //             borderWidth: 1,
            //     //             textStyle: {
            //     //                 fontWeight: 'normal',
            //     //                 fontSize: 14,
            //     //                 lineHeight: 20
            //     //             },
            //     //             left: '10%',
            //     //             top: '90%'
            //     //         }
            //     //     ],
            //     //     dataset: [
            //     //         {source: [value]},
            //     //         {transform: {type: 'boxplot', config: { itemNameFormatter: 'expr {value}' }}},
            //     //         {fromDatasetIndex: 1, fromTransformResult: 1}],
            //     //     tooltip: {trigger: 'item', axisPointer: {type: 'shadow'}},
            //     //     grid: {left: '10%', right: '10%', bottom: '15%'},
            //     //     xAxis: {type: 'category',
            //     //         boundaryGap: true,
            //     //         nameGap: 30,
            //     //         splitArea: {
            //     //             show: false},
            //     //         splitLine: {show: false}},
            //     //     yAxis: {
            //     //         type: 'value',
            //     //         splitArea: {
            //     //             show: true
            //     //         },
            //     //     },
            //     //     series: [
            //     //         {
            //     //             name: 'boxplot',
            //     //             type: 'boxplot',
            //     //             datasetIndex: 1
            //     //         },
            //     //         {
            //     //             name: 'outlier',
            //     //             type: 'scatter',
            //     //             datasetIndex: 2
            //     //         }
            //     //     ]
            //     // }
            //     // $(document).ready(function(){
            //     //     chart1=echarts.init(document.getElementById("main"))
            //     //     const chart2=echarts.init(document.getElementById("statistics1"))
            //     //     chart1.setOption(option)
            //     //     chart2.setOption(option1)
            //     //
            //     //     // const canvas = document.querySelector("#main canvas")
            //     //     // const dataUrl = canvas.toDataURL();
            //     //     // $('#downloadImg').on("click",function(){
            //     //     //     doViewAndPrint(dataUrl)
            //     //     // })
            //     // })
            // } else if (parseFloat(funcNum)==3.2) {
            //     for (var i = 0; i < arg.y1.length; i++) {
            //         let now = new Date((base += oneDay))
            //         y1.push([+now, arg.y1[i]])
            //     }
            //     for (var i = 0; i < arg.y2.length; i++) {
            //         let now = new Date((base += oneDay))
            //         y2.push([+now, arg.y2[i]])
            //         y3.push([+now, arg.y3[i]])
            //     }
            //     for (var i = 0; i < arg.value.length; i++) {
            //         value.push(arg.value[i])
            //     }
            // }

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
                    // formatter: function (params) {
                    //     console.log("params:"+params)
                    //     params = params[0];
                    //     console.log("params:"+params)
                    //     var date = new Date(params.name);
                    //     console.log(date)
                    //     return (
                    //         date.getDate() +
                    //         '/' +
                    //         (date.getMonth() + 1) +
                    //         '/' +
                    //         date.getFullYear() +
                    //         ' : ' +
                    //         params.value[1]
                    //     );
                    // },
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
                        //end: 20
                    },
                    {
                        start: 0,
                        //end: 20
                    }
                ],
                series: [
                    {
                        name: 'One',
                        type: 'line',
                        showSymbol: false,
                        data: y1
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
                chart1=echarts.init(document.getElementById("main"))
                const chart2=echarts.init(document.getElementById("statistics1"))
                chart1.setOption(option1)
                chart2.setOption(option2)

                // const canvas = document.querySelector("#main canvas")
                // const dataUrl = canvas.toDataURL();
                // $('#downloadImg').on("click",function(){
                //     doViewAndPrint(dataUrl)
                // })
            })

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
            returnBack(){
                window.location.href = '/home'
            },
            Predict(){
                let formData=new FormData()
                formData.append('future',this.futureDays)
                formData.append('funcNum',this.funcNum)
                this.showTwo=false
                this.showOne=true
                axios.post('',formData,{
                    headers: {
                        'Content-Type': 'multipart/form-data'
                    }
                }).then((response) => {
                    this.showOne=false
                    this.showTwo=true
                    let data=JSON.stringify(response.data)
                    let arg=JSON.parse(data)
                    console.log(arg)
                    let y1=[],y2=[],y3=[]
                    let oneDay=24 * 3600 *1000
                    let offset= 4*arg.y2.length
                    base-=offset*oneDay
                    if (base < this.startTime){
                        base=this.startTime
                    }
                    let i=arg.y1.length-offset
                    if (i<0){ i=0 }
                    for (;i<arg.y1.length;i++){
                        let now = new Date((base+=oneDay))
                        y1.push([+now,arg.y1[i]])
                    }
                    base-=oneDay
                    for (i=0;i<arg.y2.length;i++){
                        let now = new Date((base+=oneDay))
                        y2.push([+now,arg.y2[i]])
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
                            text: 'Time Series Prediction'
                        },
                        tooltip: {
                            trigger: 'axis',
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
                            },
                            {
                                start: 0,
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
                            }
                        ]
                    };
                    chart1.setOption(option)
                })
            }
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