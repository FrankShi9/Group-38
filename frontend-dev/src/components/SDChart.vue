<template>
    <div class="mb-3 align-self-start" id="SDChart"></div>
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
            }
        },
        created() {
            let url = this.$route.query
            function func(x) {
                return Math.exp(parseFloat(url.a)*Math.log(x)+parseFloat(url.b))
            }
            function generateData() {
                let data = [];
                for (let i = 16; i <= 23; i += 0.1) {
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
                            str +=
                                '<span style="display:inline-block;margin-right:5px;border-radius:50%;width:10px;height:10px;left:5px;background-color:'+item.color+'"></span>' + 'Revenue' + " : " + Math.round(item.data[0]*item.data[1]) + "<br />";
                        });
                        return str;
                    },
                    axisPointer: {
                        //type: 'cross',
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
                    min: url.c,
                    max: url.d,
                    minorTick: {
                        show: true
                    },
                    minorSplitLine: {
                        show: true
                    }
                },
                yAxis: {
                    name: 'y',
                    min: url.e,
                    max: url.f,
                    minorTick: {
                        show: true
                    },
                    minorSplitLine: {
                        show: true
                    }
                },
                // dataZoom: [
                //     {
                //         show: true,
                //         //type: 'inside',
                //         filterMode: 'none',
                //         xAxisIndex: [0],
                //         startValue: -20,
                //         endValue: 20
                //     },
                //     {
                //         show: true,
                //         //type: 'inside',
                //         filterMode: 'none',
                //         yAxisIndex: [0],
                //         startValue: -20,
                //         endValue: 20
                //     }
                // ],
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
                        source: [
                            [850, 740, 900, 1070, 930, 850, 950, 980, 980, 880, 1000, 980, 930, 650, 760, 810, 1000, 1000, 960, 960],
                            [960, 940, 960, 940, 880, 800, 850, 880, 900, 840, 830, 790, 810, 880, 880, 830, 800, 790, 760, 800],
                            [880, 880, 880, 860, 720, 720, 620, 860, 970, 950, 880, 910, 850, 870, 840, 840, 850, 840, 840, 840],
                            [890, 810, 810, 820, 800, 770, 760, 740, 750, 760, 910, 920, 890, 860, 880, 720, 840, 850, 850, 780],
                            [890, 840, 780, 810, 760, 810, 790, 810, 820, 850, 870, 870, 810, 740, 810, 940, 950, 800, 810, 870]
                        ]
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
            });

        },
        updated() {

        }
    }
</script>

<style lang="scss" scoped>
#main{
    width: 1000px;
    height:400px;
    margin: 20px;
}
</style>