<template>
    <input id="range" type="range" min="" max="" v-model="price">
    <div class="mb-3 align-self-start" id="SDChart"></div>
    <div id="rangeBox">
        <span> You can pull the slide block to see your profit:</span><br>
        <span> Price : £ {{price}} </span><br>
        <span> Revenue : £ {{revenue}} </span>
    </div>
    <div id="buttons">
<!--        <button id="downloadImg" style="margin: 5px;border-radius: 8px" class="btn-primary">Download Charts</button><br>-->
        <button id="downloadResults" style="margin: 5px;border-radius: 8px" class="btn-primary" @click="askDownload">Download Results</button><br>
        <button id="return" style="margin: 5px;border-radius: 8px" class="btn-primary" @click="returnBack">Return back to main menu</button>
    </div>
    <div class="mb-3 align-self-start" id="Statistics1"></div>
    <div class="mb-3 align-self-start" id="Statistics2"></div>
</template>

<script>
    // 引入 echarts 核心模块，核心模块提供了 echarts 使用必须要的接口。
    import * as echarts from 'echarts';
    import $ from 'jquery'
    export default {
        name: "SDChart",
        data(){
            return{
                publicPath: process.env.BASE_URL,
                a: 0,
                b: 0,
                price: 0,
                revenue: 0
            }
        },
        watch:{
            price(){
                this.revenue=Math.round(Math.exp((Math.log(this.price)-this.b)/this.a)*this.price)
            },
        },
        methods:{
            askDownload() {
                window.location.href = this.publicPath + 'pdf_download'
            },
            returnBack(){
                window.location.href="/home"
            }
        },
        created() {
            let arg=JSON.parse(localStorage.getItem('key'))
            localStorage.clear()

            this.a=arg.a
            this.b=arg.b
            const p=[]
            const q=[]
            for (var i=0;i<arg.g.p.length;i++){
                p.push(parseFloat(arg.g.p[i]))
                q.push(parseFloat(arg.g.q[i]))
            }

            function func(x) {
                return Math.exp(parseFloat(arg.a)*Math.log(x)+parseFloat(arg.b))
            }
            function generateData() {
                let data = [];
                for (let i = arg.c; i <= arg.d; i += 0.1) {
                    data.push([i, func(i)]);
                }
                return data;
            }
            const option1 = {
                title:{
                  text:'Demand Curve chart',
                  left:'center'
                },
                tooltip : {
                    trigger: 'axis',
                    showContent: true,
                    formatter: function (params){
                        let str = Math.round(params[0].data[0]) + "<br />";
                        params.forEach((item) => {
                            str += '<span style="display:inline-block;margin-right:5px;border-radius:50%;width:10px;height:10px;left:5px;background-color:'+item.color+'"></span>' + 'Revenue' + " : " + Math.round(item.data[0]*item.data[1]) + "<br />";
                        });
                        return str;
                    },
                    axisPointer: {
                        label: {
                            backgroundColor: '#6a7985'
                        }
                    },
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
                animation: false,
                grid: {
                    top: 50,
                    left: 50,
                    right: 65,
                    bottom: 50
                },
                xAxis: {
                    name: 'Demand',
                    min: arg.c,
                    max: arg.d,
                    minorTick: {
                        show: true
                    },
                    minorSplitLine: {
                        show: true
                    }
                },
                yAxis: {
                    name: 'Price',
                    min: arg.e,
                    max: arg.f,
                    minorTick: {
                        show: true
                    },
                    minorSplitLine: {
                        show: true
                    }
                },
                series: [
                    {
                        type: 'line',
                        showSymbol: false,
                        clip: false,
                        data: generateData(),
                    }
                ]

            };
            const option2 = {
                title: [
                    {text: 'Statistics data: Price', left: 'center'},
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
                    {source: [p]},
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
                    dataZoom:[{
                        show: true,
                        start: 0,
                        end: 20
                    },{
                        start:0,
                        end:20
                    }]
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
            };
            const option3 = {
                title: [
                    {text: 'Statistics data: Quantity', left: 'center'},
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
                    {source: [q]},
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
                const chart1=echarts.init(document.getElementById("SDChart"))
                const chart2=echarts.init(document.getElementById("Statistics1"))
                const chart3=echarts.init(document.getElementById("Statistics2"))
                chart1.setOption(option1)
                chart2.setOption(option2)
                chart3.setOption(option3)
                $('#range').attr('min',arg.e)
                $('#range').attr('max',arg.f)

                // const canvas=document.querySelector("#SDChart canvas")
                // const dataUrl = canvas.toDataURL();
                // $('#downloadImg').on("click",function (){
                //     doViewAndPrint(dataUrl)
                // })
                //
                // // 预览：因为使用window.print火狐无法预览，因此采用新打开一个窗口的方式用来展示被打印的内容
                // // 打印指定区域内容：通过只将需打印的内容添加到新窗口中，实现打印指定区域
                // function doViewAndPrint(canvasUrl) {
                //     const domPrint = document.createElement('img');
                //     domPrint.src = canvasUrl;
                //     console.log(canvasUrl)
                //     console.log(123)
                //     let page = window.open('', '_blank'); // 打开一个新窗口，用于打印
                //     page.document.body.appendChild(domPrint);
                //
                //     domPrint.onload = function () {
                //         page.print(); // 打印
                //         page.close(); // 关闭打印窗口
                //     };
                // }
            });

        },
    }
</script>

<style lang="scss" scoped>
#SDChart{
    float: left;
    width: 60%;
    height: 400px;
    margin-top: 20px;
}
#Statistics1{
    float: left;
    width: 40%;
    height: 500px;
}
#Statistics2{
    float: left;
    width: 40%;
    height: 500px;
}
#buttons{
    float: left;
    width: 20%;
    height: 200px;
    margin: 20px;
    margin-top: 100px;
    margin-left: 50px;
}
#rangeBox{
    float: left;
    width: 20%;
    height: 50px;
    margin: 20px;
    margin-top: 100px;
    margin-left: 50px;
}
input[type=range]{
    float: left;
    width: 16px;
    height: 350px;
    margin: 20px;
    margin-top: 40px;
    -webkit-appearance: slider-vertical;
}
</style>