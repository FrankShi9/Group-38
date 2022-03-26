<template>
    <div class="mb-3 align-self-start" id="main"></div>
    <div class="mb-3 align-self-start">
        <input type="range">
    </div>
</template>

<script>
    // 引入 echarts 核心模块，核心模块提供了 echarts 使用必须要的接口。
    import * as echarts from 'echarts/core';
    // 引入柱状图图表，图表后缀都为 Chart
    import { BarChart } from 'echarts/charts';
    // 引入提示框，标题，直角坐标系，数据集，内置数据转换器组件，组件后缀都为 Component
    import {
        TitleComponent,
        TooltipComponent,
        GridComponent,
        DatasetComponent,
        TransformComponent
    } from 'echarts/components';
    // 标签自动布局，全局过渡动画等特性
    import { LabelLayout, UniversalTransition } from 'echarts/features';
    // 引入 Canvas 渲染器，注意引入 CanvasRenderer 或者 SVGRenderer 是必须的一步
    import { CanvasRenderer } from 'echarts/renderers';

    // 注册必须的组件
    echarts.use([
        TitleComponent,
        TooltipComponent,
        GridComponent,
        DatasetComponent,
        TransformComponent,
        BarChart,
        LabelLayout,
        UniversalTransition,
        CanvasRenderer
    ]);

    import $ from 'jquery'



    export default {
        name: "SDChart",
        data(){
            return{
                chart: undefined,
                coefficient : undefined
            }
        },
        created() {
            let url = this.$route.query
            this.coefficient=url.k;

            function func(x) {
                return url.k/x
            }

            function generateData() {
                let data = [];
                for (let i = 0; i <= 200; i += 0.1) {
                    data.push([i, func(i)]);
                }
                return data;
            }

            const option = {
                animation: false,
                grid: {
                    top: 40,
                    left: 50,
                    right: 40,
                    bottom: 50
                },
                xAxis: {
                    name: 'x',
                    min: 0,
                    max: 20,
                    minorTick: {
                        show: true
                    },
                    minorSplitLine: {
                        show: true
                    }
                },
                yAxis: {
                    name: 'y',
                    min: 0,
                    max: 20,
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
                        areaStyle:{

                        }
                    }
                ]
            };

            $(document).ready(function(){
                this.chart=echarts.init(document.getElementById("main"))
                this.chart.setOption(option)
                window.onresize=function(){
                    this.chart.resize()
                }

                // this.chart.getZr().on('click',function (params){
                //     console.log(params)
                // })
                this.chart.on('click',function(params){
                    console.log(params)
                })
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