<template>
<!--    <div id="tips"></div>-->
<!--    <div id="nanobar">-->
<!--        <div id="bar"></div>-->
<!--    </div>-->
    <div class="noprn">第一个 ECharts 实例</div>
    <div id="main" style="width: 600px;height:400px;"></div>
    <div class="noprn" id="printImg">打印</div>
    <div>
        12312313213123213213213213213213
    </div>
</template>

<script>
    import $ from 'jquery'
    //import axios from "axios";
    import * as echarts from 'echarts'
    //import 'nanobar'

    // //进度条设置
    // const options = {
    //     target: $("#nanobar")
    // };
    // //进度条初始化
    // const nanobar = new Nanobar( options );

    export default {
        name: "Waiting",
        data(){
            return {

            }
        },
        created() {
            // const interval=setInterval(function(){
            //     axios.request({
            //         method:'post',
            //         url:'',
            //         dataType:'text',
            //     }).then(response => {
            //         $("#tips").innerHTML="Analysing, please wait..."
            //         $("#nanobar").fadeIn()
            //         nanobar.go(response)
            //     })
            // },1000)
            //
            // axios.request({
            //     method:'post',
            //     url:'',
            //
            // })

            // 指定图表的配置项和数据
            const option = {
                title: {
                    text: '第一个 ECharts 实例'
                },
                tooltip: {},
                toolbox: {
                    show: true,
                    right: '20px',
                    feature: {
                        // 下载保存为图片
                        saveAsImage: {
                            show: true,
                            title: '下载'
                        }
                    }
                },
                // 将动画效果属性设置为false：解决获取到的echarts图不全的问题（只有坐标轴）
                animation: false,
                legend: {
                    data: ['销量']
                },
                xAxis: {
                    data: ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
                },
                yAxis: {},
                series: [{
                    name: '销量',
                    type: 'bar', //柱状图 line：折线图
                    data: [5, 20, 36, 10, 10, 20],
                    markPoint: {
                        data: [{
                            type: "max",
                            name: "Max"
                        }, {
                            type: "min",
                            name: "Min"
                        }]
                    },
                    markLine: {
                        data: [{
                            type: "average",
                            name: "Avg"
                        },
                            [{
                                symbol: "none",
                                x: "90%",
                                yAxis: "max"
                            }, {
                                symbol: "emptyCircle", //折线处，即点的形状
                                label: {
                                    position: "start",
                                    formatter: "Max"
                                },
                                type: "max",
                                name: "Top"
                            }]
                        ]
                    }
                }]
            };
            $(document).ready(function(){

                const myChart = echarts.init(document.getElementById('main'));
                myChart.setOption(option)

                const printBtn = document.getElementById('printImg');
                const canvas = document.querySelector("#main canvas")
                console.log(canvas)
                const dataUrl = canvas.toDataURL();

                printBtn.onclick = function () {
                    //doPrintByFrame(dataUrl);
                    doViewAndPrint(dataUrl);
                    // 打印预览：打印当前页所有内容，且火狐上无法预览
                    // window.print();
                };

                // 预览：因为使用window.print火狐无法预览，因此采用新打开一个窗口的方式用来展示被打印的内容
                // 打印指定区域内容：通过只将需打印的内容添加到新窗口中，实现打印指定区域
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
            })


            // 打印指定区域内容：创建iframe，同样是通过将需打印的内容添加到iframe中实现（当前窗口即可完成，不需打开新窗口）
            function doPrintByFrame(canvasUrl) {
                //判断iframe是否存在，不存在则创建iframe
                var iframe = document.getElementById("print-iframe");
                const domPrint = document.createElement('img');
                domPrint.src = canvasUrl;
                if (!iframe) {
                    iframe = document.createElement('IFRAME');
                    var doc = null;
                    iframe.setAttribute("id", "print-iframe");
                    iframe.setAttribute('style', 'position:absolute;width:0px;height:0px;left:-500px;top:-500px;');
                    document.body.appendChild(iframe);
                    doc = iframe.contentWindow.document;
                    //这里可以自定义样式
                    //doc.write("<LINK rel="stylesheet" type="text/css" href="css/print.css">");
                    doc.body.appendChild(domPrint);
                    doc.close();
                    iframe.contentWindow.focus();
                }
                domPrint.onload = function () {
                    iframe.contentWindow.print(); // 打印
                    document.body.removeChild(iframe);
                };
            }
        }
    }
</script>

<style scoped>
    /*#nanobar{*/
    /*    border: 1px solid 	#DBDBDB;*/
    /*    border-radius: 7px;*/
    /*    background: #FAFAFA;*/
    /*    width: 450px;*/
    /*    height: 14px;*/
    /*}*/
    /*#nanobar #bar{*/
    /*    border-radius: 7px;*/
    /*    background: #43CD80;*/
    /*}*/
</style>