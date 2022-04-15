<template>
    <div class="mb-3 align-self-start" id="SDChart"></div>
    <input id="range" type="range" min="" max="" v-model="price"><span> Price : {{price}}; Revenue : {{revenue}}</span>
    <div class="mb-3 align-self-start" id="Statistics"></div>
</template>

<script>
    // 引入 echarts 核心模块，核心模块提供了 echarts 使用必须要的接口。
    import * as echarts from 'echarts';
    import $ from 'jquery'
    export default {
        name: "SDChart",
        data(){
            return{
                a: 0,
                b: 0,
                price: 0,
                revenue: 0
            }
        },
        watch:{
            price(){
                this.revenue=Math.round(Math.exp((Math.log(this.price)-this.b)/this.a)*this.price)
            }
        },
        created() {
            let url = decodeURIComponent(this.$route.query.arg)
            let arg=JSON.parse(url)

            this.a=arg.a
            this.b=arg.b

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
                animation: false,
                grid: {
                    top: 40,
                    left: 50,
                    right: 40,
                    bottom: 50
                },
                xAxis: {
                    name: 'x',
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
                    name: 'y',
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
                    {
                        text: 'Michelson-Morley Experiment',
                        left: 'center'
                    },
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
                    {
                    // prettier-ignore
                        source:generateData()
                    },
                    {
                        transform: {
                            type: 'boxplot',
                            config: { itemNameFormatter: 'expr {value}' }
                        }
                    },
                    {
                        fromDatasetIndex: 1,
                        fromTransformResult: 1
                    }
                ],
                tooltip: {
                    trigger: 'item',
                        axisPointer: {
                        type: 'shadow'
                    }
                },
                grid: {
                    left: '10%',
                    right: '10%',
                    bottom: '15%'
                },
                xAxis: {
                    type: 'category',
                        boundaryGap: true,
                        nameGap: 30,
                        splitArea: {
                        show: false
                    },
                    splitLine: {
                        show: false
                    }
                },
                yAxis: {
                    type: 'value',
                        name: 'km/s minus 299,000',
                        splitArea: {
                        show: true
                    }
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
            $(document).ready(function(){
                const chart1=echarts.init(document.getElementById("SDChart"))
                const chart2=echarts.init(document.getElementById("Statistics"))
                chart1.setOption(option1)
                chart2.setOption(option2)
                $('#range').attr('min',arg.e)
                $('#range').attr('max',arg.f)
            });

        },
    }
</script>

<style lang="scss" scoped>
#SDChart{
    width: 1000px;
    height:400px;
    margin: 20px;
}
#Statistics{
    width: 400px;
    height: 400px;
}
</style>