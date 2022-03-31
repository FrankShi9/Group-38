<template>
    <div class="container-fluid">
        <div class="row align-items-center">
            <div class="col-6 offset-3">
                <div class="mb-3 align-self-start">
                    <button type="submit" class="buttonOne form-control" @click="onSubmitOne">Demand-Supply</button>
                </div>
                <div class="mb-3 align-self-start">
                    <button type="submit" class="buttonTwo form-control" @click="onSubmitTwo">RFM-Prediction</button>
                </div>
                <div class="mb-3 align-self-start">
                    <button type="submit" class="buttonThree form-control" @click="onSubmitThree">Time-Series Prediction</button>
                </div>
            </div>
        </div>
    </div>
    <div id="hiddenDiv" style="display: none; width:400px; height: 400px">
        <div>
            <input type="file" class="form-control" @change="handleFileUpload( $event )" accept=".csv" >
            <button v-on:click="submitFile()">Submit</button>
        </div>
    </div>

</template>

<script>
    import axios from "axios";
    import $ from 'jquery';
    import 'jquery-confirm'

    const formObj=$("#hiddenDiv")
    const form=formObj.clone()

    export default {
        name: "ChooseFunc",
        data(){
            return{
                file:"",
                funcNum: 0
            }
        },
        methods:{
            onSubmitOne(){
                this.funcNum=1
                window.location.href='/uploadfile?funcNum='+this.funcNum
                // $.confirm({
                //     title: 'Upload File',
                //     content: form.html(),
                //     button:{
                //         formSubmit:{
                //             text:'upload',
                //             btnClass:'btn-blue',
                //             action:function (){
                //                 console.log(2)
                //                 const data={
                //                     funcNum:this.funcNum
                //                 }
                //                 this.submitFile(data)
                //             }
                //         },
                //         cancel:{
                //             text:'cancel'
                //         }
                //     }
                // })
            },
            onSubmitTwo(){
                this.funcNum=2
                window.location.href='/uploadfile?funcNum='+this.funcNum
            },
            onSubmitThree(){
                this.funcNum=3
                window.location.href='/uploadfile?funcNum='+this.funcNum
            },
            handleFileUpload( event ){
                // a single file
                this.file = event.target.files[0];
            },

            // submitFile(data){
            //     let formData = new FormData();
            //     let postData=[data,formData]
            //     console.log(postData)
            //     formData.append('file', this.file);
            //     // issue a POST request
            //     axios.post( '',
            //         postData,
            //         {
            //             headers: {
            //                 'Content-Type': 'multipart/form-data'
            //             }
            //         }
            //     ).then(function(){
            //         console.log('SUCCESS!');
            //     }).catch(function(){
            //             console.log('FAILURE!');
            //     });

        }
    }
</script>

<style scoped>

</style>