<template>
    <div class="mb-3 align-self-start" id="main"></div>
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

            const option = {
                tooltip : {
                    trigger: 'axis',
                    showContent: true,
                    enterable: true,
                    formatter: function (params){
                        let str = params[0].data[0] + "<br />";
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

            $(document).ready(function(){
                const chart=echarts.init(document.getElementById("main"))
                chart.setOption(option)
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